# Refreshers

Compact courses for people who learned a subject once and want to use it again.
More explanation than a cheat sheet; much less ground to cover than an introductory textbook.
The aim is to restore a working mental model, recall the constructions that matter, and practice just enough to expose remaining gaps.

## Courses

| Course | Intended reader | Read | Download |
| --- | --- | --- | --- |
| Mandarin grammar | Native English speaker returning to previously conversational Mandarin | [Markdown](courses/mandarin-grammar/course.md) · [HTML](output/html/mandarin-grammar-simplified.html) | [Simplified PDF](output/pdf/mandarin-grammar-simplified.pdf) · [Traditional PDF](output/pdf/mandarin-grammar-traditional.pdf) |

The first course is an **editorially revised draft** (0.2), not yet independently reviewed by a Mandarin instructor. It focuses on grammar and sentence parsing, uses simplified characters as its source, and skips beginner pronunciation instruction. The traditional edition is generated and should receive its own language review.

## Project documents

- [Project brief](PROJECT_BRIEF.md): purpose, audience, scope, quality bar, and roadmap.
- [Authoring guide](docs/AUTHORING.md): course structure, editorial conventions, and review process.
- [Course template](templates/course.md): starting point for another subject.

## Build a course

Read the source directly in the repository with no software installation.
For exports, install Python 3.10+, [Pandoc](https://pandoc.org/installing.html), and a TeX distribution with XeLaTeX and `xeCJK` (for example MiKTeX or TeX Live). PDF builds need a Chinese font: Microsoft YaHei is the Windows default; Noto Sans CJK SC is the default elsewhere. Override it with `--cjk-font` if needed. Windows also defaults to Calibri and Cambria Math; other systems use Pandoc's default text/math fonts. Use `--main-font` and `--math-font` to override them.

```sh
python scripts/build.py --format all
```

This produces a standalone HTML file with embedded CSS, an exported Markdown copy, and a PDF. The checked-in simplified source is always authoritative. Generated files are named by course and script:

```text
output/markdown/mandarin-grammar-simplified.md
output/html/mandarin-grammar-simplified.html
output/pdf/mandarin-grammar-simplified.pdf
```

Generate traditional characters with [OpenCC](https://github.com/BYVoid/OpenCC), using its standard `s2t` conversion. The Python dependency is only required for this option:

```sh
python -m pip install -r requirements-traditional.txt
python scripts/build.py --format all --script traditional
```

This changes the written script, not the dialect, grammar, vocabulary, or pinyin. Ambiguous conversions need editorial review. Links and code spans are preserved. Use `--format markdown` to export without Pandoc or TeX, or `--format html` to export without TeX. Use `--help` for font, output directory, and course selection options.

The HTML export is a portable reading edition and a starting point for eventual web display. A hosted web app is a later phase.

## Repository layout

```text
courses/<course-id>/course.md    Canonical course text
courses/<course-id>/course.json  Title, version, and language metadata
docs/                           Editorial and workflow documentation
templates/                      Reusable course skeleton
scripts/build.py                Markdown / HTML / PDF exporter
styles/                         Shared HTML and PDF presentation
output/                         Generated reading editions
```

Release reading editions live in `output/` and are checked in so a reader can download a PDF immediately. Rebuild them when course text or shared styles change. Temporary build and QA files stay outside the published outputs. No content license has been selected yet; do not infer an open-content license from repository visibility.
