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


def _get_calendar_paths(args: argparse.Namespace) -> tuple[Path, Path]:
    """Get holidays and schedules paths."""
    normalized_env = normalize_environment(args.environment)
    default_holidays, default_schedules = get_calendar_paths_for_environment(normalized_env)
    holidays_path = args.holidays or default_holidays
    schedules_dir = args.schedules_dir or default_schedules
    return holidays_path, schedules_dir


def _load_and_validate_holidays(holidays_path: Path, errors: list[str]) -> HolidayCollection | None:
    """Load and validate holidays."""
    try:
        holidays = HolidayCollection.load_file(holidays_path)
        holidays.ensure_unique_ids()
        return holidays
    except (FileNotFoundError, ValidationError, ValueError) as exc:
        errors.append(f"Holidays validation failed: {exc}")
        return None


def _check_holiday_coverage(holidays: HolidayCollection, doc_path: Path, errors: list[str]) -> None:
    """Check if holidays cover documentation references."""
    try:
        doc_ids = load_document_ids(doc_path)
    except FileNotFoundError as exc:
        errors.append(str(exc))
    else:
        missing = doc_ids - set(holidays.id_map)
        if missing:
            errors.append(f"Holiday JSON missing entries referenced in documentation: {', '.join(sorted(missing))}")


def _validate_schedule_files(schedules_dir: Path, errors: list[str]) -> list[tuple[Path, HolidayCollection]] | None:
    """Load and validate schedule files."""
    try:
        schedule_files = load_schedule_directory(schedules_dir)
    except FileNotFoundError as exc:
        errors.append(str(exc))
        return None

    for path, _collection in schedule_files:
        try:
            _ = _collection  # Trigger validation during load
        except ValidationError as exc:
            errors.append(f"Schedule validation failed for {path}: {exc}")

    return schedule_files


def _print_errors(errors: list[str]) -> None:
    """Print validation errors."""
    for line in errors:
        print(line)


def _print_success_message(holidays: HolidayCollection, schedule_files: list[tuple[Path, HolidayCollection]], quiet: bool) -> None:
    """Print success message if not quiet."""
    if not quiet:
        schedule_count = len(schedule_files)
        print(
            f"Validated {len(holidays.holidays)} holidays and {schedule_count} schedule file{'s' if schedule_count != 1 else ''}."
        )


def run_validation(args: argparse.Namespace) -> int:
    errors: list[str] = []
    holidays_path, schedules_dir = _get_calendar_paths(args)

    holidays = _load_and_validate_holidays(holidays_path, errors)
    if holidays is not None:
        _check_holiday_coverage(holidays, args.doc, errors)

    schedule_files = _validate_schedule_files(schedules_dir, errors)

    if errors:
        _print_errors(errors)
        return 1

    if schedule_files is not None and holidays is not None:
        _print_success_message(holidays, schedule_files, args.quiet)

    return 0


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    return run_validation(args)


if __name__ == "__main__":
    raise SystemExit(main())
