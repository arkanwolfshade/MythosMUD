# GitHub Actions Runner Parity Container

## Purpose

Human reader: replicate the default `ubuntu-latest` (Ubuntu 24.04) runner with only the tooling MythosMUD CI jobs
  require, enabling local reproduction of workflow failures.

- AI reader: container expected to build from `Dockerfile.github-runner` at project root.

## Build Instructions

```bash
docker build -t mythosmud-gha-runner -f Dockerfile.github-runner .
```

## Usage Patterns

### Interactive debugging

  ```bash
  docker run --rm -it \
    -v "${PWD}:/workspace" \
    mythosmud-gha-runner \
    bash
  ```

### Execute backend workflow

  ```bash
  docker run --rm -it mythosmud-gha-runner \
    bash -lc 'source .venv/bin/activate && make lint && make test'
  ```

### Execute frontend workflow

  ```bash
  docker run --rm -it mythosmud-gha-runner \
    bash -lc "cd client && npm run build"
  ```

## Validation Checklist

Python tooling: `.venv` created via `uv venv`; `uv pip list` reports MythosMUD packages.

- Playwright: `playwright install chromium` already executed during build; verify with `playwright show-trace --help`.

- Node tooling: `node --version` reports v22.x; `npm install` completed in `/workspace/client`.

- Database prep: `server/tests/scripts/init_test_db.py` and `verify_test_db.py` run successfully during image build.

- CI parity: running `make lint`, `pre-commit run mypy --all-files`, and `python -m pytest server/tests/ --cov=server

  ...` inside the container should match GitHub Actions behavior.

## Security and Secrets Management

### Local Development (Default Behavior)

The Dockerfile includes test/CI-only default values for secrets. These are safe for local development but **must never
be used in production**.

### Default test values

`POSTGRES_PASSWORD=Cthulhu1` (test database password)

- `MYTHOSMUD_ADMIN_PASSWORD=test-admin-password`
- `MYTHOSMUD_SECRET_KEY=test-secret-key-for-ci-workflow`
- `MYTHOSMUD_JWT_SECRET=test-jwt-secret-for-ci-workflow`
- `MYTHOSMUD_RESET_TOKEN_SECRET=test-reset-token-secret-for-ci-workflow`
- `MYTHOSMUD_VERIFICATION_TOKEN_SECRET=test-verification-token-secret-for-ci-workflow`

### Using GitHub Secrets (CI Builds)

When building the Docker image in GitHub Actions workflows, use GitHub Secrets via `--build-arg`:

```yaml
- name: Build Docker image with secrets
  run: |
    docker build \
      --build-arg POSTGRES_PASSWORD="${{ secrets.POSTGRES_PASSWORD }}" \
      --build-arg MYTHOSMUD_ADMIN_PASSWORD="${{ secrets.MYTHOSMUD_ADMIN_PASSWORD }}" \
      --build-arg MYTHOSMUD_SECRET_KEY="${{ secrets.MYTHOSMUD_SECRET_KEY }}" \
      --build-arg MYTHOSMUD_JWT_SECRET="${{ secrets.MYTHOSMUD_JWT_SECRET }}" \
      --build-arg MYTHOSMUD_RESET_TOKEN_SECRET="${{ secrets.MYTHOSMUD_RESET_TOKEN_SECRET }}" \
      --build-arg MYTHOSMUD_VERIFICATION_TOKEN_SECRET="${{ secrets.MYTHOSMUD_VERIFICATION_TOKEN_SECRET }}" \
      -t mythosmud-gha-runner \
      -f Dockerfile.github-runner .
```

### Using GitHub Environments

For different deployment stages (development, staging, production), use GitHub Environments:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    environment: production  # or staging, development
    steps:
      - name: Build with environment secrets
        run: |
          docker build \
            --build-arg MYTHOSMUD_SECRET_KEY="${{ secrets.MYTHOSMUD_SECRET_KEY }}" \
            ...
```

### Setting up GitHub Environments

1. Go to repository Settings → Environments
2. Create environments (e.g., `development`, `staging`, `production`)
3. Add environment-specific secrets
4. Configure protection rules (required reviewers, deployment branches)

### Runtime Secret Override

For maximum security, override secrets at runtime instead of build time:

```bash
docker run --rm -it \
  -e MYTHOSMUD_SECRET_KEY="$MYTHOSMUD_SECRET_KEY" \
  -e MYTHOSMUD_JWT_SECRET="$MYTHOSMUD_JWT_SECRET" \
  mythosmud-gha-runner \
  bash
```

This ensures secrets are never baked into image layers.

## Notes

Human reader: container runs as root; adjust volume permissions if needed when binding host workspace.

- AI reader: avoid installing additional tooling inside image to keep parity scope narrow.

- Both: pass secrets via `-e` flags, Compose, or `.act.secrets`; the image intentionally ships without baked

  credentials.

**Security**: Test defaults in Dockerfile are for local development only. Production builds must use GitHub Secrets or

  runtime environment variables.

## ACT Integration

Copy `.act.secrets.example` to `.act.secrets` and populate required tokens (e.g., `MYTHOSMUD_PAT`,
  `SEMGREP_APP_TOKEN`).

- `.actrc` maps `ubuntu-latest` to `mythosmud-gha-runner:latest`, so `act` reuses the local parity image.
- Run the full CI workflow locally:

  ```bash
  make test-comprehensive
  ```

  This command rebuilds the runner image and executes both `backend` and `frontend` jobs from `.github/workflows/ci.yml`
  via `act`.
