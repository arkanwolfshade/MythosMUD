from __future__ import annotations

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from server.models.base import Base
from server.models.item import ItemComponentState, ItemInstance, ItemPrototype


def build_engine():
    import os

    database_url = os.getenv("DATABASE_URL")
    if not database_url or not database_url.startswith("postgresql"):
        raise ValueError("DATABASE_URL must be set to a PostgreSQL URL. SQLite is no longer supported.")
    # Convert async URL to sync URL for create_engine
    sync_url = database_url.replace("+asyncpg", "")
    engine = create_engine(sync_url, future=True)
    # PostgreSQL always enforces foreign keys - no PRAGMA needed
    return engine


def test_item_models_persist_and_cascade():
    engine = build_engine()
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        prototype = ItemPrototype(
            prototype_id="equipment.test.phantasmal_visor",
            name="Phantasmal Visor",
            short_description="a visor shimmering with iridescent film",
            long_description="A training prototype that helps investigators acclimate to non-euclidean vistas.",
            item_type="equipment",
            weight=0.8,
            base_value=320,
            durability=50,
            flags=["MAGICAL"],
            wear_slots=["head"],
            stacking_rules={"max_stack": 1},
            usage_restrictions={"profession": ["trainee"]},
            effect_components=["component.sanity_guard"],
            metadata_payload={"lore": "Fabricated in the Sanitarium test lab"},
            tags=["equipment", "head"],
        )
        session.add(prototype)
        session.commit()

        instance = ItemInstance(
            item_instance_id="instance-001",
            prototype_id=prototype.prototype_id,
            owner_type="player",
            owner_id="player-001",
            location_context="inventory",
            quantity=1,
            condition=45,
            flags_override=["MAGICAL"],
            attunement_state={"status": "unbound"},
            metadata_payload={"note": "Loaner gear"},
        )
        instance.apply_flag("BLESSED")

        component_state = ItemComponentState(
            component_id="component.sanity_guard",
            state_payload={"charges": 3},
        )
        instance.component_states.append(component_state)

        session.add(instance)
        session.commit()

        refreshed_instance = session.get(ItemInstance, "instance-001")
        assert refreshed_instance is not None
        assert refreshed_instance.prototype.name == "Phantasmal Visor"
        assert "BLESSED" in refreshed_instance.flags_override
        assert refreshed_instance.component_states[0].state_payload["charges"] == 3

        # Cascading delete should remove instance and component state.
        session.delete(prototype)
        session.commit()

        remaining_instances = session.execute(
            select(ItemInstance).where(ItemInstance.item_instance_id == "instance-001")
        ).all()
        assert not remaining_instances

        remaining_components = session.execute(select(ItemComponentState)).all()
        assert not remaining_components
