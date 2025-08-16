# Git Submodule Setup for MythosMUD

This document explains the git submodule configuration for the MythosMUD project, specifically how the `data/` directory is managed as a separate repository.

## Overview

The `data/` directory is a git submodule pointing to the private repository `https://github.com/arkanwolfshade/mythosmud_data.git`. This separation allows:

- **Independent versioning** of world data from game code
- **Collaborative editing** of world data without affecting the main codebase
- **Cleaner repository structure** with focused responsibilities
- **Easier deployment** of data updates separate from code updates

## Repository Structure

```
MythosMUD/ (main repository)
├── client/          # React frontend
├── server/          # Python backend
├── data/            # Git submodule → mythosmud_data repository
├── scripts/         # Utility scripts
└── docs/            # Documentation
```

## Cloning the Repository

### Option 1: Clone with submodules (Recommended)

```bash
git clone --recursive https://github.com/arkanwolfshade/MythosMUD.git
cd MythosMUD
```

### Option 2: Clone first, then fetch submodules

```bash
git clone https://github.com/arkanwolfshade/MythosMUD.git
cd MythosMUD
git submodule update --init --recursive
```

## Working with Submodules

### Updating the submodule to latest version

```bash
# From the main repository root
git submodule update --remote data
git add data
git commit -m "Update data submodule to latest version"
```

### Making changes to the data submodule

```bash
# Navigate to the submodule
cd data

# Make your changes
# ... edit files ...

# Commit changes in the submodule
git add .
git commit -m "Update world data: add new rooms"

# Push changes to the submodule repository
git push origin main

# Return to main repository and update the submodule reference
cd ..
git add data
git commit -m "Update data submodule reference"
```

### Switching to a specific submodule version

```bash
# From the main repository root
cd data
git checkout <commit-hash-or-branch>
cd ..
git add data
git commit -m "Pin data submodule to specific version"
```

## GitHub Actions Configuration

Since the `mythosmud_data` repository is private, the GitHub Actions workflows need special configuration to access it:

### Required Configuration

1. **Permissions**: Added `actions: read` permission to allow access to private repositories
2. **Token**: Use `${{ secrets.GITHUB_TOKEN }}` for authentication
3. **Submodule checkout**: Configure `submodules: recursive` in checkout action

### Example Workflow Configuration

```yaml
permissions:
  contents: read
  actions: read  # Required for private submodule access

jobs:
  build:
    steps:
      - uses: actions/checkout@v5
        with:
          submodules: recursive
          token: ${{ secrets.GITHUB_TOKEN }}
```

## Troubleshooting

### Submodule not found during clone

```bash
# If you cloned without --recursive, fetch submodules manually
git submodule update --init --recursive
```

### Permission denied accessing submodule

**For local development:**
- Ensure you have access to the `mythosmud_data` repository
- Check that your SSH keys or GitHub token are properly configured

**For GitHub Actions:**
- Verify the workflow has `actions: read` permission
- Ensure the `GITHUB_TOKEN` is being used in the checkout action
- Check that the repository has access to the private submodule

### Submodule shows as "modified" in git status

This usually means the submodule is pointing to a different commit than what's recorded in the main repository:

```bash
# To see what's different
git submodule status

# To update to the recorded version
git submodule update

# To update to the latest version
git submodule update --remote
```

### Working with multiple submodules

If you need to add more submodules in the future:

```bash
# Add a new submodule
git submodule add <repository-url> <path>

# Initialize all submodules
git submodule update --init --recursive

# Update all submodules to latest
git submodule update --remote
```

## Security Considerations

- The `GITHUB_TOKEN` used in workflows has limited scope and expires automatically
- Private submodules maintain data security while allowing controlled access
- Repository access is managed through GitHub's permission system
- All submodule changes are tracked in the main repository's commit history

## Best Practices

1. **Always use `--recursive` when cloning** to get all submodules
2. **Commit submodule changes separately** from main repository changes
3. **Update submodule references** when the submodule repository changes
4. **Document submodule changes** in commit messages
5. **Test workflows** after submodule updates to ensure everything works

## Related Documentation

- [Git Submodules Documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
- [GitHub Actions Checkout Action](https://github.com/actions/checkout)
- [GitHub Token Permissions](https://docs.github.com/en/actions/security-guides/automatic-token-authentication)
