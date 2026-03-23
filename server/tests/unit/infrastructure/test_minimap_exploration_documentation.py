"""
Guardrails for minimap / exploration documentation.

Ensures the investigation write-up continues to state the root cause (UUID vs stable_id
confusion) and user-visible impact (non-admin minimap behavior).
"""

from pathlib import Path

# Project root: server/tests/unit/infrastructure -> unit -> tests -> server -> project root
_PROJECT_ROOT = Path(__file__).resolve().parents[4]
_MINIMAP_INVESTIGATION = (
    _PROJECT_ROOT / "investigations" / "sessions" / "2026-01-04_session-minimap-explored-rooms-bug.md"
)


class TestMinimapExplorationInvestigationDoc:
    """Content checks for the minimap explored-rooms investigation document."""

    def test_investigation_doc_exists(self):
        """The session document must remain present for traceability."""
        assert _MINIMAP_INVESTIGATION.exists(), (
            f"Missing investigation doc: {_MINIMAP_INVESTIGATION.relative_to(_PROJECT_ROOT)}"
        )

    def test_doc_describes_uuid_vs_stable_id_mismatch(self):
        """
        Documentation must state that explored room identifiers are UUIDs, not stable_ids,
        and that filtering against stable_id breaks matching.
        """
        text = _MINIMAP_INVESTIGATION.read_text(encoding="utf-8").lower()
        assert "get_explored_rooms" in text
        assert "uuid" in text
        assert "stable_id" in text
        assert (
            "incorrectly" in text
            or "mismatch" in text
            or "never match" in text
            or ("comparison" in text and "fail" in text)
        )

    def test_doc_explains_impact_on_non_admin_users(self):
        """Documentation must tie the bug to non-admin minimap behavior (not only admins)."""
        text = _MINIMAP_INVESTIGATION.read_text(encoding="utf-8").lower()
        assert "non-admin" in text
        assert "mini-map" in text or "minimap" in text
        assert (
            "not displaying" in text
            or "not showing" in text
            or "no rooms" in text
            or "empty" in text
            or "minimal" in text
        )
