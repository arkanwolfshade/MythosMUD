-- Raise the global container capacity ceiling from 20 to 200 slots (each container's real size comes from its
-- prototype; see MAX_CONTAINER_CAPACITY_SLOTS in server/models/container.py).
--
-- DDL half of the tutorial bedroom / lost-and-found chest change; the data half is
-- data/db/migrations/20261002150000_tutorial_bedroom_fixtures.sql and runs right after this one.
-- Idempotent: safe to replay.

-- migrate:up
ALTER TABLE containers DROP CONSTRAINT IF EXISTS containers_capacity_slots_check;
ALTER TABLE containers ADD CONSTRAINT containers_capacity_slots_check
CHECK (capacity_slots > 0 AND capacity_slots <= 200);

-- migrate:down
ALTER TABLE containers DROP CONSTRAINT IF EXISTS containers_capacity_slots_check;
ALTER TABLE containers ADD CONSTRAINT containers_capacity_slots_check
CHECK (capacity_slots > 0 AND capacity_slots <= 20);
