"""
Guard against unguarded optional-authentication route handlers. See issue #734.

`server.auth.users.get_current_user` is `fastapi_users.current_user(optional=True)` -- it returns
`None` on a missing or invalid token instead of raising 401. That's a legitimate FastAPI pattern
for routes whose behavior varies by login state, but #734's census found 8 route handlers using it
with *no* downstream check at all: `current_user` was referenced only in error-context logging,
so the endpoint was reachable by anyone, authenticated or not. OpenAPI's `security` field cannot
see this -- FastAPI emits the same `OAuth2PasswordBearer` block whether the dependency is optional
or required, so the generated spec looks identical either way. This guard is the enforcing check
`security` can't be.

Recognized guards, in order of how #734's fixes actually look in this codebase: a direct
`current_user is None` / `not current_user` check in the handler body; a call to
`validate_permission` or `validate_admin_permission` (the admin-auth-service pattern used across
`server/api/admin/*` and this issue's own fixes); or delegation to a same-module helper function
whose own body contains one of those markers (the `_require_current_user` / `_validate_admin_room_action`
/ `_run_set_map_origin` shape used in `character_creation.py`, `rooms.py`, `maps.py`).

New unguarded routes fail the build immediately. Existing, already-adjudicated exceptions (routes
where #734 confirmed no auth is intentional, e.g. a public GET) are grandfathered via
OPTIONAL_AUTH_ALLOWLIST below, following the same count-per-file convention as
`lint_raw_sql_in_python.py`: keyed on an expected *count*, not (file, line), so an unrelated edit
above a grandfathered route can't shift its line number and false-positive as a new violation.

Usage: python scripts/lint_optional_auth_no_guard.py
Exit: 0 if every scanned file's unguarded-route count matches its allowlist entry (or has no entry
and zero unguarded routes), 1 otherwise.
"""

from __future__ import annotations

import ast
import sys
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

SCAN_ROOTS = ("server/api", "server/auth/endpoints.py", "server/command_handler_unified.py")
EXCLUDED_DIR_PARTS = {"tests", "__pycache__"}

OPTIONAL_DEP_NAMES = {"get_current_user"}
REQUIRED_DEP_NAMES = {"get_current_active_user", "get_current_superuser", "get_current_verified_user"}
GUARD_CALL_NAMES = {"validate_permission", "validate_admin_permission"}

ROUTE_DECORATOR_METHODS = {"get", "post", "put", "delete", "patch", "websocket"}


@dataclass(frozen=True)
class AllowlistEntry:
    """One file's grandfathered unguarded-optional-auth route count, adjudicated by #734."""

    file: str
    count: int
    note: str


# #734's census adjudicated every optional-auth route in the corpus. These two are the only
# survivors: current_user is genuinely consumed downstream (not merely logged), just too many
# calls deep for this scanner's two-hop delegation search to follow.
OPTIONAL_AUTH_ALLOWLIST: tuple[AllowlistEntry, ...] = (
    AllowlistEntry(
        "server/api/maps.py",
        1,
        "get_ascii_map: current_user threaded through _MapEndpointDeps to filter to explored "
        "rooms for non-admins vs. all rooms for admins -- graduated by design, not unguarded.",
    ),
    AllowlistEntry(
        "server/api/players.py",
        1,
        "get_available_classes: returns only static class-prerequisite/description reference "
        "data, no per-player or per-account information -- harmless regardless of auth state.",
    ),
)

_ALLOWLIST_BY_FILE: dict[str, AllowlistEntry] = {entry.file: entry for entry in OPTIONAL_AUTH_ALLOWLIST}


def _collect_files() -> list[Path]:
    out: list[Path] = []
    for rel in SCAN_ROOTS:
        p = PROJECT_ROOT / rel
        candidates = p.rglob("*.py") if p.is_dir() else [p]
        for path in candidates:
            if not path.exists():
                continue
            if set(path.relative_to(PROJECT_ROOT).parts) & EXCLUDED_DIR_PARTS:
                continue
            out.append(path)
    return sorted(set(out))


def _dep_names_in_default(node: ast.expr) -> set[str]:
    """Return every bare name referenced inside a `Depends(...)` default expression.

    `Depends(get_current_user)` passes the dependency function *by reference* -- it's an
    `ast.Name`, not an `ast.Call` -- so this must collect all names, not just called ones.
    """
    return {sub.id for sub in ast.walk(node) if isinstance(sub, ast.Name)}


def _auth_posture(fn: ast.AsyncFunctionDef | ast.FunctionDef) -> str:
    """Return 'required', 'optional', or 'anonymous' from the handler's Depends() defaults."""
    all_defaults = list(fn.args.defaults) + [d for d in fn.args.kw_defaults if d is not None]
    seen: set[str] = set()
    for default in all_defaults:
        seen |= _dep_names_in_default(default)
    if seen & REQUIRED_DEP_NAMES:
        return "required"
    if seen & OPTIONAL_DEP_NAMES:
        return "optional"
    return "anonymous"


def _is_current_user_name(node: ast.expr) -> bool:
    """Match `current_user`, `_current_user`, or any other `*current_user` binding name --
    handlers vary the leading underscore depending on whether other code in the function uses
    the parameter directly."""
    return isinstance(node, ast.Name) and node.id.endswith("current_user")


def _guard_call_name(call: ast.Call) -> str | None:
    """Return the called function's own name, whether invoked as `guard(...)` (a bare import) or
    `x.guard(...)` (a method/attribute call, e.g. `get_admin_auth_service().validate_permission`)."""
    if isinstance(call.func, ast.Name):
        return call.func.id
    if isinstance(call.func, ast.Attribute):
        return call.func.attr
    return None


def _body_has_direct_guard(body: list[ast.stmt]) -> bool:
    for node in ast.walk(ast.Module(body=body, type_ignores=[])):
        if isinstance(node, ast.Call) and _guard_call_name(node) in GUARD_CALL_NAMES:
            return True
        if isinstance(node, ast.Compare) and any(isinstance(op, (ast.Is, ast.IsNot)) for op in node.ops):
            # current_user is None / current_user is not None
            operands = [node.left, *node.comparators]
            if any(_is_current_user_name(o) for o in operands):
                return True
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            if _is_current_user_name(node.operand):
                return True
    return False


def _called_helper_names(body: list[ast.stmt]) -> set[str]:
    names: set[str] = set()
    for node in ast.walk(ast.Module(body=body, type_ignores=[])):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            names.add(node.func.id)
    return names


def _is_guarded(fn: ast.AsyncFunctionDef | ast.FunctionDef, module_funcs: dict[str, ast.AST]) -> bool:
    """True if the handler guards directly, or delegates (through any depth of same-module
    helper calls) to something that does -- e.g. rooms.py's update_room_position calls
    `_validate_room_position_update`, which itself only calls `_validate_admin_room_action`,
    which is where `validate_permission` actually lives. Two hops, not one."""
    visited: set[str] = set()
    frontier = [fn]
    while frontier:
        current = frontier.pop()
        if _body_has_direct_guard(current.body):
            return True
        for name in _called_helper_names(current.body):
            if name in visited:
                continue
            visited.add(name)
            helper = module_funcs.get(name)
            if isinstance(helper, (ast.FunctionDef, ast.AsyncFunctionDef)):
                frontier.append(helper)
    return False


def _route_decorators(fn: ast.AsyncFunctionDef | ast.FunctionDef) -> bool:
    for dec in fn.decorator_list:
        if (
            isinstance(dec, ast.Call)
            and isinstance(dec.func, ast.Attribute)
            and dec.func.attr in ROUTE_DECORATOR_METHODS
        ):
            return True
    return False


def _find_unguarded(tree: ast.Module) -> int:
    module_funcs: dict[str, ast.AST] = {
        node.name: node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    count = 0
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if not _route_decorators(node):
            continue
        if _auth_posture(node) != "optional":
            continue
        if not _is_guarded(node, module_funcs):
            count += 1
    return count


def scan() -> tuple[list[str], int]:
    """Scan the corpus. Returns (violations, allowlisted_confirmed_count)."""
    violations: list[str] = []
    allowlisted_confirmed = 0

    for path in _collect_files():
        rel = str(path.relative_to(PROJECT_ROOT)).replace("\\", "/")
        try:
            tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"), filename=rel)
        except SyntaxError as e:
            violations.append(f"{rel}: parse error: {e}")
            continue

        found = _find_unguarded(tree)
        entry = _ALLOWLIST_BY_FILE.get(rel)
        expected = entry.count if entry is not None else 0

        if found > expected:
            violations.append(
                f"{rel}: {found} unguarded optional-auth route(s) found, {expected} allowlisted -- "
                f"add a current_user is None check, call validate_permission/validate_admin_permission, "
                f"or raise OPTIONAL_AUTH_ALLOWLIST's count with a note if genuinely intentional"
            )
        elif entry is not None and found < expected:
            violations.append(
                f"{rel}: {found} unguarded route(s) found, but OPTIONAL_AUTH_ALLOWLIST expects "
                f"{expected} -- a route was fixed; lower the allowlist count to {found}"
            )
        elif entry is not None:
            allowlisted_confirmed += 1

    return violations, allowlisted_confirmed


def main() -> int:
    """Run the guard and return 1 if any file's unguarded-route count doesn't match its allowlist."""
    violations, allowlisted_count = scan()

    for msg in violations:
        print(msg)

    remaining = len(OPTIONAL_AUTH_ALLOWLIST)
    print(f"\nOptional-auth allowlist: {allowlisted_count}/{remaining} grandfathered file(s) confirmed accurate.")

    if violations:
        print(f"\n{len(violations)} unguarded optional-auth route(s) found. See issue #734.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
