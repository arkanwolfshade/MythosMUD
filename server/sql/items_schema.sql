PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS item_component_states;
DROP TABLE IF EXISTS item_instances;
DROP TABLE IF EXISTS item_prototypes;

CREATE TABLE item_prototypes (
    prototype_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    short_description TEXT NOT NULL,
    long_description TEXT NOT NULL,
    item_type TEXT NOT NULL,
    weight REAL NOT NULL DEFAULT 0,
    base_value INTEGER NOT NULL DEFAULT 0,
    durability INTEGER,
    flags JSON NOT NULL DEFAULT '[]',
    wear_slots JSON NOT NULL DEFAULT '[]',
    stacking_rules JSON NOT NULL DEFAULT '{}',
    usage_restrictions JSON NOT NULL DEFAULT '{}',
    effect_components JSON NOT NULL DEFAULT '[]',
    metadata JSON NOT NULL DEFAULT '{}',
    tags JSON NOT NULL DEFAULT '[]',
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE item_instances (
    item_instance_id TEXT PRIMARY KEY,
    prototype_id TEXT NOT NULL,
    owner_type TEXT NOT NULL DEFAULT 'room',
    owner_id TEXT,
    location_context TEXT,
    quantity INTEGER NOT NULL DEFAULT 1,
    condition INTEGER,
    flags_override JSON NOT NULL DEFAULT '[]',
    binding_state TEXT,
    attunement_state JSON NOT NULL DEFAULT '{}',
    custom_name TEXT,
    metadata JSON NOT NULL DEFAULT '{}',
    origin_source TEXT,
    origin_metadata JSON NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (prototype_id) REFERENCES item_prototypes(prototype_id) ON DELETE CASCADE
);

CREATE INDEX ix_item_instances_owner ON item_instances(owner_type, owner_id);
CREATE INDEX ix_item_instances_prototype_id ON item_instances(prototype_id);

CREATE TABLE item_component_states (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_instance_id TEXT NOT NULL,
    component_id TEXT NOT NULL,
    state_payload JSON NOT NULL DEFAULT '{}',
    updated_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (item_instance_id) REFERENCES item_instances(item_instance_id) ON DELETE CASCADE
);

CREATE UNIQUE INDEX ix_component_states_instance_component
    ON item_component_states(item_instance_id, component_id);
