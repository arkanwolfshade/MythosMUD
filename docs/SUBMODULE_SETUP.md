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

### Official GitHub documentation (authoritative)

These pages are the canonical references for how we wire workflows (summarized from Context7 against GitHub Docs /
Actions docs):

1. **`GITHUB_TOKEN` scope** — The automatic token is tied to the **repository that contains the workflow**, not to
   sibling private repos. That is why `mythosmud_data` cannot be cloned with `github.token` alone.
   [Automatic token authentication](https://docs.github.com/en/actions/security-guides/automatic-token-authentication)

2. **Secrets** — Store the PAT as an Actions secret and pass it via `secrets.*`; never hardcode tokens in YAML.
   [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)

3. **`actions/checkout` and `token`** — Checkout accepts a `token` input for authenticated git operations; we use
   `github.token` for the **parent** repo and a separate secret only for the submodule step.
   [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
   (see examples for checking out a **different** private repository with a PAT).

4. **Submodules** — `actions/checkout` supports `submodules`; we set `submodules: false` and initialize `data` in a
   follow-up step (same idea as migration docs).
   [Migrating from Travis CI to GitHub Actions](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions)

5. **HTTPS Git with a PAT** — Over HTTPS, Git expects a username and **password = PAT** (not your account password).
   [Managing personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#using-a-personal-access-token-on-the-command-line)

6. **`x-access-token` in the clone URL** — GitHub documents HTTPS clones as
   `https://x-access-token:TOKEN@github.com/owner/repo.git` for installation tokens; the same URL shape is the standard
   automation pattern for embedding a token (we use it for **fine-grained** `github_pat_*` tokens).
   [Authenticating as a GitHub App installation](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation)

7. **Embedding tokens in URLs** — Putting a token in a remote URL can leave it visible in local Git configuration; only
   do this in trusted automation with **least-privilege** tokens (our step restores the plain submodule URL afterward).
   [Troubleshooting authentication to a repository](https://docs.github.com/en/codespaces/troubleshooting-github-codespaces/troubleshooting-authentication-to-a-repository)

### Required Configuration

1. **Personal Access Token (PAT)**: Required for accessing private repositories

2. **Secret name**: `MYTHOSMUD_PAT` under **Settings → Secrets and variables → Actions**. Workflows use this **only**
   for cloning `mythosmud_data`, not for the parent repo checkout.

3. **Split checkout (workflows)**: First `actions/checkout` uses `submodules: false` and **`github.token`** for the
   parent repo only. A bash step reads **`.gitmodules`** and **`git ls-tree HEAD data`** for **`OWNER/REPO`** and the
   **pinned SHA**. A second step runs **`git init` / `git fetch --depth 1`** into **`data/`** using an HTTPS remote with
   **URL-encoded** `user:token` (`github_pat_*` → **`x-access-token`**; classic **`ghp_`** →
   **`github.repository_owner`**). A second **`actions/checkout`** with `repository` + `token` was unreliable for
   **`git fetch`** on hosted runners, so workflows use explicit **`git fetch`** instead. Do not commit a stray **`tmp`**
   gitlink; keep **`tmp/`** gitignored for local scratch.

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

See `.github/workflows/ci.yml` (**Resolve data submodule** + **Clone private data into data/**). Minimal sketch:

```yaml
- uses: actions/checkout@v5
  with:
    submodules: false
    token: ${{ github.token }}
- id: data_submodule
  run: |
    set -euo pipefail
    u="$(git config -f .gitmodules --get submodule.data.url)"
    u="${u#https://github.com/}"; u="${u%.git}"
    sha=$(git ls-tree HEAD data | awk '{print $3}')
    echo "repository=${u}" >> "${GITHUB_OUTPUT}"
    echo "sha=${sha}" >> "${GITHUB_OUTPUT}"
- env:
    SUBMODULE_PAT: ${{ secrets.MYTHOSMUD_PAT }}
    GITHUB_REPOSITORY_OWNER: ${{ github.repository_owner }}
  run: |
    set -euo pipefail
    pat=$(printf '%s' "$SUBMODULE_PAT" | tr -d '\r\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    case "$pat" in github_pat_*) U=x-access-token ;; *) U=$GITHUB_REPOSITORY_OWNER ;; esac
    export GIT_USER_Q="$U" PAT_Q="$pat"
    auth=$(python3 -c "import os, urllib.parse as u; print(u.quote(os.environ['GIT_USER_Q'],safe='')+':'+u.quote(os.environ['PAT_Q'],safe=''))")
    unset GIT_USER_Q PAT_Q
    rm -rf data && mkdir data && cd data
    git init -q && git remote add origin "https://${auth}@github.com/${{ steps.data_submodule.outputs.repository }}.git"
    GIT_TERMINAL_PROMPT=0 git fetch --depth 1 origin "${{ steps.data_submodule.outputs.sha }}"
    git checkout -q FETCH_HEAD
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

- Verify `MYTHOSMUD_PAT` exists. If fetch of **MythosMUD** fails with _could not read
  Username_, a submodule-only PAT was likely passed as `actions/checkout` `token`; use split checkout as in `ci.yml`.
- **_Invalid username or token_ on submodule clone**: Regenerate the PAT, confirm **Contents: Read** on
  `mythosmud_data`, and **authorize SSO** if your org requires it. CI uses **`x-access-token`** as the HTTPS username for
  fine-grained tokens (`github_pat_*`) and **`github.repository_owner`** for classic (`ghp_*`).
- **No url found for submodule path `tmp`**: A path is recorded as a **gitlink** (mode 160000) but has no
  `submodule.<name>.url` in `.gitmodules`. CI only runs `git submodule update ... -- data`. Remove the stray entry with
  `git rm --cached tmp` and add **`tmp/`** to `.gitignore` so scratch/log exports are not committed as submodules.
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
