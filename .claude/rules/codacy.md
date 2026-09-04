---
description: "Configuration for AI behavior when interacting with Codacy's MCP Server: run codacy_cli_analyze after every edit and after dependency changes."
paths:
  - "server/**"
  - "client/**"
  - "**/*.py"
  - "**/*.ts"
  - "**/*.tsx"
---

# Codacy Rules

Configuration for AI behavior when interacting with Codacy's MCP Server (`codacy` — registered via
`claude mcp add codacy -- npx -y @codacy/codacy-mcp@latest`).

## Using any tool that accepts `provider`, `organization`, or `repository`

- ALWAYS use:
  - provider: `gh`
  - organization: `arkanwolfshade`
  - repository: `MythosMUD`
- Avoid calling `git remote -v` unless really necessary

## CRITICAL: After ANY successful file edit

- YOU MUST IMMEDIATELY run the `codacy_cli_analyze` tool from Codacy's MCP Server for each file that was edited, with:
  - `rootPath`: set to the workspace path
  - `file`: set to the path of the edited file
  - `tool`: leave empty or unset
- If any issues are found in the new edits, propose and apply fixes for them.
- Failure to follow this rule is considered a critical error.

## When `codacy_cli_analyze` fails because the Codacy CLI is not installed

- Ask the user "Codacy CLI is not installed. Would you like me to install it now?"
- If yes, run the `codacy_cli_install` tool and continue with the original task
- If no, tell the user they can disable automatic analysis, and don't run it again this session
- Wait for the user to respond before proceeding

## After every response

- If you made any file edits in this conversation, verify you ran `codacy_cli_analyze`

## When Codacy MCP tools are unavailable or unreachable

- Suggest the user check `claude mcp get codacy` for connection status
- If that doesn't resolve it, suggest contacting Codacy support

## Trying to call a tool that needs a `rootPath` parameter

- Always use the standard, non-URL-encoded file system path

## CRITICAL: Dependencies and Security Checks

- IMMEDIATELY after any of these actions:
  - Running npm/yarn/pnpm install
  - Adding dependencies to `package.json`
  - Adding requirements to `requirements.txt`/`pyproject.toml`
  - Any other package manager operations
- You MUST run `codacy_cli_analyze` with:
  - `rootPath`: set to the workspace path
  - `tool`: set to `"trivy"`
  - `file`: leave empty or unset
- If any vulnerabilities are found in the newly added packages:
  - Stop all other operations
  - Propose and apply fixes for the security issues
  - Only continue with the original task after security issues are resolved

## General

- Repeat the relevant steps for each modified file.
- "Propose fixes" means to both suggest and, if possible, automatically apply the fixes.
- You MUST NOT wait for the user to ask for analysis or remind you to run the tool.
- Do not run `codacy_cli_analyze` looking for changes in duplicated code, complexity metrics, or code coverage —
  those are handled by this project's own `make codacy-tools` / `mythosmud-pre-commit-checklist` workflow, not
  per-edit analysis.
- Do not try to manually install Codacy CLI via brew/npm/npx/etc. — use `codacy_cli_install` from the MCP server.
- When calling `codacy_cli_analyze`, only send `provider`/`organization`/`repository` if the project is a git repository.

## Whenever a Codacy tool using `repository` or `organization` returns a 404

- Offer to run `codacy_setup_repository` to add the repository to Codacy
- If the user accepts, run it — never run it unprompted
- After setup, immediately retry the action that failed (only retry once)

---

*Ported from `.cursor/rules/codacy.mdc` (always-on in Cursor). Trimmed the VS Code/GitHub Copilot-specific
troubleshooting section since it doesn't apply to Claude Code.*
