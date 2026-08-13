"""
Async item instance persistence operations.

Provides async implementations using PostgreSQL stored procedures,
replacing raw SQL/ORM for use by ItemRepository.
"""

from __future__ import annotations

import json
from typing import Any

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..async_persistence_constants import CreateItemInstanceInput, EnsureItemInstanceInput
from ..exceptions import DatabaseError, ValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import log_and_raise

logger = get_logger(__name__)


def _metadata_from_options(options: CreateItemInstanceInput | EnsureItemInstanceInput) -> dict[str, Any]:
    return options.get("metadata_payload") or options.get("metadata") or {}


def _item_instance_upsert_params(
    item_instance_id: str, prototype_id: str, opts: CreateItemInstanceInput
) -> dict[str, Any]:
    meta_val = _metadata_from_options(opts)
    return {
        "item_instance_id": item_instance_id,
        "prototype_id": prototype_id,
        "owner_type": opts.get("owner_type", "room"),
        "owner_id": opts.get("owner_id"),
        "location_context": opts.get("location_context"),
        "quantity": opts.get("quantity", 1),
        "condition": opts.get("condition"),
        "flags_override": json.dumps(opts.get("flags_override") or []),
        "binding_state": opts.get("binding_state"),
        "attunement_state": json.dumps(opts.get("attunement_state") or {}),
        "custom_name": opts.get("custom_name"),
        "metadata": json.dumps(meta_val),
        "origin_source": opts.get("origin_source"),
        "origin_metadata": json.dumps(opts.get("origin_metadata") or {}),
    }


async def _run_item_instance_upsert(
    session: AsyncSession, item_instance_id: str, prototype_id: str, opts: CreateItemInstanceInput
) -> None:
    await session.execute(
        text(
            "SELECT upsert_item_instance("
            ":item_instance_id, :prototype_id, :owner_type, :owner_id, :location_context,"
            " :quantity, :condition, :flags_override, :binding_state, :attunement_state,"
            " :custom_name, :metadata, :origin_source, :origin_metadata)"
        ),
        _item_instance_upsert_params(item_instance_id, prototype_id, opts),
    )
    await session.commit()


async def create_item_instance_async(
    session: AsyncSession,
    item_instance_id: str,
    prototype_id: str,
    options: CreateItemInstanceInput | None = None,
) -> None:
    """Create or update an item instance in the database (upsert)."""
    opts = options or {}
    if not item_instance_id:
        log_and_raise(
            ValidationError,
            "item_instance_id is required",
            operation="create_item_instance_async",
            user_friendly="Invalid item instance data",
        )
    if not prototype_id:
        log_and_raise(
            ValidationError,
            "prototype_id is required",
            operation="create_item_instance_async",
            user_friendly="Invalid item instance data",
        )

    try:
        await _run_item_instance_upsert(session, item_instance_id, prototype_id, opts)
        logger.debug(
            "Item instance created or updated",
            item_instance_id=item_instance_id,
            prototype_id=prototype_id,
            owner_type=opts.get("owner_type", "room"),
            owner_id=opts.get("owner_id"),
        )
    except SQLAlchemyError as e:
        await session.rollback()
        log_and_raise(
            DatabaseError,
            f"Database error creating item instance: {e}",
            operation="create_item_instance_async",
            item_instance_id=item_instance_id,
            prototype_id=prototype_id,
            details={"error": str(e), "item_instance_id": item_instance_id, "prototype_id": prototype_id},
            user_friendly="Failed to create item instance",
        )


async def item_instance_exists_async(session: AsyncSession, item_instance_id: str) -> bool:
    """Check if an item instance exists via item_instance_exists procedure."""
    result = await session.execute(
        text("SELECT item_instance_exists(:item_instance_id)"),
        {"item_instance_id": item_instance_id},
    )
    return bool(result.scalar())


async def ensure_item_instance_async(
    session: AsyncSession,
    item_instance_id: str,
    prototype_id: str,
    options: EnsureItemInstanceInput | None = None,
) -> None:
    """Ensure an item instance exists in the database, creating it if necessary."""
    opts = options or {}
    await create_item_instance_async(
        session=session,
        item_instance_id=item_instance_id,
        prototype_id=prototype_id,
        options={
            "owner_type": opts.get("owner_type", "room"),
            "owner_id": opts.get("owner_id"),
            "quantity": opts.get("quantity", 1),
            "metadata_payload": _metadata_from_options(opts),
            "origin_source": opts.get("origin_source"),
            "origin_metadata": opts.get("origin_metadata"),
        },
    )
    logger.debug(
        "Item instance ensured",
        item_instance_id=item_instance_id,
        prototype_id=prototype_id,
        quantity=opts.get("quantity", 1),
    )
