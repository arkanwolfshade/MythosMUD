---
description: "MythosMUD does not use Black — Python formatting is Ruff (scripts/format.py, make format)."
paths:
  - "**/*.py"
---

# Not Black — this repo uses Ruff

This rule file used to carry generic Black-formatter best practices, ported from a vendored
rules pack. **MythosMUD's actual Python formatter is Ruff**, run via `make format`
(`scripts/format.py`), not Black. Following Black-specific advice here (installing Black,
`black --check` in CI, `# fmt: off`/`# fmt: on` directives) would be actively misleading —
Ruff has its own formatting conventions and its own directives (`# fmt: skip`/`# fmt: off` are
Ruff-compatible too, but don't assume Black tooling is present).

If you need Python formatting guidance, run `make format` and trust its output, the same way
this repo's own guidance recommends trusting `black`'s output in the vendored version of this
file — just substitute Ruff for Black throughout.
