#!/usr/bin/env python3
"""
Verify that the players table migration was successful and all data is correct.
Checks:
1. Table schema matches expected structure
2. JSON data in stats column is valid
3. All required columns exist
4. Data integrity checks
"""

import asyncio
import json
import os
import sys

import asyncpg

# Database connection parameters
# WARNING: In production, always use environment variables for passwords
# The default password is for local development only
DEFAULT_HOST = os.getenv("DATABASE_HOST", "localhost")
DEFAULT_PORT = int(os.getenv("DATABASE_PORT", "5432"))
DEFAULT_USER = os.getenv("DATABASE_USER", "postgres")
# nosemgrep: python.lang.security.audit.hardcoded-password.hardcoded-password
# nosec B105: Default password for development/seed data only (not used in production)
DEFAULT_PASSWORD = os.getenv("DATABASE_PASSWORD", "Cthulhu1")

# Warn if using default password in production-like environments
if DEFAULT_PASSWORD == "Cthulhu1" and os.getenv("ENVIRONMENT") in ("production", "staging"):
    print(
        "WARNING: Using default password in production/staging environment! Set DATABASE_PASSWORD environment variable."
    )

DATABASES = ["mythos_dev", "mythos_unit", "mythos_e2e"]

# Expected columns from SQLAlchemy model
EXPECTED_COLUMNS = {
    "player_id": "varchar",
    "user_id": "uuid",
    "name": "varchar",
    "stats": "text",
    "inventory": "text",
    "status_effects": "text",
    "current_room_id": "varchar",
    "respawn_room_id": "varchar",
    "experience_points": "integer",
    "level": "integer",
    "is_admin": "integer",
    "profession_id": "integer",
    "created_at": "timestamp with time zone",
    "last_active": "timestamp with time zone",
}

# Expected stats JSON structure
EXPECTED_STATS_KEYS = {
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
    "lucidity",
    "occult_knowledge",
    "fear",
    "corruption",
    "cult_affiliation",
    "current_dp",
    "position",
}


async def verify_database(db_name: str, host: str, port: int, user: str, password: str) -> bool:
    """Verify a single database."""
    print(f"\n{'=' * 60}")
    print(f"Verifying database: {db_name}")
    print(f"{'=' * 60}")

    try:
        conn = await asyncpg.connect(host=host, port=port, user=user, password=password, database=db_name)

        try:
            # 1. Check if players table exists
            table_exists = await conn.fetchval("""
                SELECT EXISTS (
                    SELECT 1 FROM information_schema.tables
                    WHERE table_schema = 'public' AND table_name = 'players'
                )
            """)

            if not table_exists:
                print(f"[ERROR] Players table does not exist in {db_name}")
                return False

            print("[OK] Players table exists")

            # 2. Check table schema
            columns = await conn.fetch("""
                SELECT column_name, data_type, is_nullable, column_default
                FROM information_schema.columns
                WHERE table_schema = 'public' AND table_name = 'players'
                ORDER BY ordinal_position
            """)

            print(f"\n[INFO] Table schema ({len(columns)} columns):")
            schema_ok = True
            found_columns = {}

            for col in columns:
                col_name = col["column_name"]
                col_type = col["data_type"]
                nullable = col["is_nullable"]

                found_columns[col_name] = col_type

                # Check if column matches expected
                if col_name in EXPECTED_COLUMNS:
                    expected_type = EXPECTED_COLUMNS[col_name]
                    # Type matching is flexible (varchar vs character varying, etc.)
                    type_match = (
                        expected_type in col_type
                        or col_type in expected_type
                        or (expected_type == "varchar" and "character varying" in col_type)
                        or (expected_type == "integer" and col_type in ("integer", "bigint", "smallint"))
                    )

                    if not type_match:
                        print(f"  [WARN] {col_name}: type mismatch (expected {expected_type}, got {col_type})")
                        schema_ok = False
                    else:
                        print(f"  [OK] {col_name}: {col_type} (nullable: {nullable})")
                else:
                    print(f"  [INFO] {col_name}: {col_type} (extra column)")

            # Check for missing columns
            missing_columns = set(EXPECTED_COLUMNS.keys()) - set(found_columns.keys())
            if missing_columns:
                print(f"\n[ERROR] Missing columns: {missing_columns}")
                schema_ok = False
            else:
                print("\n[OK] All expected columns present")

            # 3. Check for old schema columns (should not exist)
            old_columns = ["id"]  # Old primary key
            for old_col in old_columns:
                if old_col in found_columns:
                    print(f"\n[ERROR] Old schema column still exists: {old_col}")
                    schema_ok = False

            if "id" not in found_columns:
                print("[OK] Old 'id' column removed (migration successful)")

            # 4. Check row count
            row_count = await conn.fetchval("SELECT COUNT(*) FROM players")
            print(f"\n[INFO] Total players: {row_count}")

            json_errors = []
            stats_errors = []

            if row_count == 0:
                print("[WARN] No players in table (may be expected for test databases)")
            else:
                # 5. Verify JSON data integrity
                print("\n[INFO] Verifying JSON data integrity...")
                players = await conn.fetch("""
                    SELECT player_id, name, stats, inventory, status_effects
                    FROM players
                    LIMIT 100
                """)

                for player in players:
                    player_id = player["player_id"]
                    name = player["name"]
                    stats = player["stats"]
                    inventory = player["inventory"]
                    status_effects = player["status_effects"]

                    # Check stats JSON
                    try:
                        stats_json = json.loads(stats) if stats else {}
                        if not isinstance(stats_json, dict):
                            json_errors.append(f"{name} ({player_id}): stats is not a JSON object")
                        else:
                            # Check for expected keys
                            missing_keys = EXPECTED_STATS_KEYS - set(stats_json.keys())
                            if missing_keys:
                                stats_errors.append(f"{name} ({player_id}): missing stats keys: {missing_keys}")
                    except json.JSONDecodeError as e:
                        json_errors.append(f"{name} ({player_id}): invalid stats JSON: {e}")

                    # Check inventory JSON
                    try:
                        inventory_json = json.loads(inventory) if inventory else []
                        if not isinstance(inventory_json, list):
                            json_errors.append(f"{name} ({player_id}): inventory is not a JSON array")
                    except json.JSONDecodeError as e:
                        json_errors.append(f"{name} ({player_id}): invalid inventory JSON: {e}")

                    # Check status_effects JSON
                    try:
                        effects_json = json.loads(status_effects) if status_effects else []
                        if not isinstance(effects_json, list):
                            json_errors.append(f"{name} ({player_id}): status_effects is not a JSON array")
                    except json.JSONDecodeError as e:
                        json_errors.append(f"{name} ({player_id}): invalid status_effects JSON: {e}")

                if json_errors:
                    print(f"\n[ERROR] JSON parsing errors ({len(json_errors)}):")
                    for error in json_errors[:10]:  # Show first 10
                        print(f"  - {error}")
                    if len(json_errors) > 10:
                        print(f"  ... and {len(json_errors) - 10} more")
                else:
                    print("[OK] All JSON data is valid")

                if stats_errors:
                    print(f"\n[WARN] Stats structure issues ({len(stats_errors)}):")
                    for error in stats_errors[:10]:  # Show first 10
                        print(f"  - {error}")
                    if len(stats_errors) > 10:
                        print(f"  ... and {len(stats_errors) - 10} more")
                else:
                    print("[OK] All stats have expected structure")

                # 6. Check for NULL values in required fields
                null_checks = await conn.fetch("""
                    SELECT
                        COUNT(*) FILTER (WHERE player_id IS NULL) as null_player_id,
                        COUNT(*) FILTER (WHERE user_id IS NULL) as null_user_id,
                        COUNT(*) FILTER (WHERE name IS NULL) as null_name,
                        COUNT(*) FILTER (WHERE stats IS NULL) as null_stats,
                        COUNT(*) FILTER (WHERE inventory IS NULL) as null_inventory,
                        COUNT(*) FILTER (WHERE status_effects IS NULL) as null_status_effects,
                        COUNT(*) FILTER (WHERE current_room_id IS NULL) as null_current_room_id
                    FROM players
                """)

                null_issues = []
                for check in null_checks:
                    for key, value in check.items():
                        if value > 0:
                            null_issues.append(f"{key}: {value} rows")

                if null_issues:
                    print("\n[WARN] NULL values in required fields:")
                    for issue in null_issues:
                        print(f"  - {issue}")
                else:
                    print("[OK] No NULL values in required fields")

                # 7. Sample data check
                sample = await conn.fetchrow("""
                    SELECT player_id, name, stats, current_room_id, level, experience_points
                    FROM players
                    LIMIT 1
                """)

                if sample:
                    print("\n[INFO] Sample player data:")
                    print(f"  player_id: {sample['player_id']}")
                    print(f"  name: {sample['name']}")
                    print(f"  current_room_id: {sample['current_room_id']}")
                    print(f"  level: {sample['level']}")
                    print(f"  experience_points: {sample['experience_points']}")
                    try:
                        stats_sample = json.loads(sample["stats"])
                        print(f"  stats keys: {list(stats_sample.keys())[:5]}...")
                    except json.JSONDecodeError:
                        # Catch JSON parsing errors when stats column contains invalid JSON
                        print(f"  stats: {sample['stats'][:50]}...")

            # 8. Check foreign key constraints
            fk_constraints = await conn.fetch("""
                SELECT
                    tc.constraint_name,
                    kcu.column_name,
                    ccu.table_name AS foreign_table_name,
                    ccu.column_name AS foreign_column_name
                FROM information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu
                    ON tc.constraint_name = kcu.constraint_name
                JOIN information_schema.constraint_column_usage AS ccu
                    ON ccu.constraint_name = tc.constraint_name
                WHERE tc.constraint_type = 'FOREIGN KEY'
                    AND tc.table_name = 'players'
            """)

            if fk_constraints:
                print(f"\n[INFO] Foreign key constraints ({len(fk_constraints)}):")
                for fk in fk_constraints:
                    print(f"  {fk['column_name']} -> {fk['foreign_table_name']}.{fk['foreign_column_name']}")
            else:
                print("\n[WARN] No foreign key constraints found")

            # Summary
            print(f"\n{'=' * 60}")
            if schema_ok and not json_errors:
                print(f"[SUCCESS] Database {db_name} verification passed")
                return True
            else:
                print(f"[WARNING] Database {db_name} has issues (see above)")
                return False

        finally:
            await conn.close()

    except asyncpg.PostgresError as e:
        # Catch all asyncpg database errors (connection errors, query errors, etc.)
        print(f"[ERROR] Failed to verify {db_name}: {e}")
        import traceback

        traceback.print_exc()
        return False


async def main():
    """Main function."""
    import argparse

    parser = argparse.ArgumentParser(description="Verify players table migration")
    parser.add_argument(
        "--database", "-d", default="all", help="Database to verify (mythos_dev, mythos_unit, mythos_e2e, or 'all')"
    )
    parser.add_argument("--host", default=DEFAULT_HOST, help="PostgreSQL host")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="PostgreSQL port")
    parser.add_argument("--user", "-U", default=DEFAULT_USER, help="PostgreSQL user")
    parser.add_argument("--password", "-P", default=DEFAULT_PASSWORD, help="PostgreSQL password")

    args = parser.parse_args()

    # Determine which databases to verify
    if args.database.lower() == "all":
        databases = DATABASES
    else:
        databases = [args.database]

    # Verify each database
    all_passed = True
    for db in databases:
        result = await verify_database(db, args.host, args.port, args.user, args.password)
        if not result:
            all_passed = False

    print(f"\n{'=' * 60}")
    if all_passed:
        print("[SUCCESS] All databases verified successfully!")
        return 0
    else:
        print("[WARNING] Some databases have issues")
        return 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
