"""
SkillService: skills catalog, set_player_skills, get_player_skills (with ownership);
skill use logging and improvement rolls (plan 4.5).
"""

import random
import uuid
from typing import TYPE_CHECKING, Any

from server.models.skill import Skill
from server.persistence.repositories.player_skill_repository import PlayerSkillRepository
from server.persistence.repositories.skill_repository import SkillRepository
from server.persistence.repositories.skill_use_log_repository import SkillUseLogRepository
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.async_persistence import AsyncPersistenceLayer

logger = get_logger(__name__)

# one 70, two 60, three 50, three 40
OCCUPATION_VALUES = (70, 60, 60, 50, 50, 50, 40, 40, 40)
PERSONAL_INTEREST_BONUS = 20
MAX_SKILL_VALUE = 99
OWN_LANGUAGE_KEY = "own_language"
CTHULHU_MYTHOS_KEY = "cthulhu_mythos"


class SkillService:
    """Service for skills catalog, per-character skills, use logging, and improvement rolls."""

    def __init__(
        self,
        skill_repository: SkillRepository,
        player_skill_repository: PlayerSkillRepository,
        skill_use_log_repository: SkillUseLogRepository,
        persistence: "AsyncPersistenceLayer",
    ) -> None:
        self._skill_repo = skill_repository
        self._player_skill_repo = player_skill_repository
        self._skill_use_log_repo = skill_use_log_repository
        self._persistence = persistence
        self._logger = get_logger(__name__)

    async def get_skills_catalog(self) -> list[dict[str, Any]]:
        """Return list of skill dicts (id, key, name, base_value, allow_at_creation, category)."""
        skills = await self._skill_repo.get_all_skills()
        return [
            {
                "id": s.id,
                "key": s.key,
                "name": s.name,
                "description": s.description,
                "base_value": s.base_value,
                "allow_at_creation": s.allow_at_creation,
                "category": s.category,
            }
            for s in skills
        ]

    def _validate_occupation_slots(
        self,
        occupation_slots: list[dict[str, Any]],
        skills_by_id: dict[int, Skill],
    ) -> None:
        """Raise ValueError if occupation_slots are not exactly one 70, two 60, three 50, three 40."""
        if len(occupation_slots) != 9:
            raise ValueError(f"occupation_slots must have exactly 9 entries, got {len(occupation_slots)}")
        values = sorted((s["value"] for s in occupation_slots), reverse=True)
        if values != sorted(OCCUPATION_VALUES, reverse=True):
            raise ValueError("occupation_slots must have exactly one 70, two 60, three 50, three 40")
        for s in occupation_slots:
            skill_id = s.get("skill_id")
            if skill_id is None:
                raise ValueError("occupation_slots entries must have skill_id")
            skill = skills_by_id.get(skill_id)
            if not skill:
                raise ValueError(f"Unknown skill_id {skill_id}")
            if not skill.allow_at_creation:
                raise ValueError(f"Skill {skill.key} cannot be chosen in occupation (e.g. Cthulhu Mythos)")

    def _validate_personal_interest(
        self,
        personal_interest: list[dict[str, Any]],
        skills_by_id: dict[int, Skill],
    ) -> None:
        """Require exactly 4 skill_ids; Cthulhu Mythos not allowed."""
        if len(personal_interest) != 4:
            raise ValueError(f"personal_interest must have exactly 4 entries, got {len(personal_interest)}")
        for entry in personal_interest:
            skill_id = entry.get("skill_id")
            if skill_id is None:
                raise ValueError("personal_interest entries must have skill_id")
            skill = skills_by_id.get(skill_id)
            if not skill:
                raise ValueError(f"Unknown skill_id {skill_id}")
            if not skill.allow_at_creation:
                raise ValueError(f"Skill {skill.key} cannot be chosen in personal interest (e.g. Cthulhu Mythos)")

    async def validate_skills_payload(
        self,
        occupation_slots: list[dict[str, Any]],
        personal_interest: list[dict[str, Any]],
        profession_id: int,
    ) -> None:
        """
        Validate skills allocation without persisting. Raises ValueError if invalid.

        Use before create_character so invalid payloads are rejected before creating the player.
        """
        skills = await self._skill_repo.get_all_skills()
        skills_by_id = {s.id: s for s in skills}
        self._validate_occupation_slots(occupation_slots, skills_by_id)
        self._validate_personal_interest(personal_interest, skills_by_id)
        profession = await self._persistence.get_profession_by_id(profession_id)
        if not profession:
            raise ValueError(f"Profession {profession_id} not found")

    async def set_player_skills(
        self,
        player_id: uuid.UUID,
        occupation_slots: list[dict[str, Any]],
        personal_interest: list[dict[str, Any]],
        profession_id: int,
        stats_for_edu: int,
    ) -> None:
        """
        Set all skills for a character at creation.

        Validates occupation_slots (9 entries: 70, 60, 60, 50, 50, 50, 40, 40, 40)
        and personal_interest (4 skill_ids). Applies catalog base, profession
        skill_modifiers, then overlay from occupation and personal (base+20).
        Own Language: if not allocated, set to stats_for_edu (education).
        Clamps values to 0-99. Rejects Cthulhu Mythos in occupation/personal.
        """
        skills = await self._skill_repo.get_all_skills()
        skills_by_id = {s.id: s for s in skills}
        skills_by_key = {s.key: s for s in skills}

        self._validate_occupation_slots(occupation_slots, skills_by_id)
        self._validate_personal_interest(personal_interest, skills_by_id)

        profession = await self._persistence.get_profession_by_id(profession_id)
        if not profession:
            raise ValueError(f"Profession {profession_id} not found")

        # Build base: every skill with base_value gets base + profession modifier
        skill_mods = profession.get_skill_modifiers()
        mod_by_key: dict[str, int] = {}
        for m in skill_mods:
            key = m.get("skill_key") or m.get("skill_id")
            if isinstance(key, int):
                key = next((s.key for s in skills if s.id == key), None)
            if key:
                mod_by_key[key] = mod_by_key.get(key, 0) + int(m.get("value", 0))

        final: dict[int, int] = {}
        for skill in skills:
            base = skill.base_value
            delta = mod_by_key.get(skill.key, 0)
            final[skill.id] = max(0, min(MAX_SKILL_VALUE, base + delta))

        # Overlay occupation slots
        for slot in occupation_slots:
            sid = slot["skill_id"]
            val = slot["value"]
            delta = mod_by_key.get(skills_by_id[sid].key, 0)
            final[sid] = max(0, min(MAX_SKILL_VALUE, val + delta))

        # Overlay personal interest (base + 20)
        for entry in personal_interest:
            sid = entry["skill_id"]
            skill = skills_by_id[sid]
            base = skill.base_value
            delta = mod_by_key.get(skill.key, 0)
            final[sid] = max(0, min(MAX_SKILL_VALUE, base + PERSONAL_INTEREST_BONUS + delta))

        # Own Language: if not allocated in occupation or personal, set to EDU
        own_lang = skills_by_key.get(OWN_LANGUAGE_KEY)
        if own_lang:
            in_occupation = own_lang.id in {s["skill_id"] for s in occupation_slots}
            in_personal = own_lang.id in {e["skill_id"] for e in personal_interest}
            if not in_occupation and not in_personal:
                delta = mod_by_key.get(OWN_LANGUAGE_KEY, 0)
                final[own_lang.id] = max(0, min(MAX_SKILL_VALUE, stats_for_edu + delta))

        # Persist: replace all
        await self._player_skill_repo.delete_for_player(player_id)
        rows = list(final.items())
        await self._player_skill_repo.insert_many(player_id, rows)
        self._logger.info(
            "Set player skills",
            player_id=str(player_id),
            profession_id=profession_id,
            count=len(rows),
        )

    async def get_player_skills(self, player_id: uuid.UUID, user_id: uuid.UUID | str) -> list[dict[str, Any]] | None:
        """
        Return list of {skill_id, skill_key, skill_name, value} for the player.

        If the player does not belong to user_id, returns None (caller should 403).
        """
        player = await self._persistence.get_player_by_id(player_id)
        if not player:
            return None
        if str(player.user_id) != str(user_id):
            return None
        rows = await self._player_skill_repo.get_by_player_id(player_id)
        return [
            {
                "skill_id": ps.skill_id,
                "skill_key": ps.skill.key,
                "skill_name": ps.skill.name,
                "value": ps.value,
            }
            for ps in rows
        ]

    async def record_successful_skill_use(
        self,
        player_id: uuid.UUID,
        skill_id: int,
        character_level_at_use: int,
    ) -> None:
        """
        Record one successful use of a skill at the character's current level.

        Used for improvement rolls on level-up (plan 4.5).
        """
        await self._skill_use_log_repo.record_use(
            player_id=player_id,
            skill_id=skill_id,
            character_level_at_use=character_level_at_use,
        )

    async def get_skills_used_this_level(
        self,
        player_id: uuid.UUID,
        character_level: int,
    ) -> list[int]:
        """
        Return distinct skill_ids that the player successfully used at the given level.

        Used by run_improvement_rolls(level = new_level - 1) on level-up.
        """
        return await self._skill_use_log_repo.get_skill_ids_used_at_level(
            player_id=player_id,
            character_level=character_level,
        )

    async def run_improvement_rolls(self, player_id: uuid.UUID, new_level: int) -> None:
        """
        For each skill the player used during the previous level, roll d100.

        If roll > current skill value: add +1 (if value 90-98) or +1d10 (if < 90); clamp to 99.
        Plan 4.5 / 10.4 T3.
        """
        previous_level = new_level - 1
        if previous_level < 1:
            return
        skill_ids = await self.get_skills_used_this_level(player_id, previous_level)
        if not skill_ids:
            return
        player_skills = await self._player_skill_repo.get_by_player_id(player_id)
        value_by_skill: dict[int, int] = {ps.skill_id: ps.value for ps in player_skills}
        for skill_id in skill_ids:
            current = value_by_skill.get(skill_id)
            if current is None:
                continue
            roll = random.randint(1, 100)
            if roll <= current:
                continue
            if current >= 90:
                gain = 1
            else:
                gain = random.randint(1, 10)
            new_value = min(MAX_SKILL_VALUE, current + gain)
            await self._player_skill_repo.update_value(player_id, skill_id, new_value)
            self._logger.info(
                "Skill improved on level-up",
                player_id=str(player_id),
                skill_id=skill_id,
                previous_level=previous_level,
                old_value=current,
                new_value=new_value,
                roll=roll,
            )

    async def roll_skill_check(
        self,
        player_id: uuid.UUID,
        skill_id: int,
        character_level: int,
    ) -> bool:
        """
        Roll d100 against the character's skill value; on success record use and return True.

        Commands that resolve a skill check (e.g. library use, spot hidden) should call this
        with the player's current character level. Uses server-authoritative skill value.
        Plan 10.4 T5.
        """
        player_skills = await self._player_skill_repo.get_by_player_id(player_id)
        value_by_skill: dict[int, int] = {ps.skill_id: ps.value for ps in player_skills}
        skill_value = value_by_skill.get(skill_id)
        if skill_value is None:
            return False
        roll = random.randint(1, 100)
        success = roll <= skill_value
        if success:
            await self.record_successful_skill_use(
                player_id=player_id,
                skill_id=skill_id,
                character_level_at_use=character_level,
            )
        return success
