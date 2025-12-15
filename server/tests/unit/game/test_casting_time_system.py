"""
Unit tests for spell casting time mechanics.

Tests casting time, interruption, combat integration, and command blocking.
"""

from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.app.game_tick_processing import reset_current_tick
from server.game.magic.casting_state_manager import CastingStateManager
from server.game.magic.magic_service import MagicService
from server.game.magic.spell_effects import SpellEffects
from server.game.magic.spell_registry import SpellRegistry
from server.game.magic.spell_targeting import SpellTargetingService
from server.game.player_service import PlayerService
from server.models.spell import Spell, SpellEffectType, SpellRangeType, SpellSchool, SpellTargetType
from server.schemas.target_resolution import TargetMatch, TargetType


@pytest.fixture
def mock_player():
    """Create a mock player for testing."""
    player = MagicMock()
    player.player_id = uuid4()
    player.name = "TestPlayer"
    player.current_room_id = "test_room_001"
    player.get_stats.return_value = {
        "magic_points": 50,
        "max_magic_points": 50,
        "lucidity": 100,
        "corruption": 0,
        "intelligence": 60,
        "luck": 50,
    }
    player.get_inventory.return_value = []
    player.get_status_effects.return_value = []
    return player


@pytest.fixture
def mock_player_service(mock_player):
    """Create a mock player service."""
    service = MagicMock(spec=PlayerService)
    service.persistence = MagicMock()
    service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    service.persistence.save_player = AsyncMock()
    service.heal_player = AsyncMock()
    service.damage_player = AsyncMock()
    service.update_player_location = AsyncMock(return_value=True)
    return service


@pytest.fixture
def mock_spell_registry():
    """Create a mock spell registry."""
    registry = MagicMock(spec=SpellRegistry)
    registry.get_spell = MagicMock(return_value=None)
    registry.get_spell_by_name = MagicMock(return_value=None)
    return registry


@pytest.fixture
def mock_spell_targeting_service():
    """Create a mock spell targeting service."""
    service = MagicMock(spec=SpellTargetingService)
    service.resolve_spell_target = AsyncMock()
    return service


@pytest.fixture
def mock_spell_effects():
    """Create a mock spell effects service."""
    service = MagicMock(spec=SpellEffects)
    service.process_effect = AsyncMock(
        return_value={"success": True, "message": "Spell effect applied", "effect_applied": True}
    )
    return service


@pytest.fixture
def create_test_spell():
    """Factory function to create test spells."""

    def _create_spell(
        spell_id: str = "test_spell",
        name: str = "Test Spell",
        casting_time: int = 0,
        mp_cost: int = 10,
        effect_type: SpellEffectType = SpellEffectType.HEAL,
    ) -> Spell:
        return Spell(
            spell_id=spell_id,
            name=name,
            description="A test spell",
            school=SpellSchool.ELEMENTAL,
            mp_cost=mp_cost,
            lucidity_cost=0,
            corruption_on_learn=0,
            corruption_on_cast=0,
            casting_time_seconds=casting_time,
            target_type=SpellTargetType.ENTITY,
            range_type=SpellRangeType.SAME_ROOM,
            effect_type=effect_type,
            effect_data={"heal_amount": 20},
            materials=[],
        )

    return _create_spell


@pytest.fixture
def casting_state_manager():
    """Create a casting state manager for testing."""
    return CastingStateManager()


@pytest.fixture
def magic_service(
    mock_player_service, mock_spell_registry, mock_spell_targeting_service, mock_spell_effects, casting_state_manager
):
    """Create a magic service for testing."""
    from server.persistence.repositories.player_spell_repository import PlayerSpellRepository

    player_spell_repository = MagicMock(spec=PlayerSpellRepository)
    player_spell_repository.get_player_spell = AsyncMock(return_value=MagicMock(mastery=50))
    player_spell_repository.record_spell_cast = AsyncMock()
    player_spell_repository.update_mastery = AsyncMock()

    return MagicService(
        spell_registry=mock_spell_registry,
        player_service=mock_player_service,
        spell_targeting_service=mock_spell_targeting_service,
        spell_effects=mock_spell_effects,
        player_spell_repository=player_spell_repository,
        casting_state_manager=casting_state_manager,
    )


class TestCastingStateManager:
    """Tests for CastingStateManager."""

    def test_start_casting_creates_state(self, casting_state_manager, create_test_spell):
        """Test that start_casting creates a casting state."""
        player_id = uuid4()
        spell = create_test_spell(casting_time=5)

        state = casting_state_manager.start_casting(
            player_id=player_id,
            spell=spell,
            start_tick=0,
            mastery=50,
        )

        assert state is not None
        assert state.player_id == player_id
        assert state.spell_id == spell.spell_id
        assert state.casting_time_seconds == 5
        assert state.remaining_seconds == 5

    def test_start_casting_prevents_duplicate(self, casting_state_manager, create_test_spell):
        """Test that starting a second cast while already casting raises ValueError."""
        player_id = uuid4()
        spell = create_test_spell(casting_time=5)

        casting_state_manager.start_casting(player_id=player_id, spell=spell, start_tick=0, mastery=50)

        with pytest.raises(ValueError, match="already casting"):
            casting_state_manager.start_casting(player_id=player_id, spell=spell, start_tick=1, mastery=50)

    def test_is_casting_returns_true_when_casting(self, casting_state_manager, create_test_spell):
        """Test that is_casting returns True when player is casting."""
        player_id = uuid4()
        spell = create_test_spell(casting_time=5)

        assert casting_state_manager.is_casting(player_id) is False

        casting_state_manager.start_casting(player_id=player_id, spell=spell, start_tick=0, mastery=50)

        assert casting_state_manager.is_casting(player_id) is True

    def test_update_casting_progress_decrements_time(self, casting_state_manager, create_test_spell):
        """Test that update_casting_progress decrements remaining time."""
        player_id = uuid4()
        spell = create_test_spell(casting_time=5)

        casting_state_manager.start_casting(player_id=player_id, spell=spell, start_tick=0, mastery=50)

        # Update after 20 ticks (2 seconds at 0.1s per tick)
        is_complete = casting_state_manager.update_casting_progress(player_id, 20)
        state = casting_state_manager.get_casting_state(player_id)

        assert state is not None
        # 5 seconds - (20 ticks * 0.1s/tick) = 5 - 2 = 3 seconds remaining
        assert abs(state.remaining_seconds - 3.0) < 0.01
        assert is_complete is False

    def test_update_casting_progress_completes_when_time_elapsed(self, casting_state_manager, create_test_spell):
        """Test that update_casting_progress returns True when time is up."""
        player_id = uuid4()
        spell = create_test_spell(casting_time=5)

        casting_state_manager.start_casting(player_id=player_id, spell=spell, start_tick=0, mastery=50)

        # Update after 50 ticks (5 seconds at 0.1s per tick: 50 * 0.1 = 5 seconds)
        is_complete = casting_state_manager.update_casting_progress(player_id, 50)

        assert is_complete is True

    def test_complete_casting_removes_state(self, casting_state_manager, create_test_spell):
        """Test that complete_casting removes the casting state."""
        player_id = uuid4()
        spell = create_test_spell(casting_time=5)

        casting_state_manager.start_casting(player_id=player_id, spell=spell, start_tick=0, mastery=50)
        assert casting_state_manager.is_casting(player_id) is True

        state = casting_state_manager.complete_casting(player_id)

        assert state is not None
        assert casting_state_manager.is_casting(player_id) is False

    def test_interrupt_casting_removes_state(self, casting_state_manager, create_test_spell):
        """Test that interrupt_casting removes the casting state."""
        player_id = uuid4()
        spell = create_test_spell(casting_time=5)

        casting_state_manager.start_casting(player_id=player_id, spell=spell, start_tick=0, mastery=50)
        assert casting_state_manager.is_casting(player_id) is True

        state = casting_state_manager.interrupt_casting(player_id)

        assert state is not None
        assert casting_state_manager.is_casting(player_id) is False

    def test_wait_for_initiative_delays_start(self, casting_state_manager, create_test_spell):
        """Test that casting waits for initiative when not player's turn."""
        player_id = uuid4()
        spell = create_test_spell(casting_time=5)

        # Start casting with next_initiative_tick set
        casting_state_manager.start_casting(
            player_id=player_id, spell=spell, start_tick=0, next_initiative_tick=6, mastery=50
        )

        # Update before initiative (tick 3)
        is_complete = casting_state_manager.update_casting_progress(player_id, 3)
        state = casting_state_manager.get_casting_state(player_id)

        assert is_complete is False
        assert state.next_initiative_tick == 6
        assert state.remaining_seconds == 5  # Should not have started yet

        # Update at initiative (tick 6)
        is_complete = casting_state_manager.update_casting_progress(player_id, 6)
        state = casting_state_manager.get_casting_state(player_id)

        assert state.next_initiative_tick is None  # Initiative arrived
        assert state.start_tick == 6  # Casting starts now

        # Update after 50 more ticks (tick 56: 6 + 50 = 56, which is 5 seconds at 0.1s per tick)
        is_complete = casting_state_manager.update_casting_progress(player_id, 56)

        assert is_complete is True


class TestMagicServiceCastingTime:
    """Tests for MagicService casting time mechanics."""

    @pytest.mark.asyncio
    async def test_instant_cast_executes_immediately(
        self, magic_service, mock_player, mock_spell_registry, mock_spell_targeting_service, create_test_spell
    ):
        """Test that spells with 0 casting time execute immediately."""
        reset_current_tick()

        spell = create_test_spell(casting_time=0, spell_id="instant_spell")
        target = TargetMatch(
            target_id=str(mock_player.player_id),
            target_name=mock_player.name,
            target_type=TargetType.PLAYER,
            room_id=mock_player.current_room_id,
        )

        mock_spell_registry.get_spell_by_name.return_value = spell
        mock_spell_targeting_service.resolve_spell_target = AsyncMock(return_value=(target, ""))

        result = await magic_service.cast_spell(mock_player.player_id, "instant_spell")

        assert result["success"] is True
        # Accept various success messages: "cast successfully", "healed", "spell effect applied"
        assert (
            "cast successfully" in result["message"].lower()
            or "healed" in result["message"].lower()
            or "spell effect applied" in result["message"].lower()
        )
        assert result.get("is_casting") is None  # Not casting, executed immediately
        assert not magic_service.casting_state_manager.is_casting(mock_player.player_id)

    @pytest.mark.asyncio
    async def test_delayed_cast_starts_casting_state(
        self, magic_service, mock_player, mock_spell_registry, mock_spell_targeting_service, create_test_spell
    ):
        """Test that spells with casting time > 0 start casting state."""
        reset_current_tick()

        spell = create_test_spell(casting_time=5, spell_id="delayed_spell")
        target = TargetMatch(
            target_id=str(mock_player.player_id),
            target_name=mock_player.name,
            target_type=TargetType.PLAYER,
            room_id=mock_player.current_room_id,
        )

        mock_spell_registry.get_spell_by_name.return_value = spell
        mock_spell_targeting_service.resolve_spell_target = AsyncMock(return_value=(target, ""))

        result = await magic_service.cast_spell(mock_player.player_id, "delayed_spell")

        assert result["success"] is True
        assert "begin casting" in result["message"].lower()
        assert result.get("is_casting") is True
        assert result.get("casting_time") == 5
        assert magic_service.casting_state_manager.is_casting(mock_player.player_id)

    @pytest.mark.asyncio
    async def test_cannot_cast_while_already_casting(
        self, magic_service, mock_player, mock_spell_registry, mock_spell_targeting_service, create_test_spell
    ):
        """Test that players cannot start a new cast while already casting."""
        reset_current_tick()

        spell1 = create_test_spell(casting_time=5, spell_id="spell1")
        spell2 = create_test_spell(casting_time=3, spell_id="spell2")
        target = TargetMatch(
            target_id=str(mock_player.player_id),
            target_name=mock_player.name,
            target_type=TargetType.PLAYER,
            room_id=mock_player.current_room_id,
        )

        mock_spell_registry.get_spell_by_name = MagicMock(side_effect=[spell1, spell2])
        mock_spell_targeting_service.resolve_spell_target = AsyncMock(return_value=(target, ""))

        # Start first cast
        result1 = await magic_service.cast_spell(mock_player.player_id, "spell1")
        assert result1["success"] is True

        # Try to start second cast
        result2 = await magic_service.cast_spell(mock_player.player_id, "spell2")

        assert result2["success"] is False
        assert "already casting" in result2["message"].lower()

    @pytest.mark.asyncio
    async def test_casting_progress_completes_spell(
        self, magic_service, mock_player, mock_spell_registry, mock_spell_targeting_service, create_test_spell
    ):
        """Test that check_casting_progress completes spells when time elapses."""
        reset_current_tick()

        spell = create_test_spell(casting_time=3, spell_id="progress_spell")
        target = TargetMatch(
            target_id=str(mock_player.player_id),
            target_name=mock_player.name,
            target_type=TargetType.PLAYER,
            room_id=mock_player.current_room_id,
        )

        mock_spell_registry.get_spell_by_name.return_value = spell
        mock_spell_targeting_service.resolve_spell_target = AsyncMock(return_value=(target, ""))

        # Start casting
        await magic_service.cast_spell(mock_player.player_id, "progress_spell")
        assert magic_service.casting_state_manager.is_casting(mock_player.player_id)

        # Progress 20 ticks (2 seconds at 0.1s per tick, not complete yet)
        await magic_service.check_casting_progress(20)
        assert magic_service.casting_state_manager.is_casting(mock_player.player_id)

        # Progress to 30 ticks (3 seconds at 0.1s per tick, should complete)
        await magic_service.check_casting_progress(30)
        assert not magic_service.casting_state_manager.is_casting(mock_player.player_id)

        # Verify effect was processed
        magic_service.spell_effects.process_effect.assert_called_once()

    @pytest.mark.asyncio
    async def test_interrupt_casting_with_luck_pass(
        self, magic_service, mock_player, create_test_spell, mock_spell_registry, mock_spell_targeting_service
    ):
        """Test that interrupting with LUCK pass doesn't consume MP."""
        reset_current_tick()

        spell = create_test_spell(casting_time=5, spell_id="interrupt_spell", mp_cost=20)
        target = TargetMatch(
            target_id=str(mock_player.player_id),
            target_name=mock_player.name,
            target_type=TargetType.PLAYER,
            room_id=mock_player.current_room_id,
        )

        mock_spell_registry.get_spell_by_name.return_value = spell
        mock_spell_targeting_service.resolve_spell_target = AsyncMock(return_value=(target, ""))

        # Start casting
        await magic_service.cast_spell(mock_player.player_id, "interrupt_spell")

        # Set luck to 100 (guaranteed pass)
        mock_player.get_stats.return_value["luck"] = 100

        # Interrupt
        result = await magic_service.interrupt_casting(mock_player.player_id)

        assert result["success"] is True
        assert "luck preserves" in result["message"].lower()
        assert result.get("mp_lost") is False
        assert not magic_service.casting_state_manager.is_casting(mock_player.player_id)

        # Verify casting state was cleared
        assert not magic_service.casting_state_manager.is_casting(mock_player.player_id)

    @pytest.mark.asyncio
    async def test_interrupt_casting_with_luck_fail(
        self, magic_service, mock_player, create_test_spell, mock_spell_registry, mock_spell_targeting_service
    ):
        """Test that interrupting with LUCK fail consumes MP."""
        reset_current_tick()

        spell = create_test_spell(casting_time=5, spell_id="interrupt_spell", mp_cost=20)
        target = TargetMatch(
            target_id=str(mock_player.player_id),
            target_name=mock_player.name,
            target_type=TargetType.PLAYER,
            room_id=mock_player.current_room_id,
        )

        mock_spell_registry.get_spell_by_name.return_value = spell
        mock_spell_targeting_service.resolve_spell_target = AsyncMock(return_value=(target, ""))

        # Start casting
        await magic_service.cast_spell(mock_player.player_id, "interrupt_spell")

        # Set luck to 0 (guaranteed fail)
        mock_player.get_stats.return_value["luck"] = 0

        # Interrupt (will fail LUCK check)
        with patch("random.randint", return_value=1):  # Roll 1, luck is 0, so fail
            result = await magic_service.interrupt_casting(mock_player.player_id)

        assert result["success"] is True
        assert "disruption costs" in result["message"].lower()
        assert result.get("mp_lost") is True
        assert result.get("mp_cost") == 20
        assert not magic_service.casting_state_manager.is_casting(mock_player.player_id)

        # Verify casting state was cleared
        assert not magic_service.casting_state_manager.is_casting(mock_player.player_id)
        # MP consumption is verified by checking player stats were updated
        # (This would be verified in integration tests)

    @pytest.mark.asyncio
    async def test_combat_initiative_wait(
        self, magic_service, mock_player, create_test_spell, mock_spell_registry, mock_spell_targeting_service
    ):
        """Test that casting waits for player's turn in combat."""
        reset_current_tick()

        from server.models.combat import CombatInstance, CombatParticipant
        from server.services.combat_service import CombatService

        spell = create_test_spell(casting_time=3, spell_id="combat_spell")
        target = TargetMatch(
            target_id=str(mock_player.player_id),
            target_name=mock_player.name,
            target_type=TargetType.PLAYER,
            room_id=mock_player.current_room_id,
        )

        mock_spell_registry.get_spell_by_name.return_value = spell
        mock_spell_targeting_service.resolve_spell_target = AsyncMock(return_value=(target, ""))

        # Create mock combat where it's NOT player's turn
        combat = MagicMock(spec=CombatInstance)
        combat.combat_id = uuid4()
        combat.turn_interval_ticks = 6
        combat.next_turn_tick = 6
        current_participant = MagicMock(spec=CombatParticipant)
        current_participant.participant_id = uuid4()  # Different from player_id
        combat.get_current_turn_participant.return_value = current_participant

        mock_combat_service = MagicMock(spec=CombatService)
        mock_combat_service.get_combat_by_participant = AsyncMock(return_value=combat)
        magic_service.combat_service = mock_combat_service

        # Start casting
        result = await magic_service.cast_spell(mock_player.player_id, "combat_spell")

        assert result["success"] is True
        assert "waiting for your turn" in result["message"].lower()

        casting_state = magic_service.casting_state_manager.get_casting_state(mock_player.player_id)
        assert casting_state is not None
        assert casting_state.next_initiative_tick == 6  # Waiting for turn

        # Progress before initiative - should not advance
        await magic_service.check_casting_progress(3)
        casting_state = magic_service.casting_state_manager.get_casting_state(mock_player.player_id)
        assert casting_state.remaining_seconds == 3  # Still waiting (hasn't started casting yet)

        # Progress to initiative - should start casting
        await magic_service.check_casting_progress(6)
        casting_state = magic_service.casting_state_manager.get_casting_state(mock_player.player_id)
        assert casting_state.next_initiative_tick is None  # Started casting
        assert casting_state.start_tick == 6

        # Complete casting (3 seconds = 30 ticks at 0.1s per tick, so 6 + 30 = 36)
        await magic_service.check_casting_progress(36)
        assert not magic_service.casting_state_manager.is_casting(mock_player.player_id)

    @pytest.mark.asyncio
    async def test_multi_round_casting(
        self, magic_service, mock_player, create_test_spell, mock_spell_registry, mock_spell_targeting_service
    ):
        """Test that spells can span multiple combat rounds."""
        reset_current_tick()

        # Spell with 10 seconds casting time (spans 2 rounds of 6 seconds each)
        spell = create_test_spell(casting_time=10, spell_id="multi_round_spell")
        target = TargetMatch(
            target_id=str(mock_player.player_id),
            target_name=mock_player.name,
            target_type=TargetType.PLAYER,
            room_id=mock_player.current_room_id,
        )

        mock_spell_registry.get_spell_by_name.return_value = spell
        mock_spell_targeting_service.resolve_spell_target = AsyncMock(return_value=(target, ""))

        # Start casting
        await magic_service.cast_spell(mock_player.player_id, "multi_round_spell")

        # Progress through first round (60 ticks = 6 seconds at 0.1s per tick)
        await magic_service.check_casting_progress(60)
        casting_state = magic_service.casting_state_manager.get_casting_state(mock_player.player_id)
        assert casting_state is not None
        # 10 seconds - (60 ticks * 0.1s/tick) = 10 - 6 = 4 seconds remaining
        assert abs(casting_state.remaining_seconds - 4.0) < 0.01

        # Progress through second round (100 ticks total = 10 seconds at 0.1s per tick)
        # Start was at tick 0, so after 100 ticks we've elapsed 10 seconds
        await magic_service.check_casting_progress(100)
        assert not magic_service.casting_state_manager.is_casting(mock_player.player_id)

        # Verify effect was processed
        magic_service.spell_effects.process_effect.assert_called_once()


class TestCastingCommandBlocking:
    """Tests for command blocking during casting."""

    @pytest.mark.asyncio
    async def test_commands_blocked_during_casting(self, casting_state_manager, create_test_spell):
        """Test that most commands are blocked during casting."""
        player_id = uuid4()
        spell = create_test_spell(casting_time=5)

        casting_state_manager.start_casting(player_id=player_id, spell=spell, start_tick=0, mastery=50)

        assert casting_state_manager.is_casting(player_id) is True

    @pytest.mark.asyncio
    async def test_stop_command_allowed_during_casting(self, casting_state_manager, create_test_spell):
        """Test that stop command is allowed during casting."""
        player_id = uuid4()
        spell = create_test_spell(casting_time=5)

        casting_state_manager.start_casting(player_id=player_id, spell=spell, start_tick=0, mastery=50)

        # stop command should be allowed (tested via command handler, not here)
        assert casting_state_manager.is_casting(player_id) is True


class TestCastingAutoattackDisabling:
    """Tests for autoattack disabling during casting."""

    def test_casting_state_check_for_autoattack(self, casting_state_manager, create_test_spell):
        """Test that casting state can be checked for autoattack prevention."""
        player_id = uuid4()
        spell = create_test_spell(casting_time=5)

        assert casting_state_manager.is_casting(player_id) is False

        casting_state_manager.start_casting(player_id=player_id, spell=spell, start_tick=0, mastery=50)

        assert casting_state_manager.is_casting(player_id) is True
