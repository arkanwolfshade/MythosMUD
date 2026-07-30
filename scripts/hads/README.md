# HADS tooling (MythosMUD)

**Version 1.0.0** · MythosMUD · 2026-07-30

Vendored structural validator for the Human-AI Document Standard (HADS).

## Source pin

- Upstream: https://github.com/catcam/hads
- File: `validate.py` (repo root)
- Commit: `dcfe582df90c8a276690fd05ebe4819d4ba12c36`
- Local path: `scripts/hads/validate.py`
- Local additions: `--manifest` batch mode; ASCII-only output (repo Python style)

## Usage

```powershell
# Single file
python scripts/hads/validate.py docs/TESTING.md

# All converted living docs listed in the manifest
python scripts/hads/validate.py --manifest docs/hads.manifest
```

Manifest format: one repo-relative path per line. Lines starting with `#` are ignored
(use for pending candidates during conversion ramp).

## Policy

New or materially updated living developer docs must be HADS-shaped and listed in
`docs/hads.manifest`. See `CONTRIBUTING.md`. Archive under `docs/archive/` is
historical and is not HADS-validated.
