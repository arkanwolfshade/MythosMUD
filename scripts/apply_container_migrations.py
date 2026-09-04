"""
Apply container schema normalization migrations to mythos_dev database.

This script applies:
1. normalize_container_schema - Creates container_contents table and migrates data
2. remove_items_json_column - Removes items_json column from containers table
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# Add server directory to path
project_root = Path(__file__).parent.parent
server_dir = project_root / "server"
sys.path.insert(0, str(project_root))

import psycopg2  # noqa: E402
from dotenv import load_dotenv  # noqa: E402

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    print("[ERROR] DATABASE_URL not found in environment variables")
    sys.exit(1)

# Extract connection info from DATABASE_URL
# Format: postgresql+asyncpg://user:password@host:port/database
url_parts = DATABASE_URL.replace("postgresql+asyncpg://", "").split("@")
if len(url_parts) != 2:
    print("[ERROR] Invalid DATABASE_URL format")
    sys.exit(1)

user_pass = url_parts[0].split(":")
host_port_db = url_parts[1].split("/")
if len(user_pass) != 2 or len(host_port_db) != 2:
    print("[ERROR] Invalid DATABASE_URL format")
    sys.exit(1)

user = user_pass[0]
password = user_pass[1]
host_port = host_port_db[0].split(":")
host = host_port[0]
port = int(host_port[1]) if len(host_port) > 1 else 5432
database = host_port_db[1]

print("=== MythosMUD Container Schema Migration ===")
print(f"Database: {database}")
print(f"Host: {host}:{port}")
print()

# Connect to database
try:
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password,
    )
    conn.autocommit = False
    print("[OK] Connected to database")
except Exception as e:
    print(f"[ERROR] Failed to connect to database: {e}")
    sys.exit(1)

try:
    cursor = conn.cursor()

    # Check if migrations have already been applied
    cursor.execute("""
        SELECT EXISTS (
            SELECT 1 FROM information_schema.tables
            WHERE table_schema = 'public'
            AND table_name = 'container_contents'
        )
    """)
    container_contents_exists = cursor.fetchone()[0]

    cursor.execute("""
        SELECT EXISTS (
            SELECT 1 FROM information_schema.columns
            WHERE table_schema = 'public'
            AND table_name = 'containers'
            AND column_name = 'items_json'
        )
    """)
    items_json_exists = cursor.fetchone()[0]

    if container_contents_exists and not items_json_exists:
        print("[OK] Migrations appear to already be applied")
        print("  - container_contents table exists")
        print("  - items_json column removed")
        conn.rollback()
        conn.close()
        sys.exit(0)

    # Apply first migration: normalize_container_schema
    if not container_contents_exists:
        print("Applying migration: normalize_container_schema...")
        print("  - Creating container_contents table")
        print("  - Adding container_item_instance_id column")
        print("  - Creating stored procedures")
        print("  - Migrating data from items_json to container_contents")

        # Execute the SQL statements directly
        print("  Executing migration SQL...")

        # Step 1: Add container_item_instance_id
        cursor.execute("""
            ALTER TABLE containers
            ADD COLUMN IF NOT EXISTS container_item_instance_id VARCHAR(64);
        """)
        print("    [OK] Added container_item_instance_id column")

        # Step 2: Add foreign key
        cursor.execute("""
            DO $$
            BEGIN
                IF NOT EXISTS (
                    SELECT 1 FROM pg_constraint
                    WHERE conname = 'fk_containers_container_item_instance'
                ) THEN
                    ALTER TABLE containers
                    ADD CONSTRAINT fk_containers_container_item_instance
                    FOREIGN KEY (container_item_instance_id)
                    REFERENCES item_instances(item_instance_id)
                    ON DELETE SET NULL;
                END IF;
            END $$;
        """)
        print("    [OK] Added foreign key constraint")

        # Step 3: Add index
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS ix_containers_container_item_instance_id
            ON containers(container_item_instance_id);
        """)
        print("    [OK] Added index")

        # Step 4: Create container_contents table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS container_contents (
                container_id UUID NOT NULL,
                item_instance_id VARCHAR(64) NOT NULL,
                position INTEGER NOT NULL DEFAULT 0,
                created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
                updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
                PRIMARY KEY (container_id, item_instance_id),
                FOREIGN KEY (container_id) REFERENCES containers(container_instance_id) ON DELETE CASCADE,
                FOREIGN KEY (item_instance_id) REFERENCES item_instances(item_instance_id) ON DELETE CASCADE
            );
        """)
        print("    [OK] Created container_contents table")

        # Step 5: Create indexes
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS ix_container_contents_container_id
            ON container_contents(container_id);
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS ix_container_contents_item_instance_id
            ON container_contents(item_instance_id);
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS ix_container_contents_position
            ON container_contents(container_id, position);
        """)
        print("    [OK] Created indexes")

        # Step 6: Create stored procedures
        print("    Creating stored procedures...")

        # get_container_contents_json
        cursor.execute("""
            CREATE OR REPLACE FUNCTION get_container_contents_json(p_container_id UUID)
            RETURNS JSONB AS $$
            DECLARE
                v_result JSONB;
            BEGIN
                SELECT COALESCE(
                    jsonb_agg(
                        jsonb_build_object(
                            'item_instance_id', cc.item_instance_id,
                            'item_id', ii.prototype_id,
                            'item_name', COALESCE(ii.custom_name, ip.name),
                            'quantity', ii.quantity,
                            'condition', ii.condition,
                            'metadata', ii.metadata,
                            'position', cc.position
                        )
                        ORDER BY cc.position
                    ),
                    '[]'::jsonb
                )
                INTO v_result
                FROM container_contents cc
                JOIN item_instances ii ON cc.item_instance_id = ii.item_instance_id
                JOIN item_prototypes ip ON ii.prototype_id = ip.prototype_id
                WHERE cc.container_id = p_container_id;

                RETURN v_result;
            END;
            $$ LANGUAGE plpgsql;
        """)
        print("      [OK] get_container_contents_json")

        # add_item_to_container
        cursor.execute("""
            CREATE OR REPLACE FUNCTION add_item_to_container(
                p_container_id UUID,
                p_item_instance_id VARCHAR(64),
                p_position INTEGER DEFAULT NULL
            )
            RETURNS VOID AS $$
            DECLARE
                v_max_position INTEGER;
            BEGIN
                IF p_position IS NULL THEN
                    SELECT COALESCE(MAX(position), -1) + 1
                    INTO v_max_position
                    FROM container_contents
                    WHERE container_id = p_container_id;
                ELSE
                    v_max_position := p_position;
                END IF;

                INSERT INTO container_contents (container_id, item_instance_id, position)
                VALUES (p_container_id, p_item_instance_id, v_max_position)
                ON CONFLICT (container_id, item_instance_id)
                DO UPDATE SET position = v_max_position, updated_at = NOW();
            END;
            $$ LANGUAGE plpgsql;
        """)
        print("      [OK] add_item_to_container")

        # remove_item_from_container
        cursor.execute("""
            CREATE OR REPLACE FUNCTION remove_item_from_container(
                p_container_id UUID,
                p_item_instance_id VARCHAR(64)
            )
            RETURNS BOOLEAN AS $$
            DECLARE
                v_deleted INTEGER;
            BEGIN
                DELETE FROM container_contents
                WHERE container_id = p_container_id
                  AND item_instance_id = p_item_instance_id;

                GET DIAGNOSTICS v_deleted = ROW_COUNT;
                RETURN v_deleted > 0;
            END;
            $$ LANGUAGE plpgsql;
        """)
        print("      [OK] remove_item_from_container")

        # clear_container_contents
        cursor.execute("""
            CREATE OR REPLACE FUNCTION clear_container_contents(p_container_id UUID)
            RETURNS INTEGER AS $$
            DECLARE
                v_deleted INTEGER;
            BEGIN
                DELETE FROM container_contents
                WHERE container_id = p_container_id;

                GET DIAGNOSTICS v_deleted = ROW_COUNT;
                RETURN v_deleted;
            END;
            $$ LANGUAGE plpgsql;
        """)
        print("      [OK] clear_container_contents")

        # Step 7: Migrate data
        print("    Migrating data from items_json to container_contents...")
        cursor.execute("""
            DO $$
            DECLARE
                v_container RECORD;
                v_item JSONB;
                v_item_instance_id VARCHAR(64);
                v_position INTEGER := 0;
                v_item_exists BOOLEAN;
            BEGIN
                FOR v_container IN
                    SELECT container_instance_id, items_json
                    FROM containers
                    WHERE items_json IS NOT NULL
                      AND jsonb_array_length(items_json) > 0
                LOOP
                    v_position := 0;

                    FOR v_item IN SELECT * FROM jsonb_array_elements(v_container.items_json)
                    LOOP
                        v_item_instance_id := COALESCE(
                            v_item->>'item_instance_id',
                            v_item->>'item_id',
                            NULL
                        );

                        IF v_item_instance_id IS NULL THEN
                            CONTINUE;
                        END IF;

                        SELECT EXISTS(
                            SELECT 1 FROM item_instances
                            WHERE item_instance_id = v_item_instance_id
                        ) INTO v_item_exists;

                        IF NOT v_item_exists THEN
                            INSERT INTO item_instances (
                                item_instance_id,
                                prototype_id,
                                owner_type,
                                quantity,
                                metadata
                            )
                            VALUES (
                                v_item_instance_id,
                                COALESCE(v_item->>'item_id', v_item->>'prototype_id', 'unknown'),
                                'container',
                                COALESCE((v_item->>'quantity')::INTEGER, 1),
                                COALESCE(v_item->'metadata', '{}'::jsonb)
                            )
                            ON CONFLICT (item_instance_id) DO NOTHING;
                        END IF;

                        INSERT INTO container_contents (container_id, item_instance_id, position)
                        VALUES (v_container.container_instance_id, v_item_instance_id, v_position)
                        ON CONFLICT (container_id, item_instance_id) DO NOTHING;

                        v_position := v_position + 1;
                    END LOOP;
                END LOOP;
            END;
            $$;
        """)
        print("    [OK] Data migration completed")

        conn.commit()
        print("[OK] Migration normalize_container_schema applied successfully")
    else:
        print("[OK] Migration normalize_container_schema already applied")

    # Apply second migration: remove_items_json_column
    if items_json_exists:
        print()
        print("Applying migration: remove_items_json_column...")
        print("  - Removing items_json column from containers table")

        cursor.execute("ALTER TABLE containers DROP COLUMN IF EXISTS items_json;")
        conn.commit()
        print("[OK] Migration remove_items_json_column applied successfully")
    else:
        print("[OK] Migration remove_items_json_column already applied")

    print()
    print("=== Migration Complete ===")
    print("[OK] All migrations applied successfully")

except Exception as e:
    conn.rollback()
    print(f"[ERROR] Migration failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
finally:
    conn.close()
