# Authoring a refresher

## Start with the returning reader

Specify what the reader once knew, what likely remains, and what they should be able to do again. Choose a few observable outcomes. Define omissions before expanding the outline.

Copy `templates/course.md` to `courses/<course-id>/course.md`. Add a `course.json` alongside it with `title`, `subtitle`, `version`, `date`, `lang`, and `cjk` keys; see the Mandarin course for an example. Set `cjk` to false for a course that does not need Chinese typesetting. Use a lowercase, hyphenated course ID.

## Teach through compact units

A unit should usually contain:

1. **Construction / model:** a usable pattern or relationship.
2. **Meaning / use:** what problem it solves and when it applies.
3. **Examples:** at least two realistic applications for a central construction.
4. **Pitfall / contrast:** a likely error, the reason it fails, and a repair where useful.

Allow related patterns to share a unit. Do not impose identical lengths on unequal ideas. Put difficult distinctions next to each other so the reader can compare them. Use short definitions for technical terms at first use.

Use a diagnostic to route review, not to assign an unsupported proficiency label. Include a few integrated tasks, with models or rubrics. The answer key should explain why the answer works when that is the point of the question.

## Keep the source portable

- Use UTF-8, normal Markdown headings, paragraphs, lists, blockquotes, and simple tables.
- Start with one H1 course title, then H2 modules and H3 constructions. Do not put YAML metadata above the title; metadata lives in JSON so repository readers see a clean opening.
- Prefer prose and short example lists over large tables. Reserve tables for compact comparisons.
- Keep English module headings stable for internal links. Check links after renaming headings.
- Avoid raw LaTeX, manual page breaks, required JavaScript, remote fonts, and format-specific content hidden from another edition.
- Keep URLs readable through descriptive link text. Put source details in a final reference section and identify which topics they support.
- Use plain hyphens in prose and patterns to simplify PDF compatibility.

## Mandarin conventions

Use simplified source characters and natural modern conversational Mandarin. Supply an English meaning with each teaching example. Use **bold** for constructions and Chinese examples; reserve code spans for literal software/code so character conversion can safely preserve them.

Show pinyin only when it helps identify a particle, distinguish readings, or explain contextual pronunciation. Label nonstandard example sentences explicitly as incorrect or avoid them. Mark simplifications with words such as “usually” or “in this pattern” where needed; never turn a production shortcut into an absolute grammar rule.

Traditional exports use OpenCC `s2t`. URLs and code are preserved; prose and Chinese examples are converted. Check context-dependent distinctions such as 发/發/髮, 后/後, and 里/裡. Do not change source text to fix a converter error without considering both editions; document and implement a targeted conversion override if one is needed. A traditional script edition preserves the Mandarin variety of the source.

## Build and review

```sh
python scripts/build.py --course mandarin-grammar --format all
python scripts/build.py --course mandarin-grammar --format all --script traditional
```

The build uses Pandoc's Markdown reader, exports self-contained HTML with shared CSS, and uses XeLaTeX for PDFs. It renders the source H1 as a title block using JSON metadata, and promotes modules one heading level in the exports. Keep the source H1 and metadata title aligned. Shared layout is in `styles/`.

Check the Markdown in a repository viewer. Open the HTML and follow the contents links. Render every PDF page to an image and inspect for missing Chinese, clipped tables, isolated headings, or excessive blank space. Inspect extracted text as a separate check; text extraction alone cannot verify layout.

Review the content in three passes: subject accuracy, usefulness to the specified reader, and final presentation. Check the generated traditional edition independently. Keep a draft status until human subject review is complete.

If TeX reports a missing package, install it through your TeX distribution. On Windows, MiKTeX may need a user-level package setup before its first unattended build. On Linux/macOS, pass an installed font explicitly if the default is unavailable. Build failures should be fixed before replacing a release PDF.

Commit source, styles, and rebuilt reading editions together. Do not commit TeX logs, page PNGs, Python environments, or QA contact sheets. Update the course metadata when preparing a new release.
