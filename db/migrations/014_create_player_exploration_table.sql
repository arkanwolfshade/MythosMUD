-- Migration 014: Create player_exploration table
-- Date: 2025-01-XX
-- Description: Create player_exploration junction table to track which rooms each player has explored
-- This table enables the map viewer to show only explored rooms to players
-- Status: ✅ ACTIVE

SET client_min_messages = WARNING;
SET search_path = public;

BEGIN;

-- Create player_exploration table if it doesn't exist
CREATE TABLE IF NOT EXISTS public.player_exploration (
    id UUID NOT NULL DEFAULT gen_random_uuid(),
    player_id UUID NOT NULL,
    room_id UUID NOT NULL,
    explored_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    CONSTRAINT player_exploration_pkey PRIMARY KEY (id),
    CONSTRAINT player_exploration_player_room_unique UNIQUE (player_id, room_id)
);

-- Add foreign key constraints
DO $$
BEGIN
    -- Add foreign key to players table if it doesn't exist
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_schema = 'public'
            AND table_name = 'player_exploration'
            AND constraint_name = 'player_exploration_player_id_fkey'
    ) THEN
        ALTER TABLE public.player_exploration
        ADD CONSTRAINT player_exploration_player_id_fkey
        FOREIGN KEY (player_id) REFERENCES public.players(player_id)
        ON DELETE CASCADE;

        RAISE NOTICE 'Added foreign key constraint player_exploration_player_id_fkey';
    ELSE
        RAISE NOTICE 'Foreign key constraint player_exploration_player_id_fkey already exists';
    END IF;

    -- Add foreign key to rooms table if it doesn't exist
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_schema = 'public'
            AND table_name = 'player_exploration'
            AND constraint_name = 'player_exploration_room_id_fkey'
    ) THEN
        ALTER TABLE public.player_exploration
        ADD CONSTRAINT player_exploration_room_id_fkey
        FOREIGN KEY (room_id) REFERENCES public.rooms(id)
        ON DELETE CASCADE;

        RAISE NOTICE 'Added foreign key constraint player_exploration_room_id_fkey';
    ELSE
        RAISE NOTICE 'Foreign key constraint player_exploration_room_id_fkey already exists';
    END IF;
END $$;

-- Create indexes for efficient lookups
CREATE INDEX IF NOT EXISTS idx_player_exploration_player_id
ON public.player_exploration(player_id);

CREATE INDEX IF NOT EXISTS idx_player_exploration_room_id
ON public.player_exploration(room_id);

CREATE INDEX IF NOT EXISTS idx_player_exploration_explored_at
ON public.player_exploration(explored_at);

-- Add comments
COMMENT ON TABLE public.player_exploration IS
    'Junction table tracking which rooms each player has explored. Used for map visibility filtering.';

COMMENT ON COLUMN public.player_exploration.id IS
    'Primary key (UUID)';

COMMENT ON COLUMN public.player_exploration.player_id IS
    'Foreign key to players table';

COMMENT ON COLUMN public.player_exploration.room_id IS
    'Foreign key to rooms table';

COMMENT ON COLUMN public.player_exploration.explored_at IS
    'Timestamp when the room was first explored by the player';

COMMENT ON INDEX idx_player_exploration_player_id IS
    'Index for fast lookups of all explored rooms for a specific player';

COMMENT ON INDEX idx_player_exploration_room_id IS
    'Index for reverse lookups of all players who have explored a specific room';

COMMENT ON INDEX idx_player_exploration_explored_at IS
    'Index for queries filtering by exploration time';

COMMIT;
