-- Create Professions Table DDL Script
-- This script creates the professions table and related indexes for the profession system
-- Create the professions table
create table if not exists professions (
    id bigint generated always as identity primary key,
    name text not null unique,
    description text not null,
    flavor_text text not null,
    stat_requirements text not null,
    -- JSON: {"strength": 12, "intelligence": 50}
    mechanical_effects text not null,
    -- JSON: future bonuses/penalties
    is_available boolean not null default true
);
-- Create index for efficient filtering by availability
create index if not exists idx_professions_available on professions(is_available);
-- Insert MVP professions (Tramp and Gutter Rat)
-- Note: Since id is now identity, we need to use OVERRIDING SYSTEM VALUE
insert into professions (
        id,
        name,
        description,
        flavor_text,
        stat_requirements,
        mechanical_effects
    )
overriding system value
values (
        0,
        'Tramp',
        'A wandering soul with no fixed abode',
        'You have learned to survive on the streets, finding shelter where you can and making do with what you have.',
        '{}',
        '{}'
    ),
    (
        1,
        'Gutter Rat',
        'A street-smart survivor of the urban underbelly',
        'You know the hidden passages and dark corners of the city, where others fear to tread.',
        '{}',
        '{}'
    );
-- Add profession_id column to players table
alter table players
add column if not exists profession_id bigint not null default 0;
-- Add foreign key constraint after seeding professions
do $$
begin
    if not exists (
        select 1
        from information_schema.table_constraints
        where constraint_name = 'fk_players_profession'
        and table_name = 'players'
    ) then
        alter table players
        add constraint fk_players_profession foreign key (profession_id) references professions(id);
    end if;
end $$;
-- Create index on players.profession_id for efficient lookups
create index if not exists idx_players_profession_id on players(profession_id);
