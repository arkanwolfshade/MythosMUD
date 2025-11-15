from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from server.schemas.calendar import HolidayCollection

REPO_ROOT = Path(__file__).resolve().parents[4]
DATA_DIR = REPO_ROOT / "data" / "calendar"
DOC_PATH = REPO_ROOT / "docs" / "MYTHOS_HOLIDAY_CANDIDATES.md"


def test_holiday_file_matches_schema() -> None:
    collection = HolidayCollection.load_file(DATA_DIR / "holidays.json")
    collection.ensure_unique_ids()
    assert len(collection.holidays) >= 30


def test_document_ids_are_represented() -> None:
    collection = HolidayCollection.load_file(DATA_DIR / "holidays.json")
    doc_ids = _parse_doc_ids(DOC_PATH)
    missing = doc_ids - set(collection.id_map)
    assert not missing, f"Holiday JSON missing entries: {sorted(missing)}"


def test_cli_validation() -> None:
    cmd = [
        sys.executable,
        str(REPO_ROOT / "scripts" / "validate_calendar.py"),
        "--holidays",
        str(DATA_DIR / "holidays.json"),
        "--schedules-dir",
        str(DATA_DIR / "schedules"),
        "--doc",
        str(DOC_PATH),
        "--quiet",
    ]
    result = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, env=os.environ.copy())
    assert result.returncode == 0, result.stderr


def _parse_doc_ids(doc_path: Path) -> set[str]:
    from server.schemas.calendar import extract_observance_ids

    return extract_observance_ids(doc_path.read_text(encoding="utf-8").splitlines())
