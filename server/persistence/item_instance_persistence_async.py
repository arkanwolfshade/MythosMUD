"""
Async item instance persistence operations.

Provides async implementations using SQLAlchemy AsyncSession, replacing
the sync psycopg2-based item_instance_persistence for use by ItemRepository.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any, cast

from sqlalchemy import Table, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..exceptions import DatabaseError, ValidationError
from ..models.item import ItemInstance
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)


async def create_item_instance_async(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Item creation requires many parameters for complex item instantiation logic
    session: AsyncSession,
    item_instance_id: str,
    prototype_id: str,
    owner_type: str = "room",
    owner_id: str | None = None,
    location_context: str | None = None,
    quantity: int = 1,
    condition: int | None = None,
    flags_override: list[str] | None = None,
    binding_state: str | None = None,
    attunement_state: dict[str, Any] | None = None,
    custom_name: str | None = None,
    metadata_payload: dict[str, Any] | None = None,
    origin_source: str | None = None,
    origin_metadata: dict[str, Any] | None = None,
) -> None:
    """
    Create or update an item instance in the database (upsert).

    Args:
        session: Async database session
        item_instance_id: Unique identifier for the item instance
        prototype_id: Reference to item_prototypes.prototype_id
        owner_type: Type of owner (e.g., "room", "player", "container")
        owner_id: ID of the owner (optional)
        location_context: Additional location context (optional)
        quantity: Quantity of items in this instance
        condition: Item condition (optional)
        flags_override: Override flags for this instance (optional)
        binding_state: Binding state (optional)
        attunement_state: Attunement state dictionary (optional)
        custom_name: Custom name for this instance (optional)
        metadata_payload: Additional metadata dictionary (optional)
        origin_source: Origin source string (optional)
        origin_metadata: Origin metadata dictionary (optional)

    Raises:
        DatabaseError: If the insert/update fails
        ValidationError: If required parameters are invalid
    """
    if not item_instance_id:
        context = create_error_context()
        context.metadata["operation"] = "create_item_instance_async"
        log_and_raise(
            ValidationError,
            "item_instance_id is required",
            context=context,
            user_friendly="Invalid item instance data",
        )

    if not prototype_id:
        context = create_error_context()
        context.metadata["operation"] = "create_item_instance_async"
        log_and_raise(
            ValidationError,
            "prototype_id is required",
            context=context,
            user_friendly="Invalid item instance data",
        )

    context = create_error_context()
    context.metadata["operation"] = "create_item_instance_async"
    context.metadata["item_instance_id"] = item_instance_id
    context.metadata["prototype_id"] = prototype_id

    table = cast(Table, ItemInstance.__table__)
    now = datetime.now(UTC)
    # Column in DB is "metadata"; model attribute is metadata_payload
    meta_val = metadata_payload or {}
    origin_meta_val = origin_metadata or {}

    stmt = (
        insert(table)
        .values(
            item_instance_id=item_instance_id,
            prototype_id=prototype_id,
            owner_type=owner_type,
            owner_id=owner_id,
            location_context=location_context,
            quantity=quantity,
            condition=condition,
            flags_override=flags_override or [],
            binding_state=binding_state,
            attunement_state=attunement_state or {},
            custom_name=custom_name,
            metadata=meta_val,
            origin_source=origin_source,
            origin_metadata=origin_meta_val,
            created_at=now,
            updated_at=now,
        )
        .on_conflict_do_update(
            index_elements=["item_instance_id"],
            set_={
                table.c.prototype_id: prototype_id,
                table.c.owner_type: owner_type,
                table.c.owner_id: owner_id,
                table.c.location_context: location_context,
                table.c.quantity: quantity,
                table.c.condition: condition,
                table.c.flags_override: flags_override or [],
                table.c.binding_state: binding_state,
                table.c.attunement_state: attunement_state or {},
                table.c.custom_name: custom_name,
                table.c["metadata"]: meta_val,
                table.c.origin_source: origin_source,
                table.c.origin_metadata: origin_meta_val,
                table.c.updated_at: now,
            },
        )
    )

    try:
        await session.execute(stmt)
        await session.commit()
        logger.debug(
            "Item instance created or updated",
            item_instance_id=item_instance_id,
            prototype_id=prototype_id,
            owner_type=owner_type,
            owner_id=owner_id,
        )
    except SQLAlchemyError as e:
        await session.rollback()
        log_and_raise(
            DatabaseError,
            f"Database error creating item instance: {e}",
            context=context,
            details={"error": str(e), "item_instance_id": item_instance_id, "prototype_id": prototype_id},
            user_friendly="Failed to create item instance",
        )


async def item_instance_exists_async(session: AsyncSession, item_instance_id: str) -> bool:
    """
    Check if an item instance exists in the database.

    Args:
        session: Async database session
        item_instance_id: Unique identifier for the item instance

    Returns:
        True if the item instance exists, False otherwise
    """
    stmt = select(1).select_from(ItemInstance).where(ItemInstance.item_instance_id == item_instance_id).limit(1)
    result = await session.execute(stmt)
    return result.scalar_one_or_none() is not None


async def ensure_item_instance_async(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Item instance persistence requires many parameters for context and validation
    session: AsyncSession,
    item_instance_id: str,
    prototype_id: str,
    owner_type: str = "room",
    owner_id: str | None = None,
    quantity: int = 1,
    metadata_payload: dict[str, Any] | None = None,
    origin_source: str | None = None,
    origin_metadata: dict[str, Any] | None = None,
) -> None:
    """
    Ensure an item instance exists in the database, creating it if necessary.

    Args:
        session: Async database session
        item_instance_id: Unique identifier for the item instance
        prototype_id: Reference to item_prototypes.prototype_id
        owner_type: Type of owner (default: "room")
        owner_id: ID of the owner (optional)
        quantity: Quantity of items in this instance (default: 1)
        metadata_payload: Additional metadata dictionary (optional)
        origin_source: Origin source string (optional)
        origin_metadata: Origin metadata dictionary (optional)
    """
    await create_item_instance_async(
        session=session,
        item_instance_id=item_instance_id,
        prototype_id=prototype_id,
        owner_type=owner_type,
        owner_id=owner_id,
        quantity=quantity,
        metadata_payload=metadata_payload,
        origin_source=origin_source,
        origin_metadata=origin_metadata,
    )
    logger.debug(
        "Item instance ensured",
        item_instance_id=item_instance_id,
        prototype_id=prototype_id,
        quantity=quantity,
    )
