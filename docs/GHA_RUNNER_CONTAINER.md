# GitHub Actions Runner Parity Container

## Purpose
- Human reader: replicate the default `ubuntu-latest` (Ubuntu 24.04) runner with only the tooling MythosMUD CI jobs require, enabling local reproduction of workflow failures.
- AI reader: container expected to build from `Dockerfile.github-runner` at project root.

## Build Instructions
```bash
docker build -t mythosmud-gha-runner -f Dockerfile.github-runner .
```

## Usage Patterns
- **Interactive debugging**
  ```bash
  docker run --rm -it \
    -v "${PWD}:/workspace" \
    mythosmud-gha-runner \
    bash
  ```
- **Execute backend workflow**
  ```bash
  docker run --rm -it mythosmud-gha-runner \
    bash -lc 'source .venv/bin/activate && make lint && make test'
  ```
- **Execute frontend workflow**
  ```bash
  docker run --rm -it mythosmud-gha-runner \
    bash -lc "cd client && npm run build"
  ```

## Validation Checklist
- Python tooling: `.venv` created via `uv venv`; `uv pip list` reports MythosMUD packages.
- Playwright: `playwright install chromium` already executed during build; verify with `playwright show-trace --help`.
- Node tooling: `node --version` reports v22.x; `npm install` completed in `/workspace/client`.
- Database prep: `server/tests/scripts/init_test_db.py` and `verify_test_db.py` run successfully during image build.
- CI parity: running `make lint`, `pre-commit run mypy --all-files`, and `python -m pytest server/tests/ --cov=server ...` inside the container should match GitHub Actions behavior.

## Notes
- Human reader: container runs as root; adjust volume permissions if needed when binding host workspace.
- AI reader: avoid installing additional tooling inside image to keep parity scope narrow.
- Both: pass secrets via `-e` flags, Compose, or `.act.secrets`; the image intentionally ships without baked credentials.

## ACT Integration
- Copy `.act.secrets.example` to `.act.secrets` and populate required tokens (e.g., `MYTHOSMUD_PAT`, `SEMGREP_APP_TOKEN`).
- `.actrc` maps `ubuntu-latest` to `mythosmud-gha-runner:latest`, so `act` reuses the local parity image.
- Run the full CI workflow locally:
  ```bash
  make test-comprehensive
  ```
  This command rebuilds the runner image and executes both `backend` and `frontend` jobs from `.github/workflows/ci.yml` via `act`.
