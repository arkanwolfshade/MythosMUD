"""Tests that SkillService reaches CombatService on both creation paths (#833: the taunt roll needs it)."""

# pyright: reportPrivateUsage=false
# Reason: the two wiring functions under test are module/class private by design.

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from server.app.lifespan_startup import _attach_combat_service
from server.container.bundles.combat import CombatBundle
from server.game.skill_service import SkillService
from server.services.combat_service import CombatService

_SET_COMBAT_SERVICE = "server.services.combat_service.set_combat_service"


def _skill_service() -> SkillService:
    return SkillService(MagicMock(), MagicMock(), MagicMock(), MagicMock())


def test_a_new_combat_service_has_no_skill_service_until_one_is_linked() -> None:
    assert CombatService().skill_service is None


@pytest.mark.asyncio
async def test_combat_bundle_links_the_container_skill_service() -> None:
    skill_service = _skill_service()
    container: MagicMock = MagicMock()
    container.skill_service = skill_service
    bundle = CombatBundle()
    bundle.player_combat_service = MagicMock()
    bundle.player_death_service = MagicMock()
    bundle.player_respawn_service = MagicMock()
    created: list[CombatService] = []

    with patch(_SET_COMBAT_SERVICE, new=created.append):
        await bundle._create_combat_service_with_nats(container)

    assert len(created) == 1
    assert created[0].skill_service is skill_service


def test_lifespan_startup_links_the_container_skill_service() -> None:
    skill_service = _skill_service()
    container: MagicMock = MagicMock()
    container.skill_service = skill_service
    state: MagicMock = MagicMock()
    app: MagicMock = MagicMock()
    app.state = state
    created: list[CombatService] = []

    with patch(_SET_COMBAT_SERVICE, new=created.append):
        _attach_combat_service(app, container)

    assert len(created) == 1
    assert created[0].skill_service is skill_service


def test_lifespan_startup_tolerates_a_container_without_a_skill_service() -> None:
    container: MagicMock = MagicMock()
    container.skill_service = None
    app: MagicMock = MagicMock()
    created: list[CombatService] = []

    with patch(_SET_COMBAT_SERVICE, new=created.append):
        _attach_combat_service(app, container)

    assert created[0].skill_service is None
