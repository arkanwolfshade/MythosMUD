-- PostgreSQL: add constraint so NPC names do not end with hyphen-number
-- (e.g. 'rat-1', 'dr-2') so the system can use that pattern for disambiguation.
-- Replaces legacy SQLite script; uses PostgreSQL regex and timestamptz.
-- Reference: .cursor/rules/postgresql.mdc
set client_min_messages = warning;
set search_path = public;

-- Optional: list existing rows that would violate the constraint (run before add)
-- select name from npc_definitions where name ~ '.*-[0-9]+$';

alter table npc_definitions
    drop constraint if exists npc_definitions_name_no_disambiguation_suffix;

alter table npc_definitions
    add constraint npc_definitions_name_no_disambiguation_suffix
    check (name !~ '.*-[0-9]+$');
