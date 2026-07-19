# Pre Commit Config

> 15 nodes · cohesion 0.13

## Key Concepts

- **Codacy configuration** (4 connections) — `.codacy.yml`
- **Pre-commit hook configuration** (4 connections) — `.pre-commit-config.yaml`
- **Bandit configuration** (2 connections) — `bandit.yml`
- **Enforced coverage gates** (2 connections) — `.codacy.yml`
- **Codacy exclude_paths** (2 connections) — `.codacy.yml`
- **Lizard CCN and NLOC thresholds** (2 connections) — `.codacy.yml`
- **Quality Fragmentation Guard hook** (2 connections) — `.pre-commit-config.yaml`
- **70 percent and 90 percent coverage policy** (2 connections) — `TESTING.md`
- **Greenfield testing strategy** (2 connections) — `TESTING.md`
- **Bandit B101 B105 B106 test skips** (1 connections) — `bandit.yml`
- **Grype SCA exclude paths** (1 connections) — `.grype.yaml`
- **F-string logging anti-pattern detector** (1 connections) — `.pre-commit-config.yaml`
- **Mypy pre-commit hook** (1 connections) — `.pre-commit-config.yaml`
- **Ruff pre-commit hook** (1 connections) — `.pre-commit-config.yaml`
- **Unit integration E2E test tiers** (1 connections) — `TESTING.md`

## Relationships

- No strong cross-community connections detected

## Source Files

- `.codacy.yml`
- `.grype.yaml`
- `.pre-commit-config.yaml`
- `TESTING.md`
- `bandit.yml`

## Audit Trail

- EXTRACTED: 20 (71%)
- INFERRED: 8 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
