-- Verification checks for users and players (PostgreSQL).
-- Aligns with public.users and public.players; no staging tables.
-- Reference: .cursor/rules/postgresql.mdc
set client_min_messages = warning;
set search_path = public;

-- Row counts for live tables only
select
    (select count(*) as cnt from users) as users_count,
    (select count(*) as cnt from players) as players_count,
    (select count(*) as cnt from id_map_users) as id_map_users_count,
    (select count(*) as cnt from id_map_players) as id_map_players_count;

-- Players without matching users (should be zero)
select
    count(*) as players_without_users
from
    players as p
left join
    users as u
    on u.id = p.user_id
where
    u.id is null;

-- Sample users (explicit columns)
select
    u.id,
    u.username,
    u.is_admin,
    u.created_at
from
    users as u
order by
    u.created_at
limit 5;

-- Sample players (explicit columns; stats is jsonb)
select
    p.player_id,
    p.name,
    p.created_at
from
    players as p
order by
    p.created_at
limit 5;
