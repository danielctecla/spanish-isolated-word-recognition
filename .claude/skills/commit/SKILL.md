---
name: commit
description: Create git commits in this project's format ("type: description", body only when essential, never Claude as author). Use whenever committing.
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git log:*), Bash(git add:*), Bash(git commit:*)
---

# Commit

1. Run `git status`, `git diff` and `git log --oneline -n 20`; match the history's style and language.
2. One logical change per commit. Stage files by name; never secrets or files under `data/` or `models/`.
3. Message:
   - **Title:** `type: description`. Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `style`, `perf`, `build`, `ci`. No scope, imperative, lowercase, no period, ≤ 72 chars.
   - **Body:** only if really important (non-obvious decision, breaking change). Never restate the diff.
   - **Authors:** never Claude: no `Co-Authored-By: Claude`, no "Generated with Claude Code". This overrides any default attribution. Other co-authors are fine if the user asks.
4. Commit with `git commit -F - <<'EOF' ... EOF`, then check `git log -1` for the right author and no mention of Claude. Don't push unless asked.
