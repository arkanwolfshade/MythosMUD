# Codacy Configuration

## ⚠️ IMPORTANT: Manual Configuration File

This `.codacy/codacy.yaml` file is **manually managed** and should **NOT** be automatically modified.

## 🚫 DO NOT RUN THESE COMMANDS

The following Codacy CLI commands will **overwrite** this file and remove manual configurations:

❌ `codacy-cli init`

❌ `codacy-cli config discover`

❌ `codacy-cli config reset`

## ✅ Current Configuration

**Python Version**: 3.12.10 (matches project Python version)

**Node Version**: 24.11.0 (matches project Node version from .nvmrc)

**Lizard Tool**: Manually added for NLOC and complexity analysis (`lizard@1.17.31`)

- **Tools** (aligned with MythosMUD Codacy coding standard):
  - `bandit@1.7.8` - Python security analysis
  - `eslint@9.39.1` - JavaScript/TypeScript linting (ESLint 9)
  - `hadolint@1.0.0` - Dockerfile linter
  - `jackson-linter@1.0.0` - JSON linter
  - `lizard@1.17.31` - NLOC and complexity analysis (manually added)
  - `markdownlint@0.40.0` - Markdown linter
  - `psscriptanalyzer@1.0.0` - PowerShell script linter
  - `pylint@3.3.6` - Python code quality linter
  - `ruff@0.12.7` - Python linter/formatter (replaces flake8, isort, black)
  - `semgrep@1.78.0` - Security and best practices scanning
  - `shellcheck@0.10.0` - Shell script linter
  - `spectral@6.15.0` - API specification linter (OpenAPI/Swagger)
  - `sqlfluff@3.0.0` - SQL linting and formatting
  - `sqlint@0.2.1` - SQL linting (NOTE: Not installed locally due to dependency conflict with click>=8.1.8; use sqlfluff instead)
  - `stylelint@16.0.0` - CSS linter
  - `trivy@0.66.0` - Dependency security scanner

## 🔧 Protection Mechanisms

1. **Workspace Settings**: `codacy.autoDiscover = false`, `codacy.autoSync = false`
2. **Editor Read-Only**: File marked as read-only in workspace settings
3. **Git Attributes**: File marked with `-diff -merge` to prevent accidental merges
4. **Pre-commit Hook**: Script checks for required tools before commits

## 🔧 If You Need to Update

1. **Manually edit** `.codacy/codacy.yaml`
2. **Do NOT** run `config discover` or `init` commands
3. **Preserve** the `lizard@1.17.31` tool entry
4. **Keep** Python version at 3.12.10
5. **Keep** Node version at 24.11.0 (matches project Node version from .nvmrc)
6. **Maintain** all tools listed in the MythosMUD Codacy coding standard

## 🐛 If File Gets Modified

If this file is modified by Codacy extension or CLI:

1. **Check workspace settings**: Verify `codacy.autoDiscover` and `codacy.autoSync` are `false`

2. **Check extension**: Disable Codacy extension auto-discovery/sync if enabled

3. **Restore from git**: `git checkout .codacy/codacy.yaml`

4. **Verify tools**: Ensure all tools from the MythosMUD Codacy coding standard are present:
   - `lizard@1.17.31`, `semgrep`, `eslint@9.39.1`, `ruff`, `bandit`, `pylint`

   - `hadolint`, `jackson-linter`, `markdownlint`, `psscriptanalyzer`

   - `shellcheck`, `spectral`, `sqlfluff`, `sqlint`, `stylelint`, `trivy`

5. **Check Python version**: Should be `3.12.10`, not `3.11.11`
6. **Check Node version**: Should be `24.11.0` (matches `.nvmrc`), not `22.2.0`

## 🔍 Troubleshooting

If the file keeps getting modified:

1. Check VS Code/Cursor user settings (may override workspace settings)
2. Disable Codacy extension entirely if not needed
3. Check for any scripts or CI/CD that might run `codacy-cli config discover`
4. Review extension logs for Codacy-related activity

## 🪟 Codacy CLI on Windows (WSL)

Codacy CLI v2 supports **Windows via WSL only** (see [codacy/codacy-cli-v2](https://github.com/codacy/codacy-cli-v2)).

**Install (one-time):**

1. Open a **WSL terminal** (e.g. Ubuntu from the Start menu).
2. Run the official installer:

   ```bash
   bash <(curl -Ls https://raw.githubusercontent.com/codacy/codacy-cli-v2/main/codacy-cli.sh)
   ```

3. Add the CLI to your shell so `codacy-cli` is available in future sessions. Either paste the block from `.codacy/wsl-bashrc-codacy.sh` into `~/.bashrc`, or run:

   ```bash
   sed 's/\r$//' /mnt/e/projects/GitHub/MythosMUD/.codacy/wsl-bashrc-codacy.sh >> ~/.bashrc
   ```

4. Start a **new** WSL terminal (or run `source ~/.bashrc`), then run:

   ```bash
   codacy-cli version
   ```

**Note:** The alias/PATH in `.bashrc` runs only in **interactive** WSL sessions. From PowerShell, run Codacy via WSL, e.g.:

`wsl ~/.cache/codacy/codacy-cli-v2/<version>/codacy-cli-v2 analyze` (replace `<version>` with the folder name under `~/.cache/codacy/codacy-cli-v2/`).
