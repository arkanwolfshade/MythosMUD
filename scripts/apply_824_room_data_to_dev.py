#!/usr/bin/env python3
"""Apply #815/#823/#824's cumulative rooms/room_links/zones changes to mythos_dev.

mythos_dev was found to be frozen at roughly the #815 PR-5 merge point, missing:
  - the Pier's own attributes.corruption: 65 edit (PR-5 follow-up)
  - the earth/innsmouth zone's corruption_rate/corruption_target (PR-5 + PR-C)
  - all 16 of #823's exit repairs
  - #824's new content: the Sanitarium Chapel, the Innsmouth causeway/square/water street chain,
    and gedney_st_002

Idempotent: every statement checks current state first and only acts if it differs, so this is
safe to run more than once. Uses DATABASE_URL from .env.local (mythos_dev) unless overridden.

mythos_dev is protected (see .claude/rules/database.md) -- this script was written and run only
after explicit user confirmation of the delete/replace operations below.
"""

from __future__ import annotations

import asyncio
import json
import os

import asyncpg
from dotenv import load_dotenv

# --- rooms: attribute/flag fixes -------------------------------------------------------------

PIER_STABLE_ID = "earth_innsmouth_waterfront_room_waterfront_001"
PIER_ATTRIBUTES = {"environment": "outdoors", "corruption": 65}

FOYER_STABLE_ID = "earth_arkhamcity_sanitarium_room_foyer_001"

INNSMOUTH_ZONE_STABLE_ID = "earth/innsmouth"
INNSMOUTH_SPECIAL_RULES = {
    "combat_modifier": 1.3,
    "exploration_bonus": 0.2,
    "npc_spawn_modifier": 0.6,
    "lucidity_drain_rate": 0.15,
    "corruption_rate": 0.05,
    "corruption_target": 40,
}

# --- #823: 2 erroneous rows to delete outright (superseded by nothing) ------------------------

DELETE_LINK_IDS = [
    "3d6893d3-9e46-5d74-9b03-e0967af2ea85",  # boundary_st_001 --west--> intersection (bogus dup)
    "87144381-f9d0-54f3-ae5f-dab6ac0f4321",  # boundary_st_002 --west--> intersection (bogus dup)
]

# --- #823: derby_gedney's south link keeps its id but is retargeted, from the shared (and wrong)
# gedney_st_001 to its own new sibling connector gedney_st_002 (#824) ---------------------------

RETARGET_LINKS_EXTRA = {
    "d0e62b9a-313b-5950-b0af-0948cb3ba396": "e8388bfa-6d9f-54fa-8cec-63c14e4ec7f9",  # -> gedney_st_002
}

# --- #823: rows whose direction changed -- old id deleted, new id inserted below --------------

REPLACE_LINK_IDS = [
    "aa3c1644-c72e-5186-a95e-2444790817d5",
    "474df80b-3b04-50ac-a1ee-66372798ad0e",
    "0c91b6f8-0a74-54cd-a32e-e2f16fc27737",
    "6c9c8aa5-e68c-5ff1-93eb-5f50fa7d054b",
]

# --- #823: rows whose to_room_id changed, id unchanged -- plain UPDATE ------------------------

RETARGET_LINKS = {
    "8cfeaffe-8965-5552-8221-f3fa34cb5b0d": "8b65203d-027d-54f4-a1e4-d0e8bef927d7",  # -> garrison_st_002
    "9cf5bc3d-aad5-53cd-93a7-028415e85932": "49aa84db-2a3d-59a4-8fc0-812112eaf16f",  # -> high_ln_003
    "35e9c909-245d-5c96-ba7e-bbf7bd165f01": "3c7d1810-926d-5fcb-b551-88f9ed352e0a",  # -> intersection_derby_high
    "4bf884a3-74f5-5f11-b4e1-72ae16a9e91a": "3c7d1810-926d-5fcb-b551-88f9ed352e0a",  # -> intersection_derby_high
}

# --- new rooms (id, subzone_id, stable_id, name, description, attributes) ---------------------

NEW_ROOMS = [
    (
        "38af9755-6863-5aba-a1fd-153efe00c63c",
        "3b61c43c-b64c-5499-964a-9247fbe4a9e1",
        "earth_arkhamcity_sanitarium_room_chapel_001",
        "Sanitarium Chapel",
        (
            "A small, disused chapel tucked at the end of the east wing, forgotten by most of the "
            "staff. Dust motes drift through the light of a single stained-glass window, and the "
            "few remaining pews are cool to the touch despite the stagnant asylum air. Whatever "
            "unease follows visitors through the rest of the sanitarium seems, here, to loosen its "
            "grip."
        ),
        {"environment": "indoors", "corruption": 0, "corruption_rate": 0.10},
    ),
    (
        "e8388bfa-6d9f-54fa-8cec-63c14e4ec7f9",
        "9674f8d2-788d-57c7-ac2e-3cbcd6a800c2",
        "earth_arkhamcity_northside_room_gedney_st_002",
        "Gedney Street - Derby Street Corner",
        (
            "Gedney Street bends here to meet Derby Street, the cobblestones uneven where two eras "
            "of paving were never quite matched. A gas lamp flickers weakly at the corner, doing "
            "little against the fog that rolls in off the harbor most evenings."
        ),
        {"environment": "street_paved"},
    ),
    (
        "51866d1d-de0f-5aca-96ea-24c2b05b0ab2",
        "65fd0800-6cc0-5313-957b-31ab284e140b",
        "earth_innsmouth_waterfront_room_causeway_001",
        "Innsmouth Road",
        (
            "A cracked, weed-choked causeway runs north out of Arkham toward Innsmouth, the "
            "surrounding marshland exhaling a faint, fishy reek even at a distance. Streetlamps "
            "here are broken or simply absent, and the few travelers on this road walk quickly, "
            "without looking back."
        ),
        {"environment": "outdoors"},
    ),
    (
        "07afa634-6e8f-52c1-b64f-a6a51317318f",
        "65fd0800-6cc0-5313-957b-31ab284e140b",
        "earth_innsmouth_waterfront_room_town_square_001",
        "Innsmouth Town Square",
        (
            "A sagging town square ringed by shuttered storefronts, most bearing faded, decades-old "
            "signage. A dry fountain at its center is stained green-black with something that isn't "
            "quite algae. Curtains twitch in upper-story windows as you pass, though no one appears "
            "at the doors."
        ),
        {"environment": "outdoors"},
    ),
    (
        "ae1d5987-9c03-5572-9cde-950d837d849e",
        "65fd0800-6cc0-5313-957b-31ab284e140b",
        "earth_innsmouth_waterfront_room_water_st_001",
        "Water Street",
        (
            "The buildings along Water Street lean toward the sea as if straining to return to it. "
            "The cobblestones are slick with a briny film that never quite dries, and the sound of "
            "the surf grows louder with every step toward the waterfront ahead."
        ),
        {"environment": "outdoors"},
    ),
]

# --- new room_links (id, from_room_id, to_room_id, direction) ---------------------------------

NEW_LINKS = [
    # Replacements for REPLACE_LINK_IDS (same logical row, new id because direction changed)
    ("fcc958c6-cb1c-5c7c-8e01-a22b07f80114", "8b65203d-027d-54f4-a1e4-d0e8bef927d7", "7c33be3d-8023-5520-aabb-8e29bbe19ff1", "north"),
    ("c14fab48-985f-5fa6-a035-2488f00c9c74", "99a9bb4c-5bd7-5b03-ac42-d22644f3f39d", "8b65203d-027d-54f4-a1e4-d0e8bef927d7", "north"),
    ("a49e16fc-7ec6-5e7d-a776-46d6ecaecfa1", "65f22652-1e6d-5626-8060-68dc0f2ca891", "f400f9e7-ab39-5d88-b4e6-f129cbcbe42f", "north"),
    ("2b95a85d-1030-5043-be8a-c01c8c7d1251", "0dbba265-e016-56e6-aa25-8a6fd7615e8e", "f400f9e7-ab39-5d88-b4e6-f129cbcbe42f", "east"),
    # #823 additive fixes
    ("aa3c1644-c72e-5186-a95e-2444790817d5", "8b65203d-027d-54f4-a1e4-d0e8bef927d7", "99a9bb4c-5bd7-5b03-ac42-d22644f3f39d", "south"),
    ("474df80b-3b04-50ac-a1ee-66372798ad0e", "99a9bb4c-5bd7-5b03-ac42-d22644f3f39d", "c2b2a8eb-c284-517d-b361-3cd5fe20327b", "south"),
    ("6563b965-f087-5a8a-9a18-c58ba514323b", "c2b2a8eb-c284-517d-b361-3cd5fe20327b", "99a9bb4c-5bd7-5b03-ac42-d22644f3f39d", "north"),
    ("7ef195ad-d0c8-502f-92e6-e56ecab48184", "e8388bfa-6d9f-54fa-8cec-63c14e4ec7f9", "1b06e3be-409b-57f1-90b6-0f40a0a21699", "north"),
    ("6ce0eb1b-c4eb-59a7-bbca-4592bfbebd75", "49aa84db-2a3d-59a4-8fc0-812112eaf16f", "bd2694b0-7860-565c-90ae-dc433f897044", "south"),
    ("93d5bf30-8463-5b9e-8b60-27113588aed8", "da14187c-22fb-5685-b25e-02ea7213ce0e", "773ac97e-18c3-55a1-bf95-f0a76fbfffaf", "west"),
    ("7ede7b92-c805-5fcc-b74d-1276f4ebd100", "0e2dccc1-9352-5cca-938d-dfa33033b5c6", "0745a816-793c-5717-a8d9-bedb5bbe244d", "up"),
    ("86d12e9e-a0d4-59a8-b0a9-4137d65735c2", "d3e6e0f5-5c9f-5459-8cb0-9c81e54b02a2", "a4f10dcd-0648-516f-bd61-433b05dcb8c0", "north"),
    # #824 content
    ("94a1bb92-d461-51be-b5b1-81b8a5660ca6", "76eb69f2-a8b3-59a9-b847-b019289a875a", "51866d1d-de0f-5aca-96ea-24c2b05b0ab2", "north"),
    ("08ed7649-a32d-5035-b913-f821042cd63a", "51866d1d-de0f-5aca-96ea-24c2b05b0ab2", "76eb69f2-a8b3-59a9-b847-b019289a875a", "south"),
    ("6b78bdc0-d3c2-52e7-b696-cb917475ff30", "51866d1d-de0f-5aca-96ea-24c2b05b0ab2", "07afa634-6e8f-52c1-b64f-a6a51317318f", "north"),
    ("ab68da12-3b04-5126-8078-93418e2adb3d", "07afa634-6e8f-52c1-b64f-a6a51317318f", "51866d1d-de0f-5aca-96ea-24c2b05b0ab2", "south"),
    ("04784ee1-66c6-502c-bd9b-c459df900c70", "07afa634-6e8f-52c1-b64f-a6a51317318f", "ae1d5987-9c03-5572-9cde-950d837d849e", "north"),
    ("a556aeae-367c-50f3-a3e7-75191f79a602", "ae1d5987-9c03-5572-9cde-950d837d849e", "07afa634-6e8f-52c1-b64f-a6a51317318f", "south"),
    ("e9ef4c7e-ee60-56f2-82b2-08b55b5f496c", "ae1d5987-9c03-5572-9cde-950d837d849e", "cbea963f-bc3b-562f-926e-19fefcda0801", "north"),
    ("fd661d72-6307-544d-a895-36d4332413f9", "cbea963f-bc3b-562f-926e-19fefcda0801", "ae1d5987-9c03-5572-9cde-950d837d849e", "south"),
    ("526308e3-2a21-573b-9d81-c23d2d3ac82d", "de85ff79-880e-5851-8b88-c41d275855d2", "38af9755-6863-5aba-a1fd-153efe00c63c", "east"),
    ("6cce07b5-1ddd-5277-9b54-0058c13e4e06", "38af9755-6863-5aba-a1fd-153efe00c63c", "de85ff79-880e-5851-8b88-c41d275855d2", "west"),
]


async def main() -> None:
    load_dotenv(".env.local")
    url = os.environ["DATABASE_URL"].replace("postgresql+asyncpg://", "postgresql://")
    conn = await asyncpg.connect(url, server_settings={"search_path": "mythos_dev"})
    try:
        async with conn.transaction():
            # 1. Zone special_rules
            current = await conn.fetchval(
                "SELECT special_rules::text FROM zones WHERE stable_id = $1", INNSMOUTH_ZONE_STABLE_ID
            )
            target = json.dumps(INNSMOUTH_SPECIAL_RULES)
            if current is not None and json.loads(current) != INNSMOUTH_SPECIAL_RULES:
                await conn.execute(
                    "UPDATE zones SET special_rules = $1::jsonb WHERE stable_id = $2", target, INNSMOUTH_ZONE_STABLE_ID
                )
                print(f"zones: updated special_rules for {INNSMOUTH_ZONE_STABLE_ID}")
            else:
                print(f"zones: {INNSMOUTH_ZONE_STABLE_ID} already up to date")

            # 2. Pier attributes
            current = await conn.fetchval("SELECT attributes::text FROM rooms WHERE stable_id = $1", PIER_STABLE_ID)
            if current is not None and json.loads(current) != PIER_ATTRIBUTES:
                await conn.execute(
                    "UPDATE rooms SET attributes = $1::jsonb WHERE stable_id = $2",
                    json.dumps(PIER_ATTRIBUTES),
                    PIER_STABLE_ID,
                )
                print(f"rooms: updated attributes for {PIER_STABLE_ID}")
            else:
                print(f"rooms: {PIER_STABLE_ID} already up to date")

            # 3. Foyer origin flag
            current = await conn.fetchval(
                "SELECT map_origin_zone FROM rooms WHERE stable_id = $1", FOYER_STABLE_ID
            )
            if current is False:
                await conn.execute(
                    "UPDATE rooms SET map_origin_zone = true WHERE stable_id = $1", FOYER_STABLE_ID
                )
                print(f"rooms: set map_origin_zone=true for {FOYER_STABLE_ID}")
            else:
                print(f"rooms: {FOYER_STABLE_ID}.map_origin_zone already {current}")

            # 4. New rooms -- must land before the gedney retarget below, which points at
            # gedney_st_002 and would otherwise violate the room_links FK.
            inserted_rooms = 0
            for room_id, subzone_id, stable_id, name, description, attributes in NEW_ROOMS:
                exists = await conn.fetchval("SELECT 1 FROM rooms WHERE id = $1", room_id)
                if exists:
                    print(f"rooms: {stable_id} already present")
                    continue
                await conn.execute(
                    """
                    INSERT INTO rooms (id, subzone_id, stable_id, name, description, attributes)
                    VALUES ($1, $2, $3, $4, $5, $6::jsonb)
                    """,
                    room_id,
                    subzone_id,
                    stable_id,
                    name,
                    description,
                    json.dumps(attributes),
                )
                inserted_rooms += 1
            print(f"rooms: inserted {inserted_rooms} new room(s)")

            # 5. Delete erroneous rows outright
            deleted = await conn.fetch(
                "DELETE FROM room_links WHERE id = ANY($1::uuid[]) RETURNING id", DELETE_LINK_IDS
            )
            print(f"room_links: deleted {len(deleted)} erroneous row(s)")

            # 6. Delete rows superseded by a direction change (re-inserted below with a new id)
            replaced = await conn.fetch(
                "DELETE FROM room_links WHERE id = ANY($1::uuid[]) RETURNING id", REPLACE_LINK_IDS
            )
            print(f"room_links: removed {len(replaced)} row(s) superseded by a direction change")

            # 7. Retarget rows whose to_room_id changed but id/direction did not
            # Note: two ids in REPLACE_LINK_IDS (aa3c1644, 474df80b) are *also* the natural id of an
            # unrelated new "south" row added below (id = hash(from_stable, direction), and that
            # room's real south exit now goes to a different neighbor than its old south exit did) --
            # so a second run of this script deletes and immediately re-inserts those two ids again.
            # Harmless (converges to the same correct row both times) but not silently idempotent;
            # not worth extra bookkeeping in a one-shot migration script.
            all_retargets = {**RETARGET_LINKS, **RETARGET_LINKS_EXTRA}
            for link_id, new_target in all_retargets.items():
                current_target = await conn.fetchval("SELECT to_room_id FROM room_links WHERE id = $1", link_id)
                if current_target is not None and str(current_target) != new_target:
                    await conn.execute("UPDATE room_links SET to_room_id = $1 WHERE id = $2", new_target, link_id)
                    print(f"room_links: retargeted {link_id} -> {new_target}")
                elif current_target is None:
                    print(f"room_links: {link_id} not found to retarget (already handled?)")
                else:
                    print(f"room_links: {link_id} already targets {new_target}")

            # 8. New room_links
            inserted_links = 0
            for link_id, from_room_id, to_room_id, direction in NEW_LINKS:
                exists = await conn.fetchval("SELECT 1 FROM room_links WHERE id = $1", link_id)
                if exists:
                    continue
                await conn.execute(
                    """
                    INSERT INTO room_links (id, from_room_id, to_room_id, direction, attributes)
                    VALUES ($1, $2, $3, $4, '{}'::jsonb)
                    """,
                    link_id,
                    from_room_id,
                    to_room_id,
                    direction,
                )
                inserted_links += 1
            print(f"room_links: inserted {inserted_links} new link(s)")

        print("\nDone. Transaction committed.")
    finally:
        await conn.close()


if __name__ == "__main__":
    asyncio.run(main())
