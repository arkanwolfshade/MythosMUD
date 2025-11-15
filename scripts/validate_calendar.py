from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from pydantic import ValidationError

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from server.schemas.calendar import (  # noqa: E402  # pylint: disable=wrong-import-position
    HolidayCollection,
    extract_observance_ids,
    load_schedule_directory,
)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Mythos calendar JSON assets.")
    parser.add_argument(
        "--holidays",
        type=Path,
        default=Path("data/calendar/holidays.json"),
        help="Path to holidays JSON file (default: data/calendar/holidays.json)",
    )
    parser.add_argument(
        "--schedules-dir",
        type=Path,
        default=Path("data/calendar/schedules"),
        help="Directory containing schedule JSON files (default: data/calendar/schedules)",
    )
    parser.add_argument(
        "--doc",
        type=Path,
        default=Path("docs/MYTHOS_HOLIDAY_CANDIDATES.md"),
        help="Markdown document used to cross-check holiday coverage.",
    )
    parser.add_argument("--quiet", action="store_true", help="Suppress success output.")
    return parser.parse_args(argv)


def load_document_ids(doc_path: Path) -> set[str]:
    if not doc_path.exists():
        raise FileNotFoundError(f"Holiday reference document not found: {doc_path}")
    return extract_observance_ids(doc_path.read_text(encoding="utf-8").splitlines())


def run_validation(args: argparse.Namespace) -> int:
    errors: list[str] = []
    try:
        holidays = HolidayCollection.load_file(args.holidays)
        holidays.ensure_unique_ids()
    except (FileNotFoundError, ValidationError, ValueError) as exc:
        errors.append(f"Holidays validation failed: {exc}")
    else:
        try:
            doc_ids = load_document_ids(args.doc)
        except FileNotFoundError as exc:
            errors.append(str(exc))
        else:
            missing = doc_ids - set(holidays.id_map)
            if missing:
                errors.append(f"Holiday JSON missing entries referenced in documentation: {', '.join(sorted(missing))}")

    try:
        schedule_files = load_schedule_directory(args.schedules_dir)
    except FileNotFoundError as exc:
        errors.append(str(exc))
    else:
        for path, _collection in schedule_files:
            try:
                _ = _collection  # Trigger validation during load
            except ValidationError as exc:
                errors.append(f"Schedule validation failed for {path}: {exc}")

    if errors:
        for line in errors:
            print(line)
        return 1

    if not args.quiet:
        schedule_count = len(schedule_files)
        print(
            f"Validated {len(holidays.holidays)} holidays and {schedule_count} schedule file{'s' if schedule_count != 1 else ''}."
        )
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    return run_validation(args)


if __name__ == "__main__":
    raise SystemExit(main())
