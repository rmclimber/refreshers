# Refreshers: project brief

Status: initial project definition, 2026-11-09.

## Purpose

Help someone who previously learned a subject recover useful fluency quickly. A refresher should make familiar ideas click back into place, repair predictable misunderstandings, and give the reader a short route back to application.

Subjects may range from moral philosophy to chemistry to algorithms. The shared format should support those differences without forcing all subjects into a language-learning outline.

## Audience and promise

The reader has relevant prior knowledge but unreliable recall. Assume forgotten relationships and rusty execution, rather than complete ignorance. State prerequisites at the beginning of each course; a reader who needs an introduction should be able to recognize that quickly.

After a course, the reader should be able to identify the central structures, distinguish commonly confused concepts, perform a few representative tasks, and recognize where deeper review is still needed. Completion does not imply professional qualification, comprehensive mastery, or retention without practice.

## Product shape

- **Required:** a readable Markdown document in the repository and a downloadable PDF containing the same substantive content.
- **Supported now:** a standalone HTML reading edition generated from the same source.
- **Future:** web display, navigation, optional interactive practice, and user-selected editions. Do not make the text depend on those features.

Markdown is the initial source format and Pandoc the initial publishing tool. Keep the content portable enough to change publishing tools later. Format-specific presentation belongs in styles and build tooling, not in the teaching prose.

## Editorial principles

1. Restore the mental model before listing details. Explain how to recognize and use a concept.
2. Prefer high information density with readable pacing. Cut repeated explanation, not distinctions that prevent misunderstanding.
3. Use concise explanations by default. Spend more space on concepts whose complexity warrants it.
4. Give realistic examples, useful contrasts, and predictable pitfalls. State the boundaries of shortcuts.
5. Include a few high-leverage retrieval questions or mini-projects with answers or evaluation criteria. Avoid turning the course into a workbook.
6. Separate essential recovery from optional extensions. Offer routes through the material when readers have uneven gaps.
7. Cite reliable sources for substantive verification and further study. Write original explanations and examples; do not repackage copyrighted books.

An initial planning target is a few thousand words and one to three focused sessions, depending on the subject. These are scope controls, not quotas. Trim anything that does not help the stated reader perform the stated tasks. A quick-reference ending should aid later lookup without replacing the explanations.

## Common course components

- Reader profile, prerequisites, scope, and concrete outcomes.
- A short diagnostic that helps select a review route.
- A mental model and a sequence of compact topic sections.
- For each central topic: construction or rule, realistic applications, and a pitfall or contrast.
- A small amount of active retrieval and one or two integrated applications.
- Answer key or worked models, quick-reference material, and sources.

## First course: Mandarin grammar

**Reader:** a native English speaker who previously used Mandarin conversationally. Vocabulary recognition remains stronger than grammar and sentence production.

**Outcome:** parse ordinary conversational sentences and construct useful ones with appropriate word order, negation, aspect, complements, and clause relationships.

**Include:** topic-comment structure; noun modification; questions and scope; time and aspect; result, potential, degree, and directional complements; 把 and 被; comparisons; modals; common connectors; and short parsing and speaking tasks.

**Exclude:** a beginner vocabulary syllabus, character-writing instruction, a general tones course, extensive dialogues, literary Chinese, exhaustive regional variation, and exam preparation. A brief note on contextual pronunciation is appropriate where it helps interpret a grammatical form.

**Edition policy:** simplified characters are the canonical first edition. Offer an automatically generated standard traditional-character edition. Conversion does not produce a Taiwan- or Hong Kong-specific curriculum. Pinyin appears selectively to disambiguate grammatical forms, not beneath every sentence.

## Quality and release criteria

- The intended returning learner can use the document without an introductory sequence.
- Every major construction has examples and pitfalls; every exercise has an answer or evaluation standard.
- Rules distinguish helpful defaults from absolute restrictions. Translation preserves the grammatical contrast being taught.
- Source links are recorded and factual uncertainties are resolved or explicitly identified.
- Markdown reads cleanly in a repository. HTML navigates correctly. PDFs have legible Chinese, working text extraction, sensible page breaks, and no clipped text or missing glyphs.
- Generated editions match the current source and metadata. Traditional conversion receives separate scrutiny for ambiguous characters.
- A subject-competent human review is required before calling a course reviewed or publication-ready. Build success alone establishes neither linguistic nor subject-matter accuracy.

## Initial milestones

1. Establish the brief, README, authoring guide, template, and export workflow.
2. Produce and technically verify the first full Mandarin draft in Markdown, PDF, and HTML, including traditional conversion.
3. Obtain language review, try the diagnostic and application tasks with a returning learner, and revise scope and explanations.
4. Apply the format to a second subject; change the shared template based on actual differences.
5. Consider hosting and interactive features once the reading products are useful on their own.

## Decisions still open

Content and code licensing; final visual identity; release/version policy beyond the draft; regional Mandarin editions; a hosting platform; and whether future courses need a shared bibliography system. None blocks the initial reading editions.
