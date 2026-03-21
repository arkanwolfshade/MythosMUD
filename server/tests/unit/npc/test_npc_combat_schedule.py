"""Unit tests for best-effort NPC combat cleanup scheduling."""

from unittest.mock import MagicMock, patch

from server.npc.npc_combat_schedule import schedule_end_combat_if_npc_died_best_effort


@patch("server.services.combat_service_state.get_combat_service", return_value=None)
def test_schedule_end_combat_if_npc_died_no_service(_mock_get: MagicMock) -> None:
    """When combat service is missing, scheduling is a no-op."""
    schedule_end_combat_if_npc_died_best_effort("npc-sched-1")


@patch("server.services.combat_service_state.get_combat_service")
def test_schedule_end_combat_if_npc_died_no_running_loop(mock_get: MagicMock) -> None:
    """Without a running asyncio loop, scheduling fails quietly (RuntimeError path)."""
    svc = MagicMock()
    svc.end_combat_if_npc_died = MagicMock()
    mock_get.return_value = svc
    schedule_end_combat_if_npc_died_best_effort("npc-sched-2")
