"""Hallucination trigger handling for passive lucidity flux."""

from __future__ import annotations

import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from ...structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def handle_phantom_hostile_hallucination(
    player_id_uuid: uuid.UUID, room_id: str, tier: str, current_lcd: int
) -> None:
    """Handle phantom hostile spawn hallucination (#625, #714)."""
    from ...game.chat_npc_system import deliver_personal_system
    from ...services.lucidity_event_dispatcher import send_hallucination_event
    from ...services.phantom_hostile_service import phantom_hostile_service

    phantom_data = phantom_hostile_service.create_phantom_hostile_data(player_id_uuid, room_id, tier)
    spawn_message = f"A {phantom_data['name']} materializes before you!"
    # #714: the phantom itself is already visible via the per-viewer room payload (see
    # phantom_visibility.py) -- this is just the spawn moment's ambient narration, delivered
    # like any other environmental system line so it carries no "this is fake" marker.
    _ = await deliver_personal_system(player_id_uuid, spawn_message)
    await send_hallucination_event(
        player_id_uuid,
        hallucination_type="phantom_hostile_spawn",
        message=spawn_message,
        metadata={
            "tier": tier,
            "lcd": current_lcd,
            "phantom_id": phantom_data["phantom_id"],
            "phantom_name": phantom_data["name"],
            "room_id": room_id,
            "max_dp": 1,
            "current_dp": 1,
            "is_non_damaging": phantom_data["is_non_damaging"],
        },
    )
    logger.debug(
        "Phantom hostile spawn hallucination triggered",
        player_id=player_id_uuid,
        tier=tier,
        phantom_id=phantom_data["phantom_id"],
        phantom_name=phantom_data["name"],
    )


async def handle_fake_hallucination(player_id_uuid: uuid.UUID, room_id: str, tier: str, current_lcd: int) -> None:
    """Handle fake hallucination (NPC tells or room text overlays) (#714)."""
    from ...game.chat_npc_system import deliver_fake_npc_whisper, deliver_personal_system
    from ...services.fake_hallucination_service import FakeHallucinationService
    from ...services.fake_sender_registry import fake_sender_registry
    from ...services.lucidity_event_dispatcher import send_hallucination_event

    fake_hallucination_service = FakeHallucinationService()
    hallucination_type = fake_hallucination_service.select_hallucination_type()

    if hallucination_type == "fake_npc_tell":
        fake_tell_data = fake_hallucination_service.generate_fake_npc_tell(player_id_uuid, room_id)
        # #714: delivered as an ordinary whisper from the fake NPC name -- byte-identical on the
        # wire to a real NPC whisper, no separate "hallucination" event type. Recorded in the
        # fake-sender registry too, so `reply` can answer in-fiction instead of leaking
        # "player not found" the moment someone reacts naturally to it.
        _ = await deliver_fake_npc_whisper(player_id_uuid, fake_tell_data["npc_name"], fake_tell_data["message"])
        fake_sender_registry.record_fake_whisper(player_id_uuid, fake_tell_data["npc_name"])
        await send_hallucination_event(
            player_id_uuid,
            hallucination_type="fake_npc_tell",
            message=fake_tell_data["message"],
            metadata={
                "tier": tier,
                "lcd": current_lcd,
                "npc_name": fake_tell_data["npc_name"],
                "room_id": room_id,
                "hallucination_id": fake_tell_data["hallucination_id"],
            },
        )
        logger.debug(
            "Fake NPC tell hallucination triggered",
            player_id=player_id_uuid,
            tier=tier,
            npc_name=fake_tell_data["npc_name"],
        )
    else:  # room_text_overlay
        overlay_data = fake_hallucination_service.generate_room_text_overlay(player_id_uuid, room_id)
        # #714: a spontaneous ambient line, not persisted into the room description -- the
        # authored strings ("the temperature suddenly drops") are events, not static text, and
        # would read as broken prose if repeated on a later `look`.
        _ = await deliver_personal_system(player_id_uuid, overlay_data["overlay_text"])
        await send_hallucination_event(
            player_id_uuid,
            hallucination_type="room_text_overlay",
            message=overlay_data["overlay_text"],
            metadata={
                "tier": tier,
                "lcd": current_lcd,
                "room_id": room_id,
                "hallucination_id": overlay_data["hallucination_id"],
            },
        )
        logger.debug(
            "Room text overlay hallucination triggered",
            player_id=player_id_uuid,
            tier=tier,
            room_id=room_id,
        )


async def handle_hallucination_triggers(
    player_id_uuid: uuid.UUID,
    player_id_str: str,
    room_id: str,
    lucidity_records: dict[str, object],
    session: AsyncSession,
) -> None:
    """Check and handle time-based hallucination triggers."""
    from ...services.hallucination_frequency_service import HallucinationFrequencyService
    from ...services.phantom_hostile_service import phantom_hostile_service

    frequency_service = HallucinationFrequencyService()
    lucidity_record = lucidity_records.get(player_id_str)
    if not lucidity_record:
        return
    tier = getattr(lucidity_record, "current_tier", None)
    if tier not in ("fractured", "deranged"):
        return
    current_lcd = getattr(lucidity_record, "current_lcd", 0)
    should_trigger = await frequency_service.check_time_based_hallucination(player_id_uuid, current_lcd, session)
    if not should_trigger:
        return
    if phantom_hostile_service.should_spawn_phantom_hostile(tier):
        await handle_phantom_hostile_hallucination(player_id_uuid, room_id, tier, current_lcd)
    else:
        await handle_fake_hallucination(player_id_uuid, room_id, tier, current_lcd)
