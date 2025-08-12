"""
Room Fixer

Automated fixing capabilities for common room issues.
Consolidates functionality from various fix scripts.
"""

import json
import shutil
from typing import Any


class RoomFixer:
    """Automated room fixing capabilities"""

    def __init__(self, base_path: str):
        self.base_path = base_path
        self.fixes_applied = []
        self.fixes_failed = []

    def apply_fixes(
        self, room_database: dict[str, dict[str, Any]], errors: list[dict[str, Any]], backup: bool = True
    ) -> dict[str, Any]:
        """Apply fixes based on validation errors"""
        fix_summary = {
            "fixes_applied": 0,
            "fixes_failed": 0,
            "applied_fixes": [],
            "failed_fixes": [],
        }

        # Group errors by type
        error_groups = {}
        for error in errors:
            error_type = error.get("type", "unknown")
            if error_type not in error_groups:
                error_groups[error_type] = []
            error_groups[error_type].append(error)

        # Apply fixes for each error type
        for error_type, type_errors in error_groups.items():
            if error_type == "id_mismatch":
                result = self._fix_id_mismatches(room_database, type_errors, backup)
                fix_summary["fixes_applied"] += result.get("fixes_applied", 0)
                fix_summary["fixes_failed"] += result.get("fixes_failed", 0)
                fix_summary["applied_fixes"].extend(result.get("applied_fixes", []))
                fix_summary["failed_fixes"].extend(result.get("failed_fixes", []))

            elif error_type == "invalid_environment":
                result = self._fix_environment_types(room_database, type_errors, backup)
                fix_summary["fixes_applied"] += result.get("fixes_applied", 0)
                fix_summary["fixes_failed"] += result.get("fixes_failed", 0)
                fix_summary["applied_fixes"].extend(result.get("applied_fixes", []))
                fix_summary["failed_fixes"].extend(result.get("failed_fixes", []))

        return fix_summary

    def fix_id_mismatches(
        self, room_database: dict[str, dict[str, Any]], backup: bool = True, dry_run: bool = False
    ) -> dict[str, Any]:
        """Fix room ID mismatches by adding missing 'room_' prefixes"""
        result = {
            "fixes_applied": 0,
            "fixes_failed": 0,
            "applied_fixes": [],
            "failed_fixes": [],
        }

        # Find all room files that need fixing
        for room_id, room in room_database.items():
            file_path = room.get("_file_path")
            if not file_path:
                continue

            exits = room.get("exits", {})
            needs_update = False
            updated_exits = exits.copy()

            for direction, target in exits.items():
                if target and not target.startswith("room_") and "room_" in room_id:
                    # This is a room file but the exit doesn't have room_ prefix
                    expected_target = f"room_{target}"
                    if expected_target in room_database:
                        updated_exits[direction] = expected_target
                        needs_update = True

            if needs_update and not dry_run:
                try:
                    # Create backup if requested
                    if backup:
                        backup_path = file_path + ".backup"
                        shutil.copy2(file_path, backup_path)

                    # Update the file
                    room["exits"] = updated_exits
                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(room, f, indent=2, ensure_ascii=False)

                    result["fixes_applied"] += 1
                    result["applied_fixes"].append(f"Fixed ID mismatches in {room_id}")

                except Exception as e:
                    result["fixes_failed"] += 1
                    result["failed_fixes"].append(f"Failed to fix {room_id}: {e}")

            elif needs_update and dry_run:
                result["fixes_applied"] += 1
                result["applied_fixes"].append(f"Would fix ID mismatches in {room_id}")

        return result

    def fix_environment_types(
        self, room_database: dict[str, dict[str, Any]], backup: bool = True, dry_run: bool = False
    ) -> dict[str, Any]:
        """Fix environment type categorization based on subzone patterns"""
        result = {
            "fixes_applied": 0,
            "fixes_failed": 0,
            "applied_fixes": [],
            "failed_fixes": [],
        }

        # Environment type mapping based on subzone
        subzone_environments = {
            "campus": "campus",
            "waterfront": "waterfront",
            "river_town": "waterfront",
            "downtown": "street_paved",
            "northside": "residential",
            "french_hill": "residential",
            "merchant": "commercial",
            "east_town": "residential",
            "lower_southside": "industrial",
            "uptown": "residential",
        }

        for room_id, room in room_database.items():
            file_path = room.get("_file_path")
            if not file_path:
                continue

            current_env = room.get("environment", "outdoors")
            subzone = room.get("_subzone", "")

            # Determine correct environment type
            correct_env = None
            if subzone in subzone_environments:
                correct_env = subzone_environments[subzone]
            elif "intersection" in room_id.lower():
                correct_env = "intersection"
            elif current_env == "outdoors" and subzone:
                # Default to street_paved for urban areas
                correct_env = "street_paved"

            if correct_env and correct_env != current_env:
                if not dry_run:
                    try:
                        # Create backup if requested
                        if backup:
                            backup_path = file_path + ".backup"
                            shutil.copy2(file_path, backup_path)

                        # Update the file
                        room["environment"] = correct_env
                        with open(file_path, "w", encoding="utf-8") as f:
                            json.dump(room, f, indent=2, ensure_ascii=False)

                        result["fixes_applied"] += 1
                        result["applied_fixes"].append(
                            f"Fixed environment type in {room_id}: {current_env} → {correct_env}"
                        )

                    except Exception as e:
                        result["fixes_failed"] += 1
                        result["failed_fixes"].append(f"Failed to fix environment in {room_id}: {e}")

                else:
                    result["fixes_applied"] += 1
                    result["applied_fixes"].append(
                        f"Would fix environment type in {room_id}: {current_env} → {correct_env}"
                    )

        return result

    def fix_intersection_ids(
        self, room_database: dict[str, dict[str, Any]], backup: bool = True, dry_run: bool = False
    ) -> dict[str, Any]:
        """Fix intersection room IDs to include subzone prefix"""
        result = {
            "fixes_applied": 0,
            "fixes_failed": 0,
            "applied_fixes": [],
            "failed_fixes": [],
        }

        # Find intersection rooms that need fixing
        for room_id, room in room_database.items():
            if not room_id.startswith("earth_arkham_city_intersection_"):
                continue

            file_path = room.get("_file_path")
            if not file_path:
                continue

            subzone = room.get("_subzone")
            if not subzone:
                continue

            # Create corrected room ID
            intersection_part = room_id.replace("earth_arkham_city_intersection_", "")
            corrected_id = f"earth_arkham_city_{subzone}_intersection_{intersection_part}"

            if corrected_id != room_id:
                if not dry_run:
                    try:
                        # Create backup if requested
                        if backup:
                            backup_path = file_path + ".backup"
                            shutil.copy2(file_path, backup_path)

                        # Update the file
                        room["id"] = corrected_id

                        # Update self-references in exits
                        exits = room.get("exits", {})
                        for direction, target in exits.items():
                            if target == room_id:
                                exits[direction] = corrected_id

                        with open(file_path, "w", encoding="utf-8") as f:
                            json.dump(room, f, indent=2, ensure_ascii=False)

                        result["fixes_applied"] += 1
                        result["applied_fixes"].append(f"Fixed intersection ID: {room_id} → {corrected_id}")

                    except Exception as e:
                        result["fixes_failed"] += 1
                        result["failed_fixes"].append(f"Failed to fix intersection ID {room_id}: {e}")

                else:
                    result["fixes_applied"] += 1
                    result["applied_fixes"].append(f"Would fix intersection ID: {room_id} → {corrected_id}")

        return result

    def _fix_id_mismatches(
        self, room_database: dict[str, dict[str, Any]], errors: list[dict[str, Any]], backup: bool
    ) -> dict[str, Any]:
        """Internal method to fix ID mismatches from validation errors"""
        return self.fix_id_mismatches(room_database, backup)

    def _fix_environment_types(
        self, room_database: dict[str, dict[str, Any]], errors: list[dict[str, Any]], backup: bool
    ) -> dict[str, Any]:
        """Internal method to fix environment types from validation errors"""
        return self.fix_environment_types(room_database, backup)

    def get_fix_summary(self) -> dict[str, Any]:
        """Get summary of applied fixes"""
        return {
            "fixes_applied": len(self.fixes_applied),
            "fixes_failed": len(self.fixes_failed),
            "applied_fixes": self.fixes_applied,
            "failed_fixes": self.fixes_failed,
        }
