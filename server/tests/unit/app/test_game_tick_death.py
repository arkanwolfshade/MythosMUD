"""Unit tests for game-tick death, corpse cleanup, broadcast, and loop."""

# pylint: disable=missing-function-docstring  # Reason: test names document behavior
# pyright: reportPrivateUsage=false
# Reason: this module unit-tests private tick helpers (_process_*, corpse cleanup internals).

from __future__ import annotations

import asyncio
import uuid
from collections.abc import AsyncIterator
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import FastAPI

from server.app.game_tick_corpses import (
    _create_corpse_lifecycle_service,
    _log_cleanup_results,
    cleanup_decayed_corpses,
)
from server.app.game_tick_processing import (
    _process_dead_players,
    _process_mortally_wounded_player,
    _process_passive_lucidity_flux,
    broadcast_tick_event,
    game_tick_loop,
    process_dp_decay_and_death,
)
from server.app.game_tick_protocols import _tick_online_players
from server.models.combat import CombatStatus


@pytest.mark.asyncio
async def test_process_mortally_wounded_skips_active_combat() -> None:
    get_combat_by_participant: AsyncMock = AsyncMock()
    combat_service: MagicMock = MagicMock()
    combat_service.get_combat_by_participant = get_combat_by_participant
    process_mortally_wounded_tick: MagicMock = MagicMock()
    player_death_service: MagicMock = MagicMock()
    player_death_service.process_mortally_wounded_tick = process_mortally_wounded_tick
    container: MagicMock = MagicMock()
    container.player_death_service = player_death_service
    container.combat_service = combat_service
    combat: MagicMock = MagicMock()
    combat.status = CombatStatus.ACTIVE
    combat.combat_id = "c1"
    get_combat_by_participant.return_value = combat
    player: MagicMock = MagicMock()
    player.player_id = str(uuid.uuid4())
    player.name = "Victim"
    session: AsyncMock = AsyncMock()
    await _process_mortally_wounded_player(container, player, session)
    process_mortally_wounded_tick.assert_not_called()


@pytest.mark.asyncio
async def test_process_mortally_wounded_death_threshold() -> None:
    process_mortally_wounded_tick: AsyncMock = AsyncMock()
    handle_player_death: AsyncMock = AsyncMock()
    player_death_service: MagicMock = MagicMock()
    player_death_service.process_mortally_wounded_tick = process_mortally_wounded_tick
    player_death_service.handle_player_death = handle_player_death
    move_player_to_limbo: AsyncMock = AsyncMock()
    player_respawn_service: MagicMock = MagicMock()
    player_respawn_service.move_player_to_limbo = move_player_to_limbo
    get_stats: MagicMock = MagicMock(return_value={"current_dp": -10, "max_dp": 100})
    container: MagicMock = MagicMock()
    container.player_death_service = player_death_service
    container.combat_service = None
    container.player_respawn_service = player_respawn_service
    container.event_bus = MagicMock()
    player: MagicMock = MagicMock()
    player.player_id = str(uuid.uuid4())
    player.name = "Victim"
    player.current_room_id = "room-1"
    player.get_stats = get_stats
    session: AsyncMock = AsyncMock()
    with patch(
        "server.app.game_tick_death.combat_messaging_integration.send_dp_decay_message",
        new_callable=AsyncMock,
    ):
        await _process_mortally_wounded_player(container, player, session)
    handle_player_death.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_mortally_wounded_publishes_dp_decay_to_nats() -> None:
    """DP decay tick publishes to NATS (#634) alongside the existing personal message."""
    process_mortally_wounded_tick: AsyncMock = AsyncMock()
    player_death_service: MagicMock = MagicMock()
    player_death_service.process_mortally_wounded_tick = process_mortally_wounded_tick
    combat_service: MagicMock = MagicMock()
    combat_service.get_combat_by_participant = AsyncMock(return_value=None)
    combat_service.publish_player_dp_decay_event_to_nats = AsyncMock(return_value=True)
    container: MagicMock = MagicMock()
    container.player_death_service = player_death_service
    container.combat_service = combat_service
    get_stats: MagicMock = MagicMock(return_value={"current_dp": -3, "max_dp": 100})
    player: MagicMock = MagicMock()
    player.player_id = str(uuid.uuid4())
    player.name = "Victim"
    player.current_room_id = "room-1"
    player.get_stats = get_stats
    session: AsyncMock = AsyncMock()
    with patch(
        "server.app.game_tick_death.combat_messaging_integration.send_dp_decay_message",
        new_callable=AsyncMock,
    ):
        await _process_mortally_wounded_player(container, player, session)
    combat_service.publish_player_dp_decay_event_to_nats.assert_awaited_once()
    published_event = combat_service.publish_player_dp_decay_event_to_nats.await_args.args[0]
    assert published_event.new_dp == -3
    assert published_event.room_id == "room-1"


@pytest.mark.asyncio
async def test_process_dead_players_moves_to_limbo() -> None:
    player_id = uuid.uuid4()
    player: MagicMock = MagicMock()
    player.player_id = player_id
    player.name = "Dead"
    player.current_room_id = "room-1"
    get_dead_players: AsyncMock = AsyncMock(return_value=[player])
    player_death_service: MagicMock = MagicMock()
    player_death_service.get_dead_players = get_dead_players
    move_player_to_limbo: AsyncMock = AsyncMock()
    player_respawn_service: MagicMock = MagicMock()
    player_respawn_service.move_player_to_limbo = move_player_to_limbo
    container: MagicMock = MagicMock()
    container.player_death_service = player_death_service
    container.player_respawn_service = player_respawn_service
    session: AsyncMock = AsyncMock()
    await _process_dead_players(container, session)
    move_player_to_limbo.assert_awaited_once_with(player_id, "room-1", session)


@pytest.mark.asyncio
async def test_process_dp_decay_and_death_with_session() -> None:
    app = FastAPI()
    app.state = MagicMock()
    app.state.container = MagicMock(player_death_service=MagicMock())

    async def _session_gen() -> AsyncIterator[AsyncMock]:
        yield AsyncMock()

    with patch("server.app.game_tick_death.get_async_session", return_value=_session_gen()):
        with patch(
            "server.app.game_tick_death._process_session_dp_decay_and_death",
            new_callable=AsyncMock,
        ) as mock_process:
            await process_dp_decay_and_death(app, tick_count=3)
    mock_process.assert_awaited_once()


@pytest.mark.asyncio
async def test_cleanup_decayed_corpses_on_interval() -> None:
    app = FastAPI()
    app.state = MagicMock()
    app.state.container = MagicMock(connection_manager=MagicMock())
    corpse: MagicMock = MagicMock()
    corpse.container_id = uuid.uuid4()
    corpse.room_id = "room-1"
    service: MagicMock = MagicMock()
    service.get_all_decayed_corpses = AsyncMock(return_value=[corpse])
    service.cleanup_decayed_corpse = AsyncMock()
    with patch("server.app.game_tick_corpses._create_corpse_lifecycle_service", return_value=service):
        with patch("server.services.container_websocket_events.emit_container_decayed", new_callable=AsyncMock):
            await cleanup_decayed_corpses(app, tick_count=60)


def test_create_corpse_lifecycle_service() -> None:
    app = FastAPI()
    app.state = MagicMock()
    app.state.container = MagicMock(persistence=MagicMock(), connection_manager=MagicMock())
    with patch("server.app.game_tick_corpses.get_mythos_chronicle", return_value=MagicMock()):
        service = _create_corpse_lifecycle_service(app)
    assert service is not None


@pytest.mark.asyncio
async def test_broadcast_tick_event() -> None:
    app = FastAPI()
    app.state = MagicMock()
    manager: MagicMock = MagicMock()
    player_id = uuid.uuid4()
    manager.player_websockets = {player_id: ["conn-1"]}
    manager.send_personal_message = AsyncMock()
    app.state.container = MagicMock(connection_manager=manager)
    get_current_mythos_datetime: MagicMock = MagicMock(return_value=MagicMock(isoformat=lambda: "2020-01-01T00:00:00"))
    get_calendar_components: MagicMock = MagicMock()
    format_clock: MagicMock = MagicMock(return_value="08:00")
    chronicle: MagicMock = MagicMock()
    chronicle.get_current_mythos_datetime = get_current_mythos_datetime
    components: MagicMock = MagicMock(
        month_name="January",
        day_of_month=1,
        day_name="Monday",
        week_of_month=1,
        season="winter",
        daypart="morning",
        is_daytime=True,
        is_witching_hour=False,
    )
    get_calendar_components.return_value = components
    chronicle.get_calendar_components = get_calendar_components
    chronicle.format_clock = format_clock
    with patch("server.app.game_tick_processing.get_mythos_chronicle", return_value=chronicle):
        with patch("server.app.game_tick_processing.broadcast_game_event", new_callable=AsyncMock) as mock_broadcast:
            with patch(
                "server.app.game_tick_processing.is_player_in_login_grace_period",
                return_value=False,
            ):
                with patch(
                    "server.app.game_tick_processing.get_login_grace_period_remaining",
                    return_value=0.0,
                ):
                    await broadcast_tick_event(app, tick_count=10)
    mock_broadcast.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_tick_event_skips_when_no_players() -> None:
    app = FastAPI()
    app.state = MagicMock()
    manager: MagicMock = MagicMock()
    manager.player_websockets = {}
    app.state.container = MagicMock(connection_manager=manager)
    with patch("server.app.game_tick_processing.get_mythos_chronicle") as chronicle:
        with patch("server.app.game_tick_processing.broadcast_game_event", new_callable=AsyncMock) as mock_broadcast:
            await broadcast_tick_event(app, tick_count=10)
    mock_broadcast.assert_not_awaited()
    chronicle.assert_not_called()


@pytest.mark.asyncio
async def test_game_tick_loop_cancelled_on_sleep() -> None:
    app = FastAPI()
    app.state = MagicMock()
    app.state.container = MagicMock(
        combat_service=None,
        magic_service=None,
        player_death_service=None,
        npc_lifecycle_manager=None,
    )
    with patch("server.app.game_tick_processing.get_tick_interval", return_value=0.01):
        with patch("server.app.game_tick_processing.sleep", side_effect=asyncio.CancelledError):
            with patch("server.app.game_tick_processing.process_player_effects_expiration", new_callable=AsyncMock):
                with patch("server.app.game_tick_processing.process_status_effects", new_callable=AsyncMock):
                    with patch("server.app.game_tick_processing.process_combat_tick", new_callable=AsyncMock):
                        with patch(
                            "server.app.game_tick_processing.process_casting_progress",
                            new_callable=AsyncMock,
                        ):
                            with patch(
                                "server.app.game_tick_processing.process_dp_decay_and_death",
                                new_callable=AsyncMock,
                            ):
                                with patch(
                                    "server.app.game_tick_processing.process_npc_maintenance",
                                    new_callable=AsyncMock,
                                ):
                                    with patch(
                                        "server.app.game_tick_processing.cleanup_decayed_corpses",
                                        new_callable=AsyncMock,
                                    ):
                                        await game_tick_loop(app)


@pytest.mark.asyncio
async def test_process_passive_lucidity_flux() -> None:
    process_tick: AsyncMock = AsyncMock()
    passive_lucidity_flux_service: MagicMock = MagicMock()
    passive_lucidity_flux_service.process_tick = process_tick
    container: MagicMock = MagicMock()
    container.passive_lucidity_flux_service = passive_lucidity_flux_service
    await _process_passive_lucidity_flux(container, AsyncMock(), tick_count=1)
    process_tick.assert_awaited_once()


def test_log_cleanup_results_warning_path() -> None:
    _log_cleanup_results(tick_count=60, cleaned_count=0, total_decayed=2)


@pytest.mark.asyncio
async def test_tick_online_players_counts_successes() -> None:
    seen: list[str] = []

    async def process_one(player_id_str: str) -> bool:
        seen.append(player_id_str)
        return player_id_str.endswith("1")

    id_ok = uuid.UUID("00000000-0000-0000-0000-000000000001")
    id_skip = uuid.UUID("00000000-0000-0000-0000-000000000002")
    debug: MagicMock = MagicMock()
    with patch("server.app.game_tick_protocols.logger.debug", debug):
        await _tick_online_players([id_ok, id_skip], 3, "Processed test", process_one)
    assert seen == [str(id_ok), str(id_skip)]
    debug.assert_called_once_with("Processed test", tick_count=3, players_processed=1)
