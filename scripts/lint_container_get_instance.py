"""
Guard against new `ApplicationContainer.get_instance()` service-location debt in container-
constructed classes. See issue #636 and `docs/CONTAINER_INJECTION_AUDIT.md`.

ADR-002 v1.1.0 §3: injection is required for any type a `server/container/bundles/*.py` bundle
constructs directly; service location via `ApplicationContainer.get_instance()` is sanctioned for
everything else -- domain entities, mixins, free functions, and services constructed by another
service rather than a bundle, none of which have a constructor a bundle could inject through.

This guard cannot tell, from text alone, whether a given call site's enclosing class is
bundle-constructed or sanctioned -- that classification is #636's own audit work, recorded in
CONTAINER_GET_INSTANCE_ALLOWLIST below with the reason for each entry. Structurally, this differs
from lint_raw_sql_in_python.py's ADR-015 guard: raw SQL outside db/procedures/ has no legitimate
form at all, so an empty allowlist is the healthy end state. Nearly every entry here is a
*permanent, sanctioned* site, not debt trending to zero -- the allowlist is a confirmed baseline
census, and this guard's job is catching *drift*: a brand-new get_instance() call added to an
already-listed file (its count goes up), or a new file introducing the pattern (an unlisted file
with a hit). A genuinely bundle-constructed class calling get_instance() from a new site is exactly
what should fail here, whether or not that file is already listed for other, sanctioned reasons.

No target-date/overdue tracking (unlike the raw-SQL guard): there's no "grandfathered until fixed"
concept for a call site that is correctly and permanently sanctioned. Each entry instead carries a
`reason` explaining the classification, cross-referenced against
docs/CONTAINER_INJECTION_AUDIT.md's table.

Detection is AST/token-based, not regex: matches the literal token sequence
`ApplicationContainer . get_instance ( )` only in CODE tokens, skipping STRING and COMMENT tokens
entirely -- several files now carry prose mentioning "ApplicationContainer.get_instance()" in
docstrings (explaining what they migrated *away* from), which must never count as a hit.

Usage: python scripts/lint_container_get_instance.py
Exit: 0 if every file's count matches its allowlist entry (or has no entry and zero hits), 1
otherwise.
"""

from __future__ import annotations

import sys
import tokenize
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Directories under server/ excluded entirely -- never scanned, never allowlisted. Same set as
# lint_raw_sql_in_python.py, for the same reasons (tests, migration tooling, admin scripts, and a
# vendored tree are not live request-serving application code).
EXCLUDED_DIR_PARTS = {
    "tests",
    "alembic",
    "scripts",
    "graphify-out",
}


@dataclass(frozen=True)
class AllowlistEntry:
    """One file's confirmed get_instance() call-site count, and why it's there."""

    file: str
    count: int
    reason: str


# Baseline as of #636 (2026-08-25), the audit in docs/CONTAINER_INJECTION_AUDIT.md. All six
# container-constructed classes identified as debt (UserManager, EventPublisher,
# PlayerDeathService, HealthService, NPCStartupService, MemoryLeakMetricsCollector) were migrated
# to constructor injection in #679/#636 and carry zero entries here. Everything below is either
# sanctioned service location (ADR-002 v1.1.0 §3) or dead code tracked under #630.
CONTAINER_GET_INSTANCE_ALLOWLIST: tuple[AllowlistEntry, ...] = (
    AllowlistEntry("server/container/main.py", 1, "get_container() is the DI accessor itself"),
    AllowlistEntry("server/app/lifespan_startup.py", 1, "startup-sequence helper function, not bundle-constructed"),
    AllowlistEntry(
        "server/monitoring/memory_leak_metrics.py",
        2,
        (
            "fallback only, reached when event_bus/nats_service aren't injected -- used by the "
            + "standalone get_monitoring_dashboard() singleton; MonitoringBundle's own instance is injected"
        ),
    ),
    AllowlistEntry("server/npc/npc_base.py", 1, "domain entity (ADR-002 v1.1.0 3's own example)"),
    AllowlistEntry(
        "server/npc/threading.py", 1, "lazy default inside NPCLifecycleManager.__init__, not bundle-constructed"
    ),
    AllowlistEntry("server/npc/spawning_request_execution.py", 1, "free function"),
    AllowlistEntry(
        "server/npc/passive_mob_npc.py",
        1,
        "entity-factory product (spawning_instance_factory.py), not bundle-constructed",
    ),
    AllowlistEntry("server/services/combat_death_handler.py", 2, "constructed by CombatService, not a bundle"),
    AllowlistEntry("server/services/combat_cleanup_handler.py", 1, "constructed by CombatService, not a bundle"),
    AllowlistEntry("server/services/combat_persistence_handler.py", 1, "constructed by CombatService, not a bundle"),
    AllowlistEntry("server/services/combat_messaging/base.py", 1, "mixin, never instantiated directly"),
    AllowlistEntry(
        "server/services/combat_hp_sync.py", 1, "dead code (#630): CombatDPSync has zero production callers"
    ),
    AllowlistEntry(
        "server/services/npc_combat_handlers.py", 1, "constructed by NPCCombatIntegrationService, not a bundle"
    ),
    AllowlistEntry(
        "server/services/npc_combat_rewards.py", 1, "constructed by NPCCombatIntegrationService, not a bundle"
    ),
    AllowlistEntry("server/game/magic/magic_healing_events.py", 1, "mixin, never instantiated directly"),
    AllowlistEntry("server/realtime/connection_manager_utils.py", 1, "free function"),
)

_ALLOWLIST_BY_FILE: dict[str, AllowlistEntry] = {entry.file: entry for entry in CONTAINER_GET_INSTANCE_ALLOWLIST}

_SKIP_TOKEN_TYPES = frozenset(
    {
        tokenize.COMMENT,
        tokenize.STRING,
        tokenize.NL,
        tokenize.NEWLINE,
        tokenize.INDENT,
        tokenize.DEDENT,
        tokenize.ENCODING,
        tokenize.ENDMARKER,
    }
)


def _collect_python_files() -> list[Path]:
    out: list[Path] = []
    for path in (PROJECT_ROOT / "server").rglob("*.py"):
        rel_parts = set(path.relative_to(PROJECT_ROOT).parts)
        if rel_parts & EXCLUDED_DIR_PARTS:
            continue
        out.append(path)
    return sorted(out)


_GET_INSTANCE_TOKEN_PATTERN: tuple[tuple[int | None, str], ...] = (
    (tokenize.NAME, "ApplicationContainer"),
    (None, "."),
    (tokenize.NAME, "get_instance"),
    (None, "("),
    (None, ")"),
)


def _code_tokens(content: str) -> list[tokenize.TokenInfo]:
    """Tokenize Python source, omitting comments, strings, and whitespace tokens."""
    try:
        return [
            tok
            for tok in tokenize.generate_tokens(iter(content.splitlines(keepends=True)).__next__)
            if tok.type not in _SKIP_TOKEN_TYPES
        ]
    except (tokenize.TokenError, IndentationError, SyntaxError):
        # Unparsable file is not this guard's problem to diagnose; other tooling (ruff, basedpyright)
        # already fails the build on a syntax error.
        return []


def _is_application_container_get_instance(tokens: list[tokenize.TokenInfo], index: int) -> bool:
    """True when tokens[index:index+5] is ApplicationContainer.get_instance()."""
    if index + len(_GET_INSTANCE_TOKEN_PATTERN) > len(tokens):
        return False
    for tok, (expected_type, expected_string) in zip(
        tokens[index : index + len(_GET_INSTANCE_TOKEN_PATTERN)],
        _GET_INSTANCE_TOKEN_PATTERN,
        strict=True,
    ):
        if expected_type is not None and tok.type != expected_type:
            return False
        if tok.string != expected_string:
            return False
    return True


def _find_get_instance_lines(content: str) -> list[int]:
    """Return 1-based line numbers of real `ApplicationContainer.get_instance()` calls.

    Token-based rather than regex: the pattern is an exact, unambiguous identifier chain (unlike
    the raw-SQL guard's fuzzy SQL-keyword matching), so a tokenizer that skips STRING/COMMENT
    tokens is the precise tool -- it can't be fooled by a docstring or comment that merely mentions
    the pattern in prose, which several migrated files now do.
    """
    tokens = _code_tokens(content)
    hits: set[int] = set()
    for i in range(len(tokens) - len(_GET_INSTANCE_TOKEN_PATTERN) + 1):
        if _is_application_container_get_instance(tokens, i):
            hits.add(tokens[i].start[0])
    return sorted(hits)


def _collect_get_instance_counts() -> tuple[dict[str, int], list[str]]:
    """Walk server/*.py and count get_instance() hits per file; collect read errors."""
    counts_by_file: dict[str, int] = {}
    read_errors: list[str] = []
    for path in _collect_python_files():
        rel = str(path.relative_to(PROJECT_ROOT)).replace("\\", "/")
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            read_errors.append(f"{rel}: read error: {e}")
            continue
        line_nums = _find_get_instance_lines(content)
        if line_nums:
            counts_by_file[rel] = len(line_nums)
    return counts_by_file, read_errors


def _allowlist_count_violations(counts_by_file: dict[str, int]) -> tuple[list[str], int]:
    """Compare per-file hit counts to allowlist; return violations and confirmed entries."""
    violations: list[str] = []
    allowlisted_confirmed = 0
    for rel, found_count in counts_by_file.items():
        entry = _ALLOWLIST_BY_FILE.get(rel)
        expected_count = entry.count if entry is not None else 0
        if found_count > expected_count:
            violations.append(
                f"{rel}: {found_count} ApplicationContainer.get_instance() call(s) found, "
                + f"{expected_count} allowlisted -- inject the dependency at its bundle's "
                + "construction site instead (ADR-002 v1.1.0 3), or add an allowlist entry with a "
                + "reason if this site is genuinely sanctioned service location"
            )
        elif entry is not None and found_count < expected_count:
            violations.append(
                f"{rel}: {found_count} call(s) found, but CONTAINER_GET_INSTANCE_ALLOWLIST expects "
                + f"{expected_count} -- a site was migrated or removed; lower the allowlist count to {found_count}"
            )
        elif entry is not None:
            allowlisted_confirmed += 1
    return violations, allowlisted_confirmed


def _stale_allowlist_violations(counts_by_file: dict[str, int]) -> list[str]:
    """Flag allowlist entries whose file no longer contains any get_instance() call."""
    violations: list[str] = []
    for entry in CONTAINER_GET_INSTANCE_ALLOWLIST:
        if entry.file not in counts_by_file:
            violations.append(
                f"{entry.file}: CONTAINER_GET_INSTANCE_ALLOWLIST expects {entry.count} call(s), "
                + "0 found -- remove this allowlist entry"
            )
    return violations


def scan() -> tuple[list[str], int]:
    """Scan server/ for ApplicationContainer.get_instance() calls. Returns (new_violations,
    allowlisted_confirmed) -- allowlisted_confirmed is the number of entries whose file's actual
    count matches its expected count."""
    counts_by_file, read_errors = _collect_get_instance_counts()
    count_violations, allowlisted_confirmed = _allowlist_count_violations(counts_by_file)
    stale_violations = _stale_allowlist_violations(counts_by_file)
    return read_errors + count_violations + stale_violations, allowlisted_confirmed


def main() -> int:
    """Run the container-injection guard and return 1 if any file's get_instance() count doesn't
    match its allowlist entry (or has an unlisted site)."""
    new_violations, allowlisted_count = scan()

    for msg in new_violations:
        print(msg)

    remaining = len(CONTAINER_GET_INSTANCE_ALLOWLIST)
    print(f"\nContainer get_instance() allowlist: {allowlisted_count}/{remaining} file(s) confirmed accurate.")

    if new_violations:
        print(
            f"\n{len(new_violations)} container get_instance() allowlist mismatch(es) found. "
            + "See docs/CONTAINER_INJECTION_AUDIT.md and ADR-002."
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
