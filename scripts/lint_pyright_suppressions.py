#!/usr/bin/env python3
"""Pre-commit: enforce the ``# pyright: ignore`` suppression standard under ``server/``.

Two rules, deliberately scoped differently (see #784):

1. **Every** ``# pyright: ignore`` must name the rules it suppresses -- ``# pyright: ignore[rule]``.
   A bare ignore silences every diagnostic on the line, which is the laundering hole this project
   closed when it set ``enableTypeIgnoreComments = false``.

2. Suppressions naming ``reportAny`` or ``reportExplicitAny`` must additionally carry a
   justification block: a ``# Reason: <CATEGORY> - <cause>`` line and an
   ``# Appropriate because: <argument>`` line of at least MIN_JUSTIFICATION_CHARS characters.

   The second rule is scoped to the ``Any`` family on purpose. The category vocabulary below
   classifies *why a value is untyped*; it says nothing useful about ``reportPrivateUsage`` on a
   test reaching into a private helper, or ``reportUnannotatedClassAttribute`` on SQLAlchemy's
   ``__tablename__``. Forcing those through an ``Any``-shaped taxonomy would produce mislabelled
   suppressions and make the category field meaningless where it actually matters.

``Reason:`` states the *cause* of the ``Any``. ``Appropriate because:`` must argue that ``Any`` is
the correct engineering decision rather than unfinished work. If the honest answer is "we have not
got to it yet", no sentence fits -- delete the suppression and let the finding land in
``.basedpyright/baseline.json`` as honest debt instead.

Usage::

    python scripts/lint_pyright_suppressions.py [FILE ...]   # defaults to walking server/
    python scripts/lint_pyright_suppressions.py --report     # inventory grouped by rule/category
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

# Suppressions naming one of these rules must carry a full justification block.
ANY_FAMILY_RULES = frozenset({"reportAny", "reportExplicitAny"})

# Fixed category vocabulary. Entries ending in ":" take a free-form suffix (a library or a
# mypy error code), e.g. ``THIRD_PARTY_UNTYPED:nats`` or ``CHECKER_CONFLICT:redundant-cast``.
BARE_CATEGORIES = frozenset({"TEST_MOCK", "SERIALIZATION_BOUNDARY", "DYNAMIC_DISPATCH"})
PREFIX_CATEGORIES = frozenset({"THIRD_PARTY_UNTYPED", "CHECKER_CONFLICT"})

MIN_JUSTIFICATION_CHARS = 40

# How far from the suppression line to look for its justification block. The block may sit in the
# contiguous comment lines immediately above the suppression, or in the comment lines just below
# it -- above is required for suppressions on a multi-line expression, where "below" lands inside
# the parentheses.
JUSTIFICATION_WINDOW = 12

SKIP_DIR_PARTS = frozenset({"graphify-out", ".venv", "__pycache__", "node_modules", "graphify"})

IGNORE_RE = re.compile(r"#\s*pyright:\s*ignore(?:\[([^\]]*)\])?")
REASON_RE = re.compile(r"#\s*Reason:\s*(?P<body>.+)", re.IGNORECASE)
APPROPRIATE_RE = re.compile(r"#\s*Appropriate because:\s*(?P<body>.+)", re.IGNORECASE)
CATEGORY_RE = re.compile(r"^(?P<name>[A-Z_]+)(?::(?P<suffix>[^\s]+))?")


@dataclass(frozen=True)
class Suppression:
    """One ``# pyright: ignore`` occurrence."""

    path: Path
    lineno: int
    rules: tuple[str, ...]
    category: str | None
    justification: str


@dataclass(frozen=True)
class Failure:
    """A suppression that violates the standard."""

    path: Path
    lineno: int
    problem: str


def _should_skip(path: Path) -> bool:
    return bool(SKIP_DIR_PARTS.intersection(path.parts))


def _iter_target_files(args: list[str]) -> list[Path]:
    if args:
        return [p for p in (Path(a) for a in args) if p.suffix == ".py" and p.is_file() and not _should_skip(p)]
    root = Path("server")
    if not root.is_dir():
        return []
    return sorted(p for p in root.rglob("*.py") if not _should_skip(p))


def _comment_text(line: str) -> str | None:
    """Return the comment portion of a comment-only line, or None if the line has code."""
    stripped = line.strip()
    if stripped.startswith("#"):
        return stripped
    return None


def _collect_context(lines: list[str], index: int) -> str:
    """Gather the comment lines that may hold the justification for the suppression at ``index``."""
    above: list[str] = []
    cursor = index - 1
    while cursor >= 0 and len(above) < JUSTIFICATION_WINDOW:
        comment = _comment_text(lines[cursor])
        if comment is None:
            break
        above.append(comment)
        cursor -= 1

    below: list[str] = []
    cursor = index + 1
    while cursor < len(lines) and len(below) < JUSTIFICATION_WINDOW:
        comment = _comment_text(lines[cursor])
        if comment is None:
            break
        below.append(comment)
        cursor += 1

    # The suppression's own line can carry `# Reason:` inline after the ignore.
    return "\n".join([lines[index], *reversed(above), *below])


def _join_continuation(context: str, first_match_end: int) -> str:
    """Text of a field, including any following ``#``-prefixed continuation lines."""
    remainder = context[first_match_end:]
    out: list[str] = []
    for raw in remainder.splitlines():
        stripped = raw.strip()
        if not stripped.startswith("#"):
            break
        body = stripped.lstrip("#").strip()
        if REASON_RE.match(stripped) or APPROPRIATE_RE.match(stripped):
            break
        out.append(body)
    return " ".join(out)


def _extract_field(context: str, pattern: re.Pattern[str]) -> str:
    match = pattern.search(context)
    if match is None:
        return ""
    head = match.group("body").strip()
    tail = _join_continuation(context, match.end())
    return f"{head} {tail}".strip()


def _validate_category(raw_reason: str) -> tuple[str | None, str | None]:
    """Return ``(category, error)`` for the ``Reason:`` field's leading category token."""
    match = CATEGORY_RE.match(raw_reason.strip())
    if match is None:
        return None, "`# Reason:` must start with a CATEGORY token"
    name = match.group("name")
    suffix = match.group("suffix")
    if name in BARE_CATEGORIES:
        return name, None
    if name in PREFIX_CATEGORIES:
        if not suffix:
            return None, f"category `{name}` requires a `:<detail>` suffix (e.g. `{name}:nats`)"
        return f"{name}:{suffix}", None
    allowed = ", ".join(sorted(BARE_CATEGORIES | {f"{p}:<detail>" for p in PREFIX_CATEGORIES}))
    return None, f"unknown category `{name}`; allowed: {allowed}"


def _parse_rules(ignore_match: re.Match[str], path: Path, lineno: int) -> tuple[str, ...] | Failure:
    """The rules named in brackets, or the Failure explaining why none could be read."""
    raw_rules = ignore_match.group(1)
    if raw_rules is None:
        return Failure(path, lineno, "bare `# pyright: ignore` - name the rule, e.g. `# pyright: ignore[reportAny]`")
    rules = tuple(r.strip() for r in raw_rules.split(",") if r.strip())
    if not rules:
        return Failure(path, lineno, "`# pyright: ignore[]` names no rule")
    return rules


def _justification_failures(
    path: Path,
    lineno: int,
    reason_body: str,
    category_error: str | None,
    appropriate: str,
) -> list[Failure]:
    """Check the two mandatory fields. Only reached for reportAny / reportExplicitAny."""
    failures: list[Failure] = []

    if not reason_body:
        failures.append(Failure(path, lineno, "missing `# Reason: <CATEGORY> - <cause>` line"))
    elif category_error is not None:
        failures.append(Failure(path, lineno, category_error))

    if not appropriate:
        failures.append(Failure(path, lineno, "missing `# Appropriate because: <argument>` line"))
    elif len(appropriate) < MIN_JUSTIFICATION_CHARS:
        failures.append(
            Failure(
                path,
                lineno,
                f"`# Appropriate because:` is {len(appropriate)} chars; "
                f"at least {MIN_JUSTIFICATION_CHARS} required. State why `Any` is correct here, "
                "not merely why it exists.",
            )
        )

    return failures


def scan_file(path: Path) -> tuple[list[Suppression], list[Failure]]:
    """Parse one file's suppressions and report any that violate the standard."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError):
        return [], []

    suppressions: list[Suppression] = []
    failures: list[Failure] = []

    for index, line in enumerate(lines):
        ignore_match = IGNORE_RE.search(line)
        if ignore_match is None:
            continue

        lineno = index + 1
        parsed = _parse_rules(ignore_match, path, lineno)
        if isinstance(parsed, Failure):
            failures.append(parsed)
            continue

        context = _collect_context(lines, index)
        reason_body = _extract_field(context, REASON_RE)
        category, category_error = _validate_category(reason_body) if reason_body else (None, None)
        appropriate = _extract_field(context, APPROPRIATE_RE)

        suppressions.append(Suppression(path, lineno, parsed, category, appropriate))

        if ANY_FAMILY_RULES.intersection(parsed):
            failures.extend(_justification_failures(path, lineno, reason_body, category_error, appropriate))

    return suppressions, failures


def _print_report(suppressions: list[Suppression]) -> None:
    """Inventory grouped by rule and category.

    A category that repeats across many files usually means one stub, wrapper, or Protocol would
    retire all of them at once -- which is the point of collecting the field.
    """
    print(f"pyright suppressions under server/: {len(suppressions)}")
    print()
    by_rule: Counter[str] = Counter(rule for s in suppressions for rule in s.rules)
    print("--- by rule ---")
    for rule, count in by_rule.most_common():
        print(f"{count:5}  {rule}")

    any_family = [s for s in suppressions if ANY_FAMILY_RULES.intersection(s.rules)]
    print()
    print(f"--- Any-family suppressions (justification required): {len(any_family)} ---")
    by_category: Counter[str] = Counter(s.category or "<none>" for s in any_family)
    for category, count in by_category.most_common():
        print(f"{count:5}  {category}")
    print()
    for supp in sorted(any_family, key=lambda s: (str(s.path), s.lineno)):
        print(f"  {supp.path}:{supp.lineno}  [{', '.join(supp.rules)}]  {supp.category or '<no category>'}")


def main() -> None:
    args = [a for a in sys.argv[1:] if a != "--report"]
    report_mode = "--report" in sys.argv[1:]

    all_suppressions: list[Suppression] = []
    all_failures: list[Failure] = []
    for path in _iter_target_files(args):
        suppressions, failures = scan_file(path)
        all_suppressions.extend(suppressions)
        all_failures.extend(failures)

    if report_mode:
        _print_report(all_suppressions)
        sys.exit(0)

    if not all_failures:
        sys.exit(0)

    print("PYRIGHT SUPPRESSION STANDARD VIOLATIONS:", file=sys.stderr)
    print("", file=sys.stderr)
    for failure in all_failures:
        print(f"  {failure.path}:{failure.lineno}: {failure.problem}", file=sys.stderr)
    print("", file=sys.stderr)
    print("Required form for reportAny / reportExplicitAny (see AGENTS.md, #784):", file=sys.stderr)
    print("", file=sys.stderr)
    print("    # Reason: THIRD_PARTY_UNTYPED:nats - Msg.data is annotated bytes | Any upstream.", file=sys.stderr)
    print("    # Appropriate because: the payload is validated by _decode_envelope() on the", file=sys.stderr)
    print("    # next line, which returns a typed Envelope; annotating a shape here would", file=sys.stderr)
    print("    # assert a structure we have not yet checked.", file=sys.stderr)
    print("    msg = await sub.next_msg()  # pyright: ignore[reportAny]", file=sys.stderr)
    print("", file=sys.stderr)
    print("If no honest `Appropriate because:` sentence fits, delete the suppression and let the", file=sys.stderr)
    print("finding land in .basedpyright/baseline.json as debt instead of claiming permanence.", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
