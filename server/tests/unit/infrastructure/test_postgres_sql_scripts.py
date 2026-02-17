"""
PostgreSQL-focused tests for verification and maintenance SQL scripts.

Validates that SQL files updated during the PostgreSQL audit remediation
follow style rules and do not reference obsolete schema.
"""

from pathlib import Path

# Project root: server/tests/unit/infrastructure -> unit -> tests -> server -> project root
_PROJECT_ROOT = Path(__file__).resolve().parents[4]
_DB_VERIFICATION = _PROJECT_ROOT / "db" / "verification" / "users_players.sql"
_NPC_CONSTRAINT_SCRIPT = _PROJECT_ROOT / "server" / "scripts" / "add_npc_name_constraint.sql"


class TestVerificationSqlUsersPlayers:
    """Tests for db/verification/users_players.sql alignment with current schema."""

    def test_verification_sql_file_exists(self):
        """Verification SQL file must exist."""
        assert _DB_VERIFICATION.exists(), "db/verification/users_players.sql missing"

    def test_verification_sql_uses_live_tables_only(self):
        """Verification SQL must not reference staging tables or select obsolete columns."""
        content = _DB_VERIFICATION.read_text()
        assert "staging_" not in content, "Must not reference staging_* tables"
        # Must not select sanity_score as a column (comment may mention it for documentation)
        assert " p.sanity_score" not in content and "select sanity_score" not in content.lower()

    def test_verification_sql_uses_explicit_joins(self):
        """Verification SQL must use explicit join syntax for multi-table queries."""
        content = _DB_VERIFICATION.read_text().lower()
        assert "left join" in content or "join" in content
        # Players-without-users query must use explicit join, not "from a, b where"
        assert "players as p" in content and "users as u" in content
        assert "on u.id = p.user_id" in content or "on p.user_id = u.id" in content

    def test_verification_sql_references_users_and_players(self):
        """Verification SQL must reference users and players tables."""
        content = _DB_VERIFICATION.read_text().lower()
        assert "users" in content
        assert "players" in content


class TestNpcNameConstraintScript:
    """Tests for server/scripts/add_npc_name_constraint.sql (PostgreSQL-only)."""

    def test_npc_constraint_script_exists(self):
        """NPC name constraint script must exist."""
        assert _NPC_CONSTRAINT_SCRIPT.exists(), "server/scripts/add_npc_name_constraint.sql missing"

    def test_npc_constraint_script_no_sqlite_pragma(self):
        """Script must not contain SQLite-specific pragma."""
        content = _NPC_CONSTRAINT_SCRIPT.read_text()
        assert "pragma" not in content.lower(), "Must be PostgreSQL-only, no pragma"

    def test_npc_constraint_script_uses_postgresql_constraint(self):
        """Script must use PostgreSQL constraint (CHECK or ALTER TABLE)."""
        content = _NPC_CONSTRAINT_SCRIPT.read_text()
        assert "alter table" in content.lower() or "check" in content.lower()
        assert "npc_definitions" in content
