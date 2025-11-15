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
from server.utils.project_paths import (  # noqa: E402  # pylint: disable=wrong-import-position
    get_calendar_paths_for_environment,
    get_project_root,
    normalize_environment,
)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Mythos calendar JSON assets.")
    parser.add_argument(
        "--holidays",
        type=Path,
        default=None,
        help="Path to holidays JSON file (default: derived from --environment)",
    )
    parser.add_argument(
        "--schedules-dir",
        type=Path,
        default=None,
        help="Directory containing schedule JSON files (default: derived from --environment)",
    )
    parser.add_argument(
        "--doc",
        type=Path,
        default=get_project_root() / "docs" / "MYTHOS_HOLIDAY_CANDIDATES.md",
        help="Markdown document used to cross-check holiday coverage.",
    )
    parser.add_argument(
        "--environment",
        choices=["local", "unit_test", "e2e_test", "production"],
        default="local",
        help="Environment whose data directory should be validated (default: local).",
    )
    parser.add_argument("--quiet", action="store_true", help="Suppress success output.")
    return parser.parse_args(argv)


def load_document_ids(doc_path: Path) -> set[str]:
    if not doc_path.exists():
        raise FileNotFoundError(f"Holiday reference document not found: {doc_path}")
    return extract_observance_ids(doc_path.read_text(encoding="utf-8").splitlines())


def run_validation(args: argparse.Namespace) -> int:
    errors: list[str] = []
    normalized_env = normalize_environment(args.environment)
    default_holidays, default_schedules = get_calendar_paths_for_environment(normalized_env)
    holidays_path = args.holidays or default_holidays
    schedules_dir = args.schedules_dir or default_schedules

    try:
        holidays = HolidayCollection.load_file(holidays_path)
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
        schedule_files = load_schedule_directory(schedules_dir)
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
