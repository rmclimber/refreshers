#!/usr/bin/env python3
"""Export a canonical Markdown course using Pandoc; no Python deps by default."""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def traditional(text):
    try:
        from opencc import OpenCC
    except ImportError as exc:
        raise RuntimeError(
            "Traditional export needs OpenCC. Run: "
            "python -m pip install -r requirements-traditional.txt"
        ) from exc
    converter = OpenCC("s2t")
    # Preserve fenced/inline code, Markdown link targets, and bare URLs.
    protected = re.compile(
        r"(```[\s\S]*?```|~~~[\s\S]*?~~~|`[^`\n]+`|"
        r"\]\([^\n)]*\)|https?://[^\s<>]+)"
    )
    parts = protected.split(text)
    converted = "".join(
        part if i % 2 else converter.convert(part)
        for i, part in enumerate(parts)
    )
    converted = converted.replace(
        "· Simplified characters",
        "· Traditional characters (automatically converted; not regionally adapted)",
    )
    return converted.replace(
        "Traditional characters can be generated from this edition; that changes the script, not the regional variety.",
        "This traditional-character edition is generated from the simplified source; the regional variety is unchanged.",
    )


def run(command):
    result = subprocess.run(command, capture_output=True, text=True,
                            encoding="utf-8", errors="replace")
    if result.returncode:
        raise RuntimeError(
            f"Command failed ({result.returncode}): {command[0]}\n"
            f"{result.stdout}\n{result.stderr}"
        )
    if result.stderr.strip():
        print(result.stderr.strip(), file=sys.stderr)


def build(args):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.course):
        raise RuntimeError("Course ID must use lowercase letters, digits, and hyphens.")
    course_dir = ROOT / "courses" / args.course
    source = course_dir / "course.md"
    metadata = json.loads((course_dir / "course.json").read_text(encoding="utf-8"))
    text = source.read_text(encoding="utf-8")
    if args.script == "traditional":
        if not metadata.get("cjk"):
            raise RuntimeError("Traditional conversion is only enabled for CJK courses.")
        text = traditional(text)
    formats = ["markdown", "html", "pdf"] if args.format == "all" else [args.format]
    pandoc = shutil.which("pandoc")
    if any(f != "markdown" for f in formats) and not pandoc:
        raise RuntimeError("Pandoc was not found on PATH. Install it or export --format markdown.")
    if "pdf" in formats and not shutil.which("xelatex"):
        raise RuntimeError("XeLaTeX was not found on PATH. Install MiKTeX or TeX Live.")
    output = Path(args.output_dir).resolve() if args.output_dir else ROOT / "output"
    output.mkdir(parents=True, exist_ok=True)
    stem = f"{args.course}-{args.script}"
    # All formats are staged before any published reading edition is replaced.
    with tempfile.TemporaryDirectory(prefix=".build-", dir=output) as temporary:
        stage = Path(temporary)
        staged_md = stage / (stem + ".md")
        staged_md.write_text(text, encoding="utf-8")
        # Render the source H1 as Pandoc's title block, with modules at level 1.
        reading_source = stage / "reading.md"
        reading_source.write_text(re.sub(r"\A# [^\n]+\n", "", text, count=1),
                                  encoding="utf-8")
        staged_metadata = stage / "metadata.json"
        staged_metadata.write_text(json.dumps({
            "title": metadata["title"],
            "subtitle": metadata.get("subtitle", ""),
            "date": f"{metadata['version']} | {metadata['date']}",
            "pagetitle": metadata["title"],
            "lang": metadata.get("lang", "en-US"),
        }), encoding="utf-8")
        common = [str(pandoc), str(reading_source), "--from=markdown", "--standalone",
                  "--shift-heading-level-by=-1", "--toc",
                  f"--metadata-file={staged_metadata}"]
        staged = []
        for fmt in formats:
            suffix = ".md" if fmt == "markdown" else "." + fmt
            artifact = stage / (stem + suffix)
            if fmt == "html":
                run(common + ["--to=html5", "--toc-depth=2", "--embed-resources",
                              f"--css={ROOT / 'styles' / 'reading.css'}",
                              "--output", str(artifact)])
            elif fmt == "pdf":
                command = common + [
                    "--pdf-engine=xelatex", "--toc-depth=1", "--variable=documentclass:article",
                    "--variable=fontsize:11pt", "--variable=geometry:margin=23mm",
                    "--variable=colorlinks:true", "--variable=linkcolor:MidnightBlue",
                    "--variable=urlcolor:MidnightBlue",
                    f"--include-in-header={ROOT / 'styles' / 'pdf-header.tex'}",
                    "--output", str(artifact),
                ]
                if metadata.get("cjk"):
                    font = args.cjk_font or (
                        "Microsoft YaHei" if os.name == "nt" else "Noto Sans CJK SC"
                    )
                    command += [f"--variable=CJKmainfont:{font}"]
                main_font = args.main_font or ("Calibri" if os.name == "nt" else None)
                math_font = args.math_font or ("Cambria Math" if os.name == "nt" else None)
                if main_font:
                    command += [f"--variable=mainfont:{main_font}"]
                if math_font:
                    command += [f"--variable=mathfont:{math_font}"]
                run(command)
            staged.append((artifact, output / fmt / artifact.name))
        for artifact, destination in staged:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(artifact, destination)
            print(destination)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--course", default="mandarin-grammar")
    parser.add_argument("--format", choices=["markdown", "html", "pdf", "all"], default="all")
    parser.add_argument("--script", choices=["simplified", "traditional"], default="simplified")
    parser.add_argument("--cjk-font", help="Installed CJK font family for XeLaTeX")
    parser.add_argument("--main-font", help="PDF text font (Windows default: Calibri)")
    parser.add_argument("--math-font", help="PDF math font (Windows default: Cambria Math)")
    parser.add_argument("--output-dir", help="Output root (default: repository output/)")
    args = parser.parse_args()
    try:
        build(args)
    except (RuntimeError, OSError, ValueError, KeyError) as exc:
        parser.exit(1, f"Build error: {exc}\n")


if __name__ == "__main__":
    main()
