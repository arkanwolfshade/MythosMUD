-- Player bank deposit boxes (#977): the schema half.
--
-- 1. Allow containers.source_type = 'bank' (one box per player, owner_id = the player, room_id NULL;
--    created lazily by server/services/bank_service.py).
-- 2. Unique index so a get-or-create race cannot give one player two boxes.
--
-- The bank room and its banker are data: data/db/migrations/20261007120000_bank_deposit_boxes.sql, which runs
-- right after this one. Idempotent: safe to replay.

-- migrate:up
ALTER TABLE containers DROP CONSTRAINT IF EXISTS containers_source_type_check;
ALTER TABLE containers ADD CONSTRAINT containers_source_type_check
CHECK (source_type IN ('environment', 'equipment', 'corpse', 'bank'));

CREATE UNIQUE INDEX IF NOT EXISTS uq_containers_bank_owner
ON containers (owner_id) WHERE source_type = 'bank';

-- migrate:down
-- CONCURRENTLY cannot run inside dbmate's transaction, and this rollback block is never reached through
-- scripts/migrate.ps1 (it only exposes up/status), so the brief table lock is acceptable.
DROP INDEX IF EXISTS uq_containers_bank_owner; -- noqa: PG01

-- Deliberately no DELETE of bank containers: re-adding the narrower CHECK below fails while any
-- player still has a box, so a rollback can never silently destroy deposited items.
ALTER TABLE containers DROP CONSTRAINT IF EXISTS containers_source_type_check;
ALTER TABLE containers ADD CONSTRAINT containers_source_type_check
CHECK (source_type IN ('environment', 'equipment', 'corpse'));
