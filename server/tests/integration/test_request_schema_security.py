"""
Guard: every FastAPI request-body schema must inherit SecureBaseModel.

#755 found that most of server/schemas/ subclasses bare pydantic.BaseModel despite
SecureBaseModel's docstring ("all models that handle user input or API requests should
inherit from this"). This test makes that rule mechanically enforced instead of a
convention nobody checks: it walks the real app's route table, resolves each route's
body-bound parameter to a schema class, follows nested model fields transitively, and
asserts every reachable model is a SecureBaseModel subclass.

Deliberately in the integration tier, not unit: this is the first test in the suite to
import server.main. Reading app.routes only needs the import (create_app() never runs
lifespan at construction time - see server/app/factory.py), so no NATS connection and no
background threads start. Keeping that import confined to one integration module matters
because the same import landing in *unit* workers, under per-item xdist distribution, is
what crashed workers during the #757 PR2 pass (see #724).
"""

import inspect
import re
from collections.abc import Callable, Iterator, Sequence
from typing import ClassVar, Protocol, cast, get_args, get_origin, get_type_hints, runtime_checkable

import pytest
from fastapi.routing import APIRoute
from pydantic import BaseModel, ConfigDict, ValidationError
from starlette.routing import BaseRoute

from server.main import app
from server.schemas.shared.base import SecureBaseModel

# Methods that carry a request body per the OpenAPI/HTTP convention this app follows.
_BODY_METHODS = frozenset({"POST", "PUT", "PATCH"})


@runtime_checkable
class _RouterHolder(Protocol):  # pylint: disable=too-few-public-methods  # Reason: structural Protocol, one attribute is the whole shape
    """Structural shape of fastapi.routing's internal include-router wrapper."""

    original_router: object


@runtime_checkable
class _RouteContainer(Protocol):  # pylint: disable=too-few-public-methods  # Reason: structural Protocol, one attribute is the whole shape
    """Structural shape shared by Router/APIRouter/Mount: something with .routes."""

    routes: Sequence[BaseRoute]


def _iter_api_routes(routes: Sequence[BaseRoute]) -> Iterator[APIRoute]:
    """
    Recursively descend into every route grouping to find leaf APIRoutes.

    app.include_router() in this FastAPI version does not flatten sub-router routes
    onto app.routes; it wraps each included router in an internal object exposing the
    real APIRouter via `.original_router`. Matched structurally (rather than importing
    that private class) so a FastAPI upgrade that renames it doesn't silently make this
    walk find nothing - see the "no request-body models found" self-check below.
    """
    for route in routes:
        if isinstance(route, APIRoute):
            yield route
        elif isinstance(route, _RouterHolder):
            holder = route.original_router
            if isinstance(holder, _RouteContainer):
                yield from _iter_api_routes(holder.routes)
        elif isinstance(route, _RouteContainer):
            yield from _iter_api_routes(route.routes)


_MISSING_NAME_RE = re.compile(r"name '(\w+)' is not defined")


def _resolve_hints(func: Callable[..., object]) -> dict[str, object]:
    """
    Best-effort get_type_hints: resolves every annotation get_type_hints can, even when
    the function also carries an unrelated unresolvable forward reference (e.g. a
    TYPE_CHECKING-only DI container type, never imported at runtime, on a sibling
    parameter). get_type_hints fails the *whole* signature on the first unresolved name;
    retry with each offending name stubbed to `object` in localns so the parameters this
    guard actually cares about keep resolving to their real type - a name stubbed to
    `object` can never accidentally pass the `issubclass(..., BaseModel)` check below, so
    this cannot manufacture a false negative, only recover from an unrelated NameError.
    """
    localns: dict[str, object] = {}
    for _ in range(10):  # generous bound; a real route signature won't carry 10 dangling refs
        try:
            return get_type_hints(func, localns=localns)
        except NameError as exc:
            match = _MISSING_NAME_RE.search(str(exc))
            if not match:
                raise
            localns[match.group(1)] = object
    raise RuntimeError(f"Could not resolve type hints for {func!r} after repeated stubbing")


def _iter_body_models(route: APIRoute) -> Iterator[type[BaseModel]]:
    """Yield each BaseModel subclass bound as a body parameter on this route."""
    if not _BODY_METHODS.intersection(route.methods or set()):
        return
    # get_type_hints (not inspect.signature's raw .annotation) is required here: several
    # endpoint modules (e.g. npc_schemas.py, container_endpoints_basic.py) use
    # `from __future__ import annotations`, which turns every annotation into an
    # unresolved string. inspect.signature returns those strings verbatim; get_type_hints
    # resolves them against the endpoint's own module globals - the same resolution
    # FastAPI itself performs internally to build request validation, so this walk sees
    # exactly what FastAPI sees. Extras stripped (default), so Annotated[Model, Body()]
    # already resolves straight to Model with no separate unwrap step needed.
    hints = _resolve_hints(route.endpoint)
    for name in inspect.signature(route.endpoint).parameters:
        annotation = cast(object, hints.get(name))
        if isinstance(annotation, type) and issubclass(annotation, BaseModel):
            yield annotation


def _iter_nested_models(model: type[BaseModel], seen: set[type[BaseModel]]) -> Iterator[type[BaseModel]]:
    """Yield model and every BaseModel subclass reachable through its fields, once each."""
    if model in seen:
        return
    seen.add(model)
    yield model
    for field_info in model.model_fields.values():
        annotation = cast(object, field_info.annotation)
        candidates = get_args(annotation) if get_origin(annotation) is not None else (annotation,)
        for candidate in candidates:
            if isinstance(candidate, type) and issubclass(candidate, BaseModel):
                yield from _iter_nested_models(candidate, seen)


def _all_route_reachable_models() -> dict[type[BaseModel], list[str]]:
    """Map each request-body-reachable model to the route path(s) that reach it."""
    reached: dict[type[BaseModel], list[str]] = {}
    seen: set[type[BaseModel]] = set()
    for route in _iter_api_routes(app.routes):
        for body_model in _iter_body_models(route):
            for model in _iter_nested_models(body_model, seen):
                reached.setdefault(model, []).append(f"{sorted(route.methods or [])} {route.path}")
    return reached


def test_every_request_body_schema_is_secure_base_model() -> None:
    """Every schema reachable from a request body must inherit SecureBaseModel."""
    reached = _all_route_reachable_models()
    assert reached, "No request-body models found - route walk likely broken, not a clean pass"

    offenders = {model: routes for model, routes in reached.items() if not issubclass(model, SecureBaseModel)}
    if offenders:
        details = "\n".join(
            f"  - {model.__module__}.{model.__qualname__} (reached via {routes})" for model, routes in offenders.items()
        )
        pytest.fail(f"Request-body schemas must inherit SecureBaseModel, but {len(offenders)} do not:\n{details}")


def test_secure_base_model_config_survives_subclass_json_schema_extra() -> None:
    """
    A subclass that redeclares model_config only for json_schema_extra must still enforce
    the inherited security settings - Pydantic v2 merges base and subclass model_config,
    but this is exactly the assumption #755's migration relies on, so assert it directly
    rather than trusting it silently.
    """

    class _WithExtraExample(SecureBaseModel):
        name: str
        model_config: ClassVar[ConfigDict] = ConfigDict(json_schema_extra={"example": {"name": "test"}})

    assert _WithExtraExample.model_config.get("extra") == "forbid"
    # extra="forbid" makes an unknown kwarg a static type error on the constructor itself;
    # go through model_validate (an untyped payload, exactly like an inbound request body)
    # to exercise the runtime rejection this test is actually checking.
    payload: dict[str, object] = {"name": "test", "unexpected_field": "nope"}
    with pytest.raises(ValidationError):
        _ = _WithExtraExample.model_validate(payload)
