# Data Analytics Master Handbook Standard (DAMS v2.0)

**Status:** Active

**Purpose:** Define the quality contract for every chapter in the Data Analytics Master Handbook. DAMS v2.0 preserves the 25-section structure from v1.0 and adds source traceability, code metadata, difficulty labels, cross-references, and version history.

## Project KPI

The delivery target is **at least one publishable chapter per week**, with **two chapters per week** as a stretch goal. Quality gates take priority over the schedule; a chapter is not published merely to meet the weekly target.

## Chapter Contract

Every chapter must use these sections, in this order:

1. Learning Objectives
2. Prerequisites
3. Introduction
4. History (if applicable)
5. Why This Topic Matters
6. Core Theory
7. Internal Working
8. Visual Diagram
9. Syntax
10. Examples (Easy to Advanced)
11. Real-world Applications
12. Best Practices
13. Common Mistakes
14. Debugging Tips
15. Performance Notes
16. Interview Questions
17. MCQs
18. Coding Exercises
19. Assignments
20. Mini Project
21. Case Study
22. Summary
23. Cheat Sheet
24. Glossary
25. References

A section may state that it is not applicable, but it must not silently disappear. Chapters use the title format `Chapter X - Title` and should link to their runnable code, datasets, diagrams, exercises, and projects where those resources exist.

Every chapter must also end with a **Looking Ahead** section naming the next chapter and explaining how it follows from the current chapter.

## Statement Confidence

Use a confidence label when a statement could be confused with a universal language rule, an implementation detail, or a recommendation:

| Label | Use for |
| --- | --- |
| Established Fact | Claims supported by official documentation, standards, or authoritative references. |
| Implementation Detail | Behavior true for a named implementation, such as CPython, but potentially different elsewhere. |
| Best Practice | A community or project recommendation rather than a language rule. |

Labels clarify scope; they do not replace references or need to appear on ordinary prose that is already unambiguous.

## Source Policy

Every factual statement must have an appropriate source category:

| Statement type | Required source |
| --- | --- |
| Language rule | Language specification or official Python documentation |
| Library behavior | Official library documentation |
| Historical claim | Primary or reputable historical source |
| Performance claim | Reproducible benchmark or cited evidence |
| Opinion | Clearly marked as opinion or recommendation |

Use inline links or a nearby reference marker when a claim needs support. References must be relevant, accessible, and listed in Section 25.

## Code Verification Policy

Every code block that readers may run must include metadata identifying its target environment and verification state:

```text
Python Version: 3.12+
Status: Tested
Expected Output: Yes
Dependencies: None
```

Adapt the fields for SQL, shell, or another language when needed. Code metadata must state the relevant version, whether the example was tested, whether output is provided, and all dependencies. Untested code must never be labeled `Tested`.

## Difficulty Tags

Label each example with one of these progression tags:

- `[Beginner]`
- `[Intermediate]`
- `[Advanced]`

Examples should normally progress from Beginner to Advanced. A chapter may omit a level only when the topic genuinely does not support that progression.

## Cross-References

Every chapter must include a **See also** list linking to related chapters. Links should use stable repository-relative paths or chapter links and should explain the relationship when it is not obvious.

## Version History

Every chapter must include a version history recording meaningful milestones. At minimum, use entries equivalent to:

```text
v0.1 Initial Draft
v0.2 Technical Review
v0.3 Added Examples
v0.4 Added Exercises
v1.0 Published
```

Do not add a version entry for trivial spelling or formatting changes. The current version in the chapter front matter must match the latest version-history entry.

## Documentation Coverage

Every chapter must include a Coverage Checklist showing which learning and publication components are complete. The checklist must distinguish completed content from pending review work.

At minimum, track:

- Theory
- Internal Working
- Diagrams
- Runnable Examples
- Practice
- Assignments
- Interview Questions
- Cheat Sheet
- References
- Technical Review
- Final QA

## Quality Levels

| Level | Meaning | Promotion evidence |
| --- | --- | --- |
| 1 star | Draft | All required sections exist; content is incomplete or not yet reviewed. |
| 2 stars | Reviewed | Structure, clarity, terminology, and factual claims have received review. |
| 3 stars | Tested | Code examples, commands, queries, exercises, and expected outputs have been executed or checked. |
| 4 stars | Production Ready | Links, formatting, accessibility, prerequisites, answers, and supporting assets are complete. |
| 5 stars | Book Quality | The chapter is coherent, progressive, realistic, referenced, and passes final editorial and technical review. |

A chapter cannot enter `Completed` on the project board until it reaches 5 stars.

Stage and quality are independent fields. Use `Stage` for workflow position and `Quality` for evidence maturity. For example, a chapter may remain in `QA` at 3 stars while rendering or editorial issues are resolved, then advance to 4 or 5 stars without changing its stage.

Valid stages are: `Draft`, `Review`, `Revision`, `QA`, and `Published`.

## Development Process

Each chapter follows this sequence:

1. **Research** - Gather authoritative references and identify the scope.
2. **Outline** - Map the topic to all 25 sections and the required closing material.
3. **Draft v1.0** - Explain the ideas with precise, readable prose.
4. **Technical Review** - Review accuracy, pedagogy, examples, claims, and references.
5. **Corrections** - Resolve findings and record the resulting draft version.
6. **Draft v1.1** - Produce the corrected manuscript.
7. **Code Verification** - Execute examples, commands, queries, and exercises where applicable.
8. **Grammar Review** - Check language, consistency, formatting, and accessibility.
9. **Technical Accuracy Check** - Confirm corrections introduced no new errors.
10. **Final v2.0** - Approve the complete manuscript for publication.
11. **Git Commit** - Commit the approved chapter and supporting assets with a descriptive message.

## Minimum Review Gate

Before a chapter is marked 5 stars, verify:

- The 25-section contract is complete and in order.
- `Looking Ahead`, `See also`, and `Version History` are present.
- Learning objectives match examples and assessments.
- Every runnable code block has accurate verification metadata.
- Every example has an appropriate difficulty tag.
- Source categories and references satisfy the Source Policy.
- Exercises include enough information to start and a solution or rubric where appropriate.
- Diagrams, tables, code blocks, and links render correctly.
- The chapter has been read as a learner, not only checked as an author.
- The chapter quality rating, current version, and review date are recorded.
- The Coverage Checklist is present and accurately reflects the chapter state.

## Working Roles

| Role | Responsibilities |
| --- | --- |
| Technical Author | Research assistant, instructor, technical author, and documentation writer. |
| Technical Reviewer | Technical review, quality assurance, code testing, and editorial review. |

The roles describe responsibilities, not identity. Additional specialist reviewers may be added when the subject requires them.

## Definition of Done

A chapter may be tagged `v1.0` and moved to `Completed` only when:

- Technical accuracy has been verified.
- The explanation is readable for the intended learner.
- Working code and expected outputs have been tested.
- DAMS structure and required metadata are complete.
- Markdown formatting and links have been checked.
- References have been added wherever claims require support.
- Technical, editorial, and learner-focused reviews are complete.
- The chapter has been explicitly approved for publication.

The final test is: **Would we enthusiastically recommend this chapter to someone learning the topic for the first time?** If not, the chapter remains in review or improvement.

## Version 1.0 Scope

Version 1.0 targets 40 Python chapters, 35 SQL chapters, 30 Pandas chapters, Statistics fundamentals, Git and GitHub, and Linux basics. The scope is a delivery target; DAMS v2.0 remains the quality gate for every included chapter.
