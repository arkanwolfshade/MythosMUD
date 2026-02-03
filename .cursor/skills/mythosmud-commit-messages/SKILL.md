---
name: mythosmud-commit-messages
description: Generate conventional commit messages from git diffs: short summary, optional body, type(scope) format, link issues with #number. Use when the user asks for a commit message, to amend or write commits, or when reviewing staged changes.
---

# MythosMUD Commit Messages

## Format

- **First line:** 50–72 characters, imperative mood or past tense. Type(scope): summary.
- **Body (optional):** Bullet points for detail. No corporate boilerplate.
- **Issue link:** Include `#issue-number` when the commit relates to an issue.

## Types

| Type | Use for |
|------|--------|
| feat | New feature |
| fix | Bug fix |
| docs | Documentation only |
| refactor | Code change that neither fixes nor adds feature |
| test | Adding or updating tests |
| chore | Build, tooling, deps |

## Template

```
<type>(<scope>): <short summary>

- Optional bullet for detail
- Another bullet if needed

#issue-number
```

## Examples

**Feature with issue:**

```
feat(auth): add JWT login endpoint

Add POST /auth/login and token validation middleware.

#42
```

**Bug fix:**

```
fix(reports): correct date formatting in timezone conversion

Use UTC timestamps consistently across report generation.
```

**Docs only:**

```
docs(api): update OpenAPI spec for players endpoint
```

## Rules

- **Be direct and technical.** Avoid phrases like "reflect our commitment" or "these changes ensure."
- **Link issues** when the work addresses an issue: add `#issue-number` in the body or after the summary.
- **No trailing period** on the subject line.
- Prefer **past tense** for summary when describing what was done (e.g. "added", "fixed", "updated").
