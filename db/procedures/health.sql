-- Apply with: psql -d <db> -v schema_name=<schema> -f health.sql

CREATE OR REPLACE FUNCTION :schema_name.update_player_health(p_player_id UUID, p_delta INT) -- noqa: PRS
RETURNS VOID
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE players
    SET stats = jsonb_set(
        stats,
        '{current_dp}',
        (
            GREATEST(
                0,
                LEAST(
                    GREATEST(
                        COALESCE(
                            (stats->>'max_dp')::int,
                            ((COALESCE((stats->>'constitution')::int, 50)
                              + COALESCE((stats->>'size')::int, 50)) / 5)
                        ),
                        20
                    ),
                    (stats->>'current_dp')::int + p_delta
                )
            )
        )::text::jsonb
    )
    WHERE player_id = p_player_id;
END;
$$;
