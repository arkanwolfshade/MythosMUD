import json
import os
from typing import Dict, Optional, List
from datetime import datetime
from server.models import Player, Stats, StatusEffect, StatusEffectType
import random


class PlayerManager:
    def save_player(self, player):
        """Serialize a player to a JSON file in the ./players folder."""
        player_data = player.__dict__.copy()
        # If player.stats is an object, serialize its __dict__
        if hasattr(player_data.get("stats"), "__dict__"):
            player_data["stats"] = player_data["stats"].__dict__
        players_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "players")
        os.makedirs(players_dir, exist_ok=True)
        file_path = os.path.join(players_dir, f"{player.name}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(player_data, f, indent=2)

    """Manages player data persistence and operations."""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.players_file = os.path.join(data_dir, "players.json")
        self.players: Dict[str, Player] = {}
        self._ensure_data_dir()
        self._load_players()

    def _ensure_data_dir(self) -> None:
        """Ensure the data directory exists."""
        os.makedirs(self.data_dir, exist_ok=True)

    def _load_players(self) -> None:
        """Load all players from the data file."""
        if os.path.exists(self.players_file):
            try:
                with open(self.players_file, "r", encoding="utf-8") as f:
                    players_data = json.load(f)
                    for player_data in players_data.values():
                        player = Player(**player_data)
                        self.players[player.id] = player
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading players: {e}")
                # Backup corrupted file
                if os.path.exists(self.players_file):
                    backup_file = f"{self.players_file}.backup.{datetime.now().timestamp()}"
                    os.rename(self.players_file, backup_file)

    def _save_players(self) -> None:
        """Save all players to the data file."""
        try:
            players_data = {player_id: player.model_dump() for player_id, player in self.players.items()}
            with open(self.players_file, "w", encoding="utf-8") as f:
                json.dump(players_data, f, indent=2, default=str)
        except Exception as e:
            print(f"Error saving players: {e}")

    def create_player(self, name: str, starting_room_id: str = "arkham_001") -> Player:
        """Create a new player with randomized stats."""
        # Generate random stats using 3d6 method (D&D style)
        stats = Stats(
            strength=random.randint(3, 18),
            dexterity=random.randint(3, 18),
            constitution=random.randint(3, 18),
            intelligence=random.randint(3, 18),
            wisdom=random.randint(3, 18),
            charisma=random.randint(3, 18),
            sanity=100,  # Start with full sanity
            occult_knowledge=0,  # Start with no occult knowledge
            fear=0,  # Start with no fear
            corruption=0,  # Start uncorrupted
            cult_affiliation=0,  # Start unaffiliated
        )

        player = Player(name=name, stats=stats, current_room_id=starting_room_id)

        self.players[player.id] = player
        self._save_players()
        return player

    def get_player(self, player_id: str) -> Optional[Player]:
        """Get a player by ID."""
        return self.players.get(player_id)

    def get_player_by_name(self, name: str) -> Optional[Player]:
        """Get a player by name."""
        for player in self.players.values():
            if player.name.lower() == name.lower():
                return player
        return None

    def update_player(self, player: Player) -> None:
        """Update a player's data."""
        player.update_last_active()
        self.players[player.id] = player
        self._save_players()

    def delete_player(self, player_id: str) -> bool:
        """Delete a player."""
        if player_id in self.players:
            del self.players[player_id]
            self._save_players()
            return True
        return False

    def list_players(self) -> List[Player]:
        """Get a list of all players."""
        return list(self.players.values())

    def apply_sanity_loss(self, player: Player, amount: int, source: str = "unknown") -> None:
        """Apply sanity loss to a player with potential status effects."""
        old_sanity = player.stats.sanity
        player.stats.sanity = max(0, player.stats.sanity - amount)

        # Apply status effects based on sanity loss
        if player.stats.sanity <= 0 and old_sanity > 0:
            # Complete madness
            player.add_status_effect(
                StatusEffect(
                    effect_type=StatusEffectType.INSANE,
                    duration=0,  # Permanent until cured
                    intensity=10,
                    source=source,
                )
            )
        elif player.stats.sanity <= 25 and old_sanity > 25:
            # Severe mental instability
            player.add_status_effect(
                StatusEffect(
                    effect_type=StatusEffectType.HALLUCINATING,
                    duration=0,  # Permanent until sanity recovers
                    intensity=8,
                    source=source,
                )
            )
        elif player.stats.sanity <= 50 and old_sanity > 50:
            # Moderate mental instability
            player.add_status_effect(
                StatusEffect(
                    effect_type=StatusEffectType.PARANOID,
                    duration=0,  # Permanent until sanity recovers
                    intensity=5,
                    source=source,
                )
            )

        self.update_player(player)

    def apply_fear(self, player: Player, amount: int, source: str = "unknown") -> None:
        """Apply fear to a player with potential status effects."""
        old_fear = player.stats.fear
        player.stats.fear = min(100, player.stats.fear + amount)

        # Apply status effects based on fear level
        if player.stats.fear >= 75 and old_fear < 75:
            # Extreme fear - trembling
            player.add_status_effect(
                StatusEffect(
                    effect_type=StatusEffectType.TREMBLING,
                    duration=0,  # Permanent until fear decreases
                    intensity=7,
                    source=source,
                )
            )

        self.update_player(player)

    def apply_corruption(self, player: Player, amount: int, source: str = "unknown") -> None:
        """Apply corruption to a player with potential status effects."""
        old_corruption = player.stats.corruption
        player.stats.corruption = min(100, player.stats.corruption + amount)

        # Apply status effects based on corruption level
        if player.stats.corruption >= 50 and old_corruption < 50:
            # Significant corruption
            player.add_status_effect(
                StatusEffect(
                    effect_type=StatusEffectType.CORRUPTED,
                    duration=0,  # Permanent until corruption decreases
                    intensity=6,
                    source=source,
                )
            )

        self.update_player(player)

    def gain_occult_knowledge(self, player: Player, amount: int, source: str = "unknown") -> None:
        """Gain occult knowledge with potential sanity loss."""
        player.stats.occult_knowledge = min(100, player.stats.occult_knowledge + amount)

        # Learning forbidden knowledge comes with a price
        sanity_loss = amount // 2  # Lose half the knowledge gained as sanity
        if sanity_loss > 0:
            self.apply_sanity_loss(player, sanity_loss, f"learning from {source}")

        self.update_player(player)

    def heal_player(self, player: Player, amount: int) -> None:
        """Heal a player's health."""
        player.stats.current_health = min(player.stats.max_health, player.stats.current_health + amount)
        self.update_player(player)

    def damage_player(self, player: Player, amount: int, damage_type: str = "physical") -> None:
        """Damage a player's health."""
        player.stats.current_health = max(0, player.stats.current_health - amount)

        # Apply status effects based on damage type
        if damage_type == "poison":
            player.add_status_effect(
                StatusEffect(
                    effect_type=StatusEffectType.POISONED,
                    duration=10,  # 10 ticks
                    intensity=5,
                    source="poison damage",
                )
            )

        self.update_player(player)

    def process_status_effects(self, current_tick: int) -> None:
        """Process all active status effects for all players."""
        for player in self.players.values():
            active_effects = player.get_active_status_effects(current_tick)

            # Apply effects based on type
            for effect in active_effects:
                if effect.effect_type == StatusEffectType.POISONED:
                    # Poison damage over time
                    self.damage_player(player, effect.intensity, "poison")
                elif effect.effect_type == StatusEffectType.TREMBLING:
                    # Trembling reduces dexterity temporarily
                    player.stats.dexterity = max(1, player.stats.dexterity - effect.intensity)

            # Remove expired effects
            player.status_effects = [effect for effect in player.status_effects if effect.is_active(current_tick)]

            self.update_player(player)
