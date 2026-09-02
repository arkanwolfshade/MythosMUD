"""
Unit tests for room_write schemas.

#755: these request models now inherit SecureBaseModel.
"""

import pytest
from pydantic import ValidationError

from server.schemas.rooms.room_write import ExitCreateRequest, ExitUpdateRequest, RoomUpdateRequest
from server.schemas.shared.base import SecureBaseModel


@pytest.mark.parametrize(
    "model_cls,payload",
    [
        (RoomUpdateRequest, {"name": "New name"}),
        (ExitCreateRequest, {"direction": "north", "target_room_id": "some_room"}),
        (ExitUpdateRequest, {"target_room_id": "some_room"}),
    ],
)
def test_room_write_request_schemas_reject_unknown_field(
    model_cls: type[SecureBaseModel], payload: dict[str, object]
) -> None:
    """An extra field in the request body must be rejected, not silently discarded."""
    with pytest.raises(ValidationError):
        _ = model_cls.model_validate({**payload, "unexpected_field": "nope"})


def test_room_update_request_environment_is_set_still_works() -> None:
    """Regression guard: model_fields_set introspection still works after the migration."""
    request = RoomUpdateRequest.model_validate({"environment": ""})
    assert request.environment_is_set() is True

    request_without_environment = RoomUpdateRequest.model_validate({"name": "New name"})
    assert request_without_environment.environment_is_set() is False
