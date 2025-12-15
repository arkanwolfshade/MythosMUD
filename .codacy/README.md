# Codacy Configuration

## ⚠️ IMPORTANT: Manual Configuration File

This `.codacy/codacy.yaml` file is **manually managed** and should **NOT** be automatically modified.

## 🚫 DO NOT RUN THESE COMMANDS

The following Codacy CLI commands will **overwrite** this file and remove manual configurations:

- ❌ `codacy-cli init`
- ❌ `codacy-cli config discover`
- ❌ `codacy-cli config reset`

## ✅ Current Configuration

- **Python Version**: 3.12.10 (matches project Python version)
- **Node Version**: 24.11.0 (matches .nvmrc)
- **Go Version**: 1.22.3
- **Lizard Tool**: Manually added for NLOC and complexity analysis (`lizard@1.17.31`)
- **Tools**:
  - `bandit@1.7.8` - Python security analysis
  - `eslint@8.57.0` - JavaScript/TypeScript linting
  - `lizard@1.17.31` - NLOC and complexity analysis (manually added)
  - `pylint@3.3.6` - Python linting
  - `revive@1.7.0` - Go linting
  - `ruff@0.12.7` - Python linter/formatter (replaces flake8, isort, black)
  - `semgrep@1.78.0` - Security and best practices scanning

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
5. **Keep** Node version matching `.nvmrc` (currently 24.11.0)

## 🐛 If File Gets Modified

If this file is modified by Codacy extension or CLI:

1. **Check workspace settings**: Verify `codacy.autoDiscover` and `codacy.autoSync` are `false`
2. **Check extension**: Disable Codacy extension auto-discovery/sync if enabled
3. **Restore from git**: `git checkout .codacy/codacy.yaml`
4. **Verify tools**: Ensure `lizard@1.17.31`, `semgrep`, `eslint`, `ruff`, `bandit`, and `node@` are present
5. **Check Python version**: Should be `3.12.10`, not `3.11.11`

## 🔍 Troubleshooting

If the file keeps getting modified:

1. Check VS Code/Cursor user settings (may override workspace settings)
2. Disable Codacy extension entirely if not needed
3. Check for any scripts or CI/CD that might run `codacy-cli config discover`
4. Review extension logs for Codacy-related activity
