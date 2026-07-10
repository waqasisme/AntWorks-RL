---
description: Advance the AntWorks-RL /teach loop — review the just-finished exercise, then generate the next lesson.
argument-hint: "[optional: a specific lesson id like 0.3, or notes on what you did]"
---

You are running the AntWorks-RL teaching loop. The file-based teaching workspace lives in `learning/`. Follow the `/teach` philosophy: **knowledge → skill → feedback → references**, ZPD-tight, user writes all project code.

## Steps

1. **Load state.** Read `learning/ROADMAP.md` (checkbox state = source of truth for position), `learning/MISSION.md`, `learning/GLOSSARY.md`, and every file in `learning/learning-records/`. Identify the current 🟦 in-progress lesson (or the next ⬜ if none is in progress).

2. **Review the completed exercise.** Inspect the actual repo state for the current lesson's deliverables (read the relevant source/config/test files, run the lesson's acceptance check if it is a shell command, check `git status`/`git diff`). Judge against the exercise's stated acceptance criteria in that lesson's explainer under `learning/explainers/`.
   - If **incomplete or flawed**: do NOT advance. Give specific, kind, actionable feedback and stop. Coach; don't hand over the full answer.
   - If **complete**: continue.

3. **Record learning.** If the user demonstrated non-trivial understanding, a corrected misconception, or disclosed prior knowledge, write a new `learning/learning-records/NNNN-slug.md` (increment the highest existing number; format = short title + 1–3 sentences). Graduate any now-understood terms into `learning/GLOSSARY.md` (tight definitions, per its format).

4. **Advance the roadmap.** Flip the finished lesson to ✅ and the next lesson to 🟦 in `learning/ROADMAP.md`. If the next item is a phase whose lessons are not yet decomposed, decompose it into ~3–8 lesson-sized units now (just-in-time), consistent with the locked design in `learning/learning-records/0002-locked-design-decisions.md`.

5. **Generate the next lesson explainer.** Create `learning/explainers/lesson-<id>-<slug>.html`: a self-contained, beautiful, theme-aware HTML page (inline CSS/JS, no external assets) matching the style of `lesson-0.1-modern-python-scaffolding.html`. It must include: why-this-lesson (tied to MISSION), the knowledge grounded in `learning/RESOURCES.md` (never parametric guesses — web-search to verify/extend sources if needed and append them to RESOURCES.md), an interactive self-check with instant feedback, a clearly-scoped **you-code-this** exercise with explicit acceptance criteria, and a **deep-dive references** section spanning the domains it touches (Python / ML / RL / ant biology).

6. **Hand off.** Print the `open "<absolute path>"` command for the new explainer and a 2–3 line summary of what the lesson covers and its exercise. Remind the user: they write the code; ping for review (or re-run `/next-lesson`) when done.

Extra context / notes from the user: $ARGUMENTS
