"""Unit tests for wire_instance_content: building the instance content service at startup."""

from typing import cast
from unittest.mock import MagicMock

from server.app.lifespan_instance import wire_instance_content
from server.game.items.item_factory import ItemFactory
from server.game.items.prototype_registry import PrototypeRegistry
from server.services.instance_content import InstanceContentService


def _container(*, with_registry: bool = True, with_npcs: bool = True) -> tuple[MagicMock, MagicMock]:
    """A container with everything wired; returns (container, attach_content mock of its flush service)."""
    registry = PrototypeRegistry({}, [])
    attach_content: MagicMock = MagicMock()
    flusher: MagicMock = MagicMock()
    flusher.attach_content = attach_content
    connection_manager: MagicMock = MagicMock()
    container: MagicMock = MagicMock()
    container.instance_flush_service = flusher
    container.item_prototype_registry = registry if with_registry else None
    container.item_factory = ItemFactory(registry) if with_registry else None
    container.async_persistence = MagicMock()
    container.connection_manager = connection_manager
    container.npc_population_controller = MagicMock() if with_npcs else None
    container.npc_lifecycle_manager = MagicMock() if with_npcs else None
    return container, attach_content


def test_wires_the_content_service_into_the_flush_service_and_the_container() -> None:
    container, attach_content = _container()

    content = wire_instance_content(container)

    assert isinstance(content, InstanceContentService)
    attached = cast(object, getattr(container, "instance_content_service"))  # noqa: B009  # the slot the wiring set
    assert attached is content
    attach_content.assert_called_once_with(content)


def test_wires_without_npc_services() -> None:
    """NPC services are optional: instances still get furniture and floor items."""
    container, attach_content = _container(with_npcs=False)

    content = wire_instance_content(container)

    assert isinstance(content, InstanceContentService)
    attach_content.assert_called_once_with(content)


def test_missing_item_services_leave_instances_unpopulated_without_raising() -> None:
    container, attach_content = _container(with_registry=False)

    assert wire_instance_content(container) is None
    attach_content.assert_not_called()


def test_missing_flush_service_wires_nothing() -> None:
    container, _ = _container()
    container.instance_flush_service = None

    assert wire_instance_content(container) is None
