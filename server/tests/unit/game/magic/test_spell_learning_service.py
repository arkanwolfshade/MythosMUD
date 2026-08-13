"""Unit tests for SpellLearningService."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.magic.spell_learning_service import SpellLearningService


@pytest.fixture
def learning_service() -> SpellLearningService:
    registry = MagicMock()
    player_service = MagicMock()
    player_service.persistence = MagicMock()
    repo = MagicMock()
    repo.get_player_spell = AsyncMock(return_value=None)
    repo.learn_spell = AsyncMock()
    repo.get_player_spells = AsyncMock(return_value=[])
    repo.update_mastery = AsyncMock()
    return SpellLearningService(registry, player_service, repo)


@pytest.mark.asyncio
async def test_learn_spell_not_found(learning_service: SpellLearningService) -> None:
    learning_service.spell_registry.get_spell.return_value = None
    learning_service.spell_registry.get_spell_by_name.return_value = None
    result = await learning_service.learn_spell(uuid.uuid4(), "missing")
    assert result["success"] is False
    assert "not found" in result["message"]


@pytest.mark.asyncio
async def test_learn_spell_player_missing(learning_service: SpellLearningService) -> None:
    spell = MagicMock(spell_id="s1", name="Cantrip")
    learning_service.spell_registry.get_spell.return_value = spell
    learning_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=None)
    result = await learning_service.learn_spell(uuid.uuid4(), "s1")
    assert result["success"] is False


@pytest.mark.asyncio
async def test_learn_spell_already_known(learning_service: SpellLearningService) -> None:
    spell = MagicMock(spell_id="s1", name="Cantrip")
    learning_service.spell_registry.get_spell.return_value = spell
    learning_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=MagicMock())
    learning_service.player_spell_repository.get_player_spell = AsyncMock(return_value=MagicMock())
    result = await learning_service.learn_spell(uuid.uuid4(), "s1")
    assert result["already_known"] is True


@pytest.mark.asyncio
async def test_learn_spell_success(learning_service: SpellLearningService) -> None:
    spell = MagicMock(spell_id="s1", name="Cantrip", is_mythos=MagicMock(return_value=False), corruption_on_learn=0)
    spell.effect_data = {}
    player = MagicMock()
    player.get_stats.return_value = {}
    learning_service.spell_registry.get_spell.return_value = spell
    learning_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    with patch.object(
        learning_service, "_validate_prerequisites", new_callable=AsyncMock, return_value={"valid": True}
    ):
        result = await learning_service.learn_spell(uuid.uuid4(), "s1", source="test")
    assert result["success"] is True
    assert "learned" in result["message"]


@pytest.mark.asyncio
async def test_validate_prerequisites_power_too_low(learning_service: SpellLearningService) -> None:
    spell = MagicMock(effect_data={"required_power": 80})
    player = MagicMock()
    player.get_stats.return_value = {"power": 40}
    learning_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    result = await learning_service._validate_prerequisites(uuid.uuid4(), spell)
    assert result["valid"] is False


@pytest.mark.asyncio
async def test_increase_mastery_on_cast(learning_service: SpellLearningService) -> None:
    player_spell = MagicMock(mastery=10)
    learning_service.player_spell_repository.get_player_spell = AsyncMock(return_value=player_spell)
    with patch("random.random", return_value=0.1):
        await learning_service.increase_mastery_on_cast(uuid.uuid4(), "s1", True)
    learning_service.player_spell_repository.update_mastery.assert_awaited_once()


@pytest.mark.asyncio
async def test_validate_prerequisites_intelligence_too_low(learning_service: SpellLearningService) -> None:
    spell = MagicMock(effect_data={"required_intelligence": 80})
    player = MagicMock()
    player.get_stats.return_value = {"intelligence": 40, "power": 50}
    learning_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    result = await learning_service._validate_prerequisites(uuid.uuid4(), spell)
    assert result["valid"] is False


@pytest.mark.asyncio
async def test_validate_prerequisites_missing_required_spells(learning_service: SpellLearningService) -> None:
    spell = MagicMock(effect_data={"required_spells": ["spell_a"]})
    player = MagicMock()
    player.get_stats.return_value = {"power": 50, "intelligence": 50}
    learning_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    learning_service.player_spell_repository.get_player_spells = AsyncMock(return_value=[])
    req_spell = MagicMock()
    req_spell.name = "Prerequisite"
    learning_service.spell_registry.get_spell.return_value = req_spell
    result = await learning_service._validate_prerequisites(uuid.uuid4(), spell)
    assert result["valid"] is False


@pytest.mark.asyncio
async def test_learn_spell_from_npc(learning_service: SpellLearningService) -> None:
    with patch.object(learning_service, "learn_spell", new_callable=AsyncMock, return_value={"success": True}) as learn:
        result = await learning_service.learn_spell_from_npc(uuid.uuid4(), "npc-1", "s1")
    assert result["success"] is True
    learn.assert_awaited_once()


@pytest.mark.asyncio
async def test_learn_spell_from_book_no_spell_id(learning_service: SpellLearningService) -> None:
    result = await learning_service.learn_spell_from_book(uuid.uuid4(), "book-1")
    assert result["success"] is False


@pytest.mark.asyncio
async def test_learn_spell_from_book_with_spell(learning_service: SpellLearningService) -> None:
    with patch.object(learning_service, "learn_spell", new_callable=AsyncMock, return_value={"success": True}) as learn:
        result = await learning_service.learn_spell_from_book(uuid.uuid4(), "book-1", spell_id="s1")
    assert result["success"] is True
    learn.assert_awaited_once()
