"""
Predefined subject patterns for MythosMUD chat system.

This module contains all predefined NATS subject patterns used throughout
the application. Patterns follow the hierarchical structure:
{service}.{channel}.{scope}.{identifier}

AI: These patterns define the hierarchical structure: {service}.{channel}.{scope}.{identifier}
"""

# Predefined subject patterns for MythosMUD chat system
PREDEFINED_PATTERNS = {
    # Chat patterns
    "chat_say_room": {
        "pattern": "chat.say.room.{room_id}",
        "required_params": ["room_id"],
        "description": "Room-level say messages",
    },
    "chat_local_subzone": {
        "pattern": "chat.local.subzone.{subzone}",
        "required_params": ["subzone"],
        "description": "Subzone-level local messages",
    },
    "chat_global": {
        "pattern": "chat.global",
        "required_params": [],
        "description": "Global chat messages",
    },
    "chat_whisper_player": {
        "pattern": "chat.whisper.player.{target_id}",
        "required_params": ["target_id"],
        "description": "Player-to-player whisper messages",
    },
    "chat_system": {
        "pattern": "chat.system",
        "required_params": [],
        "description": "System-wide messages",
    },
    "chat_emote_room": {
        "pattern": "chat.emote.room.{room_id}",
        "required_params": ["room_id"],
        "description": "Room-level emote messages",
    },
    "chat_pose_room": {
        "pattern": "chat.pose.room.{room_id}",
        "required_params": ["room_id"],
        "description": "Room-level pose messages",
    },
    "chat_party_group": {
        "pattern": "chat.party.group.{party_id}",
        "required_params": ["party_id"],
        "description": "Party (ephemeral group) chat messages",
    },
    # Event patterns
    "event_player_entered": {
        "pattern": "events.player_entered.{room_id}",
        "required_params": ["room_id"],
        "description": "Player entered room events",
    },
    "event_player_left": {
        "pattern": "events.player_left.{room_id}",
        "required_params": ["room_id"],
        "description": "Player left room events",
    },
    "event_game_tick": {
        "pattern": "events.game_tick",
        "required_params": [],
        "description": "Global game tick events",
    },
    "event_player_mortally_wounded": {
        "pattern": "events.player_mortally_wounded.{room_id}",
        "required_params": ["room_id"],
        "description": "Player mortally wounded events",
    },
    "event_player_dp_decay": {
        "pattern": "events.player_dp_decay.{room_id}",
        "required_params": ["room_id"],
        "description": "Player DP decay events",
    },
    "event_player_died": {
        "pattern": "events.player_died.{room_id}",
        "required_params": ["room_id"],
        "description": "Player death events",
    },
    "event_player_respawned": {
        "pattern": "events.player_respawned.{room_id}",
        "required_params": ["room_id"],
        "description": "Player respawn events",
    },
    "event_domain": {
        "pattern": "events.domain.{event_type}",
        "required_params": ["event_type"],
        "description": "Distributed EventBus domain events",
    },
    # Combat patterns
    "combat_attack": {
        "pattern": "combat.attack.{room_id}",
        "required_params": ["room_id"],
        "description": "Combat attack events",
    },
    "combat_npc_attacked": {
        "pattern": "combat.npc_attacked.{room_id}",
        "required_params": ["room_id"],
        "description": "NPC attacked events",
    },
    "combat_npc_action": {
        "pattern": "combat.npc_action.{room_id}",
        "required_params": ["room_id"],
        "description": "NPC action events",
    },
    "combat_started": {
        "pattern": "combat.started.{room_id}",
        "required_params": ["room_id"],
        "description": "Combat started events",
    },
    "combat_ended": {
        "pattern": "combat.ended.{room_id}",
        "required_params": ["room_id"],
        "description": "Combat ended events",
    },
    "combat_npc_died": {
        "pattern": "combat.npc_died.{room_id}",
        "required_params": ["room_id"],
        "description": "NPC death events",
    },
    "combat_damage": {
        "pattern": "combat.damage.{room_id}",
        "required_params": ["room_id"],
        "description": "Combat damage events",
    },
    "combat_turn": {
        "pattern": "combat.turn.{room_id}",
        "required_params": ["room_id"],
        "description": "Combat turn events",
    },
    "combat_timeout": {
        "pattern": "combat.timeout.{room_id}",
        "required_params": ["room_id"],
        "description": "Combat timeout events",
    },
    "combat_dp_update": {
        "pattern": "combat.dp_update.{player_id}",
        "required_params": ["player_id"],
        "description": "Player DP update events",
    },
}
