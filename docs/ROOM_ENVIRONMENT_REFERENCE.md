# Room Environment Reference

## The canonical list

`environment` is a classification carried by zones, subzones, and rooms. The canonical values live in
one place — `server/models/world.py::ROOM_ENVIRONMENTS` — and are enforced by database `CHECK`
constraints, JSON schema `enum`s, and the map editor's dropdown, all derived from that one list.

| Value | Meaning |
|---|---|
| `indoors` | Enclosed interior space |
| `outdoors` | Open-air exterior space |
| `underwater` | Submerged aquatic environment |
| `intersection` | Street or path intersection |
| `street_paved` | Paved road or street |
| `arena` | Combat arena cell (the Gladiator Ring / `limbo/arena` zone) |
| `void` | Liminal space between life and death (the `limbo/death` zone) |

`environment` may also be `NULL`/unset at any level.

## Inheritance

A room's effective environment is resolved by `server/world_loader.py::get_room_environment()` via a
priority chain:

1. Room-specific `environment` (if set)
2. Sub-zone `environment` (if set)
3. Zone `environment` (if set)
4. Default: `outdoors`

Because all three levels share the same enum, the chain is always valid — a fallback from any level to
any other level can never produce a value one level doesn't recognize.

## Where `environment` is stored

- **Zones and subzones**: typed `text` columns (`zones.environment`, `subzones.environment`), each with
  a `CHECK` constraint.
- **Rooms**: a key inside the `attributes` JSONB column (`attributes->>'environment'`), enforced by an
  expression `CHECK` constraint (`chk_rooms_environment`) rather than a column constraint. See the
  follow-up issue tracking promoting this to a typed column, matching zones/subzones.

## Adding a new environment value

1. Add the value to `ROOM_ENVIRONMENTS` in `server/models/world.py`.
2. Write a dbmate migration (`npx dbmate new <description> --migrations-dir db/migrations`,
   see `db/migrations/README.md`) that drops and re-adds all three `CHECK` constraints
   (`chk_zones_environment`, `chk_subzones_environment`, `chk_rooms_environment`) with the new
   list, then run it against `mythos_dev` with `scripts/migrate.ps1 -Environment dev`.
3. Regenerate `db/schema.sql` from `mythos_dev` (`scripts/generate_schema_from_dev.ps1`) so the
   baseline matches.
4. Update both JSON schemas (`tools/room_toolkit/room_validator/schemas/room_hierarchy_schema.json` and
   `unified_room_schema.json`) and `tools/room_toolkit/room_validator/tests/test_hierarchical_schema.py`.
5. Add the option to `ENVIRONMENT_OPTIONS` in `client/src/components/map/RoomEditModal.tsx`.
6. Run `server/tests/unit/test_room_environment_parity.py` — it fails if any of the above is missed.
