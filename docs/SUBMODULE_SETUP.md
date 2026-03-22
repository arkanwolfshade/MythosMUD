# Git Submodule Setup for MythosMUD

This document explains the git submodule configuration for the MythosMUD project, specifically how the `data/` directory
is managed as a separate repository.

## Overview

The `data/` directory is a git submodule pointing to the private repository
`https://github.com/arkanwolfshade/mythosmud_data.git`. This separation allows:

**Independent versioning** of world data from game code

**Collaborative editing** of world data without affecting the main codebase

**Cleaner repository structure** with focused responsibilities

**Easier deployment** of data updates separate from code updates

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

1. **Personal Access Token (PAT)**: Required for accessing private repositories

2. **Secret names**: `MYTHOSMUD_PAT` or optional alias `PRIVATE_SUBMODULE_PAT` under **Settings → Secrets and variables →
   Actions**. Workflows use this **only** for cloning `mythosmud_data`, not for the parent repo checkout.

3. **Split checkout (workflows)**: `actions/checkout` uses `submodules: false` and `github.token` for the parent repo.
   A follow-up step runs `git submodule sync`, sets `submodule.data.url` to an authenticated HTTPS URL, then
   `git submodule update --init`. CI sets the plain submodule URL from `.gitmodules`, then configures
   `http.https://github.com/.extraheader` to `Authorization: basic base64(<username>:<PAT>)` (same pattern as
   `actions/checkout`), because embedding `user:pat@` in the URL still produced _Invalid username or token_ on the
   runner. Override username via **`MYTHOSMUD_GIT_USERNAME`** if the PAT owner is not `github.repository_owner`.

4. **PAT scope**: Fine-grained PAT needs **Contents: Read** on `arkanwolfshade/mythosmud_data` only; it does **not** need
   access to `MythosMUD` for CI.

5. **Debug logging**: To enable Actions step/runner debug output, set repository **secret or variable**
   `ACTIONS_STEP_DEBUG` to `true` (and optionally `ACTIONS_RUNNER_DEBUG`). See GitHub:
   [Enabling debug logging](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/enabling-debug-logging).

### PAT Requirements

**Token Type**: Fine-grained Personal Access Token

**Required Permissions:**

**Repository access**: `arkanwolfshade/mythosmud_data`

**Repository permissions**:

- Contents: `Read-only` (minimum required)
- Metadata: `Read-only` (automatically included)

**Steps to Create PAT:**

1. Go to <https://github.com/settings/tokens>

2. Click "Generate new token" → "Fine-grained personal access tokens"

3. Configure:
   - Token name: `MythosMUD-CI-Submodule-Access`

   - Expiration: [Choose appropriate duration]

   - Repository access: Only select repositories

   - Repository: `arkanwolfshade/mythosmud_data`

   - Permissions: Repository permissions → Contents → Read-only

4. Generate and copy the token
5. Add to repository secrets as `MYTHOSMUD_PAT` (used only for the `mythosmud_data` submodule step, not parent
   checkout).

### Example Workflow Configuration

```yaml
permissions:
  contents: read

jobs:
  build:
    steps:
      - uses: actions/checkout@v5
        with:
          submodules: false
          token: ${{ github.token }}
      - name: Fetch private data submodule
        env:
          SUBMODULE_PAT: ${{ secrets.MYTHOSMUD_PAT }}
          GITHUB_REPOSITORY_OWNER: ${{ github.repository_owner }}
          MYTHOSMUD_GIT_USERNAME: ${{ secrets.MYTHOSMUD_GIT_USERNAME }}
        run: |
          set -euo pipefail
          data_url="$(git config -f .gitmodules --get submodule.data.url)"
          git_user="${MYTHOSMUD_GIT_USERNAME:-${GITHUB_REPOSITORY_OWNER}}"
          pat_trim=$(printf '%s' "$SUBMODULE_PAT" | tr -d '\r\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
          git submodule sync --recursive
          git config --local submodule.data.url "${data_url}"
          basic_b64=$(printf '%s:%s' "${git_user}" "${pat_trim}" | base64 -w0)
          git config --local http.https://github.com/.extraheader "AUTHORIZATION: basic ${basic_b64}"
          GIT_TERMINAL_PROMPT=0 git -c credential.helper= submodule update --init --recursive
          git config --local --unset-all http.https://github.com/.extraheader 2>/dev/null || true
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

- Verify `MYTHOSMUD_PAT` (or `PRIVATE_SUBMODULE_PAT`) exists. If fetch of **MythosMUD** fails with _could not read
  Username_, a submodule-only PAT was likely passed as `actions/checkout` `token`; use split checkout as in `ci.yml`.
- **_Invalid username or token_ on submodule clone**: Use `OWNER:PAT` in the URL, not `x-access-token:PAT`, for
  fine-grained PATs. Set **`MYTHOSMUD_GIT_USERNAME`** to the GitHub login that created the PAT if it is not the same
  as the parent repo owner (e.g. user token accessing an org-owned data repo).
- Check that the PAT is not expired and still lists **Contents: Read** on `arkanwolfshade/mythosmud_data`
- **SAML SSO**: If the org uses GitHub Enterprise SSO, open [Fine-grained tokens](https://github.com/settings/tokens),
  find the token, and click **Configure SSO** → **Authorize** for the org

### "not our ref" error in GitHub Actions

This error occurs when the submodule points to a commit that doesn't exist in the remote repository:

```bash
# Error: fatal: remote error: upload-pack: not our ref <commit-hash>

```

**Resolution:**

1. Navigate to the submodule directory: `cd data`
2. Check if local changes need to be pushed: `git status`
3. Push local changes: `git push origin main`
4. If there are conflicts, resolve them and push again
5. Update the main repository's submodule reference:

   ```bash
   cd ..
   git submodule update --remote data
   git add data
   git commit -m "Update data submodule reference"
   ```

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

The PAT used in workflows should have minimal required permissions

- Private submodules maintain data security while allowing controlled access
- Repository access is managed through GitHub's permission system
- All submodule changes are tracked in the main repository's commit history
- PATs should be rotated regularly and have appropriate expiration dates

## Best Practices

1. **Always use `--recursive` when cloning** to get all submodules
2. **Commit submodule changes separately** from main repository changes
3. **Update submodule references** when the submodule repository changes
4. **Document submodule changes** in commit messages
5. **Test workflows** after submodule updates to ensure everything works
6. **Use fine-grained PATs** with minimal required permissions
7. **Regularly rotate PATs** and monitor their usage

## Related Documentation

[Git Submodules Documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

- [GitHub Actions Checkout Action](https://github.com/actions/checkout)

- [GitHub Token Permissions](https://docs.github.com/en/actions/security-guides/automatic-token-authentication)

- [Fine-grained Personal Access

  Tokens](<https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-fine-grained-personal-access-token>)
