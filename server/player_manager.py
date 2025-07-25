import json
import os
from typing import Dict, Optional, List
from server.models import Player, Stats, StatusEffect, StatusEffectType
import random


class PlayerManager:
    """Manages player data persistence and operations using per-player files."""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.players_dir = os.path.join(data_dir, "players")
        self.players: Dict[str, Player] = {}
        self._ensure_players_dir()
        self._load_all_players()

    def _ensure_players_dir(self) -> None:
        os.makedirs(self.players_dir, exist_ok=True)

    def _player_file_path(self, player_id: str) -> str:
        return os.path.join(self.players_dir, f"player_{player_id}.json")

    def _load_all_players(self) -> None:
        """Load all players from individual files."""
        self.players = {}
        for filename in os.listdir(self.players_dir):
            if filename.startswith("player_") and filename.endswith(".json"):
                file_path = os.path.join(self.players_dir, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        player_data = json.load(f)
                        player = Player(**player_data)
                        self.players[player.id] = player
                except Exception as e:
                    print(f"Error loading player file {file_path}: {e}")

    def load_player(self, player_id: str) -> Optional[Player]:
        """Load a single player from file."""
        file_path = self._player_file_path(player_id)
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    player_data = json.load(f)
                    player = Player(**player_data)
                    self.players[player.id] = player
                    return player
            except Exception as e:
                print(f"Error loading player file {file_path}: {e}")
        return None

    def save_player(self, player: Player) -> None:
        """Save a single player to file."""
        file_path = self._player_file_path(player.id)
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(player.model_dump(), f, indent=2, default=str)
        except Exception as e:
            print(f"Error saving player file {file_path}: {e}")

    def create_player(self, name: str, starting_room_id: str = "arkham_001") -> Player:
        """Create a new player with randomized stats and save to file."""
        stats = Stats(
            strength=random.randint(3, 18),
            dexterity=random.randint(3, 18),
            constitution=random.randint(3, 18),
            intelligence=random.randint(3, 18),
            wisdom=random.randint(3, 18),
            charisma=random.randint(3, 18),
            sanity=100,
            occult_knowledge=0,
            fear=0,
            corruption=0,
            cult_affiliation=0,
        )
        player = Player(name=name, stats=stats, current_room_id=starting_room_id)
        self.players[player.id] = player
        self.save_player(player)
        return player

    def get_player(self, player_id: str) -> Optional[Player]:
        """Get a player by ID, loading from file if not in memory."""
        if player_id in self.players:
            return self.players[player_id]
        return self.load_player(player_id)

    def get_player_by_name(self, name: str) -> Optional[Player]:
        """Get a player by name, loading from file if not in memory."""
        for player in self.players.values():
            if player.name.lower() == name.lower():
                return player
        # If not found in memory, try loading all files
        for filename in os.listdir(self.players_dir):
            if filename.startswith("player_") and filename.endswith(".json"):
                file_path = os.path.join(self.players_dir, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        player_data = json.load(f)
                        if player_data.get("name", "").lower() == name.lower():
                            player = Player(**player_data)
                            self.players[player.id] = player
                            return player
                except Exception:
                    continue
        return None

    def update_player(self, player: Player) -> None:
        """Update a player's data and save to file."""
        player.update_last_active()
        self.players[player.id] = player
        self.save_player(player)

    def delete_player(self, player_id: str) -> bool:
        """Delete a player file and remove from memory."""
        if player_id in self.players:
            del self.players[player_id]
        file_path = self._player_file_path(player_id)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False

    def list_players(self) -> List[Player]:
        """Get a list of all players."""
        self._load_all_players()
        return list(self.players.values())

    def apply_sanity_loss(
        self, player: Player, amount: int, source: str = "unknown"
    ) -> None:
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

    def apply_corruption(
        self, player: Player, amount: int, source: str = "unknown"
    ) -> None:
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

    def gain_occult_knowledge(
        self, player: Player, amount: int, source: str = "unknown"
    ) -> None:
        """Gain occult knowledge with potential sanity loss."""
        player.stats.occult_knowledge = min(100, player.stats.occult_knowledge + amount)

        # Learning forbidden knowledge comes with a price
        sanity_loss = amount // 2  # Lose half the knowledge gained as sanity
        if sanity_loss > 0:
            self.apply_sanity_loss(player, sanity_loss, f"learning from {source}")

        self.update_player(player)

    def heal_player(self, player: Player, amount: int) -> None:
        """Heal a player's health."""
        player.stats.current_health = min(
            player.stats.max_health, player.stats.current_health + amount
        )
        self.update_player(player)

    def damage_player(
        self, player: Player, amount: int, damage_type: str = "physical"
    ) -> None:
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
                    player.stats.dexterity = max(
                        1, player.stats.dexterity - effect.intensity
                    )

            # Remove expired effects
            player.status_effects = [
                effect
                for effect in player.status_effects
                if effect.is_active(current_tick)
            ]

            self.update_player(player)
