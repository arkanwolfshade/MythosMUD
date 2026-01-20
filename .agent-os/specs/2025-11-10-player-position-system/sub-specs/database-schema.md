# Database Schema

This is the database schema implementation for the spec detailed in @.agent-os/specs/2025-11-10-player-position-system/spec.md

## Changes

No new table columns required; leverage the existing player stats JSON field to store a `position` key with values
  (`standing`, `sitting`, `lying`).

- Ensure stats blobs default to `'standing'` when the key is absent and backfill existing records accordingly.

## Specifications

SQLite Migration:

  ```sql
  UPDATE players
  SET stats = json_set(COALESCE(stats, '{}'), '$.position', 'standing')
  WHERE json_extract(stats, '$.position') IS NULL;
  ```

- Maintain parity for PostgreSQL by mirroring JSON updates when the migration layer is prepared.

- Update ORM models (SQLAlchemy) and data accessors to treat `stats["position"]` as the canonical persisted value with

  enum validation handled in application logic.

## Rationale

Consolidating posture into the stats JSON avoids schema churn while still persisting state for reconnects.

- Defaulting to `'standing'` preserves legacy behavior and maintains compatibility with clients unaware of the new key.
