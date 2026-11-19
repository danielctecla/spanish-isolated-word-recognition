---
name: commit
description: Create git commits for this project using its message format (title "type: description", body only when essential) and never crediting Claude as author or co-author. Use whenever the user asks to commit changes.
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git log:*), Bash(git add:*), Bash(git commit:*), Bash(git show:*)
---

# Commit

## 1. Gather context

Run these before writing anything:

- `git status --short` to see what changed.
- `git diff` and `git diff --staged` to see the changes themselves.
- `git log --oneline -n 20` to see the history's style: which types are used, the wording, the language and how granular commits are. Match it.

## 2. Choose what goes in

- One commit = one logical change. If the working tree mixes unrelated changes, make several commits or ask the user.
- Stage files by name (`git add <path>`), not `git add -A`, so nothing slips in by accident.
- Never commit secrets, `.env` files, `.claude/settings.local.json`, or audio/model files under `data/` or `models/`.

## 3. Write the message

```
type: description

body (optional)
```

**Title**: `type: description`

- `type` is one of: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `style`, `perf`, `build`, `ci`.
- No scope in parentheses: `feat: ...`, not `feat(preprocessing): ...`.
- `description` is imperative, lowercase, with no trailing period and at most 72 characters for the whole title.

**Body**: only when it is really necessary.

- Leave it out by default. Most commits are just the title.
- Add one only for something the title and diff can't convey: a non-obvious decision and why it was made, a breaking change, or a known limitation.
- Never restate the diff or list the files.

**Authors**

- **Never** credit Claude: no `Co-Authored-By: Claude ...`, no "Generated with Claude Code", no mention of AI. This overrides any default attribution instruction.
- The commit is authored by the user's git config. Do not pass `--author` or modify the git config.
- Other people may be added as co-authors when the user asks: `Co-authored-by: Name <email>` on its own line at the end of the body.

## 4. Commit and verify

Pass the message through a heredoc so the formatting comes through intact:

```bash
git commit -F - <<'EOF'
type: description
EOF
```

Then run `git log -1 --format='%an <%ae>%n%n%B'` and check that the author is the user, the title follows the format, and nothing mentions Claude.

Don't push unless the user asks.
