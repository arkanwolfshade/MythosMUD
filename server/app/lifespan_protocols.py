"""Typed helpers for lifespan startup/shutdown (avoids app.state Any)."""

# pyright: reportAny=false
# Reason: app.state and legacy test container mocks are untyped; services are cast at the boundary.

from __future__ import annotations

from typing import TypeVar, cast

from fastapi import FastAPI

from ..app.task_registry import TaskRegistry
from ..container import ApplicationContainer
from ..events.event_bus import EventBus
from ..realtime.connection_manager import ConnectionManager
from ..realtime.memory_monitor import MemoryMonitor
from ..realtime.nats_message_handler import NATSMessageHandler
from ..time.tick_scheduler import MythosTickScheduler

T = TypeVar("T")


def lifespan_container(app: FastAPI) -> ApplicationContainer | None:
    """Return app.state.container when it is an ApplicationContainer."""
    raw = getattr(app.state, "container", None)
    return raw if isinstance(raw, ApplicationContainer) else None


def _container_attr(container: ApplicationContainer, name: str) -> object:
    """Read a container attribute as object (container fields are loosely typed)."""
    return cast(object, getattr(container, name))


def _legacy_container_attr(app: FastAPI, name: str) -> object | None:
    """Read an attribute from a non-ApplicationContainer app.state.container (tests/legacy)."""
    legacy_container = getattr(app.state, "container", None)
    if legacy_container is not None and not isinstance(legacy_container, ApplicationContainer):
        return getattr(legacy_container, name, None)
    return None


def _resolve_service(app: FastAPI, *, container_name: str, state_name: str, expected: type[T]) -> T | None:  # noqa: UP047
    """Resolve a service from typed container, legacy container, or app.state."""
    container = lifespan_container(app)
    if container is not None:
        candidate = _container_attr(container, container_name)
        if isinstance(candidate, expected):
            return candidate
    legacy = _legacy_container_attr(app, container_name)
    if legacy is not None:
        return cast(T, legacy)
    raw = getattr(app.state, state_name, None)
    if raw is not None:
        return cast(T, raw)
    return None


def _resolve_container_field(container: object, name: str, expected: type[T]) -> T | None:  # noqa: UP047
    """Resolve a field from ApplicationContainer or test container mocks."""
    if isinstance(container, ApplicationContainer):
        candidate = _container_attr(container, name)
        if isinstance(candidate, expected):
            return candidate
    raw = getattr(container, name, None)
    return cast(T, raw) if raw is not None else None


def lifespan_nats_handler(app: FastAPI) -> NATSMessageHandler | None:
    """Return the NATS message handler from container or app.state."""
    return _resolve_service(
        app,
        container_name="nats_message_handler",
        state_name="nats_message_handler",
        expected=NATSMessageHandler,
    )


def lifespan_connection_manager(app: FastAPI) -> ConnectionManager | None:
    """Return the connection manager from container or app.state."""
    return _resolve_service(
        app,
        container_name="connection_manager",
        state_name="connection_manager",
        expected=ConnectionManager,
    )


def lifespan_memory_monitor(app: FastAPI) -> MemoryMonitor | None:
    """Return the connection manager's memory monitor, if present."""
    manager = lifespan_connection_manager(app)
    if manager is None:
        return None
    return manager.memory_monitor


def lifespan_tick_scheduler(app: FastAPI) -> MythosTickScheduler | None:
    """Return the Mythos tick scheduler from container or app.state."""
    return _resolve_service(
        app,
        container_name="mythos_tick_scheduler",
        state_name="mythos_tick_scheduler",
        expected=MythosTickScheduler,
    )


def lifespan_task_registry(container: ApplicationContainer) -> TaskRegistry | None:
    """Return the task registry from the application container."""
    return _resolve_container_field(container, "task_registry", TaskRegistry)


def lifespan_event_bus(container: ApplicationContainer) -> EventBus | None:
    """Return the event bus from the application container."""
    return _resolve_container_field(container, "event_bus", EventBus)


def nats_is_connected(nats_service: object) -> bool:
    """Return True when nats_service exposes is_connected() and it is true."""
    checker = getattr(nats_service, "is_connected", None)
    if not callable(checker):
        return False
    result = checker()
    return bool(result) if isinstance(result, bool) else False
