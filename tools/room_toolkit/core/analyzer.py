"""
Room Analyzer

Comprehensive analysis and reporting capabilities for room data.
"""

import json
from collections import defaultdict
from typing import Any

try:
    from rich.console import Console

    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False


class RoomAnalyzer:
    """Comprehensive room analysis and reporting"""

    def __init__(self):
        self.console = Console() if RICH_AVAILABLE else None

    def analyze_connectivity(self, room_database: dict[str, dict[str, Any]]) -> dict[str, Any]:
        """Analyze room connectivity patterns"""
        analysis = {
            "total_rooms": len(room_database),
            "connected_components": [],
            "exit_distribution": defaultdict(int),
            "connectivity_stats": {},
        }

        # Analyze exit distribution
        for room in room_database.values():
            exits = room.get("exits", {})
            exit_count = len([e for e in exits.values() if e])
            analysis["exit_distribution"][exit_count] += 1

        # Find connected components
        components = self._find_connected_components(room_database)
        analysis["connected_components"] = [{"size": len(comp), "rooms": list(comp)} for comp in components]

        # Connectivity statistics
        analysis["connectivity_stats"] = {
            "total_components": len(components),
            "largest_component": max(len(comp) for comp in components) if components else 0,
            "average_component_size": sum(len(comp) for comp in components) / len(components) if components else 0,
            "isolated_rooms": len([comp for comp in components if len(comp) == 1]),
        }

        return analysis

    def analyze_environment_distribution(self, room_database: dict[str, dict[str, Any]]) -> dict[str, Any]:
        """Analyze environment type distribution"""
        analysis = {
            "environment_counts": defaultdict(int),
            "subzone_environments": defaultdict(lambda: defaultdict(int)),
            "environment_examples": defaultdict(list),
        }

        for room_id, room in room_database.items():
            env = room.get("environment", "unknown")
            subzone = room.get("_subzone", "unknown")

            analysis["environment_counts"][env] += 1
            analysis["subzone_environments"][subzone][env] += 1

            # Keep track of examples (first 5 per environment)
            if len(analysis["environment_examples"][env]) < 5:
                analysis["environment_examples"][env].append(room_id)

        return analysis

    def analyze_zone_structure(self, room_database: dict[str, dict[str, Any]]) -> dict[str, Any]:
        """Analyze zone and subzone structure"""
        analysis = {
            "zones": defaultdict(lambda: {"subzones": set(), "room_count": 0}),
            "subzone_stats": defaultdict(lambda: {"room_count": 0, "environments": set()}),
        }

        for _room_id, room in room_database.items():
            zone = room.get("_zone", "unknown")
            subzone = room.get("_subzone", "unknown")
            env = room.get("environment", "unknown")

            analysis["zones"][zone]["subzones"].add(subzone)
            analysis["zones"][zone]["room_count"] += 1

            analysis["subzone_stats"][subzone]["room_count"] += 1
            analysis["subzone_stats"][subzone]["environments"].add(env)

        # Convert sets to lists for JSON serialization
        for zone_data in analysis["zones"].values():
            zone_data["subzones"] = list(zone_data["subzones"])

        for subzone_data in analysis["subzone_stats"].values():
            subzone_data["environments"] = list(subzone_data["environments"])

        return analysis

    def _find_connected_components(self, room_database: dict[str, dict[str, Any]]) -> list[set]:
        """Find all connected components in the room graph"""
        visited = set()
        components = []

        for room_id in room_database:
            if room_id not in visited:
                component = self._bfs_component(room_id, room_database)
                components.append(component)
                visited.update(component)

        return components

    def _bfs_component(self, start_room: str, room_database: dict[str, dict[str, Any]]) -> set:
        """Find all rooms reachable from start_room using BFS"""
        if start_room not in room_database:
            return set()

        component = set()
        queue = [start_room]
        component.add(start_room)

        while queue:
            current = queue.pop(0)
            room = room_database[current]

            for _direction, target in room.get("exits", {}).items():
                if target and target in room_database and target not in component:
                    component.add(target)
                    queue.append(target)

        return component

    def generate_console_report(self, analysis_results: dict[str, Any]) -> str:
        """Generate console-formatted analysis report"""
        report_lines = []
        report_lines.append("=" * 80)
        report_lines.append("MYTHOSMUD ROOM ANALYSIS REPORT")
        report_lines.append("=" * 80)
        report_lines.append("")

        # Connectivity Analysis
        if "connectivity" in analysis_results:
            conn = analysis_results["connectivity"]
            report_lines.append("🔗 CONNECTIVITY ANALYSIS")
            report_lines.append("-" * 40)
            report_lines.append(f"Total Rooms: {conn['total_rooms']}")
            report_lines.append(f"Connected Components: {conn['connectivity_stats']['total_components']}")
            report_lines.append(f"Largest Component: {conn['connectivity_stats']['largest_component']} rooms")
            report_lines.append(f"Isolated Rooms: {conn['connectivity_stats']['isolated_rooms']}")
            report_lines.append("")

            # Exit distribution
            report_lines.append("Exit Distribution:")
            for exit_count, room_count in sorted(conn["exit_distribution"].items()):
                report_lines.append(f"  {exit_count} exits: {room_count} rooms")
            report_lines.append("")

        # Environment Analysis
        if "environment" in analysis_results:
            env = analysis_results["environment"]
            report_lines.append("🌍 ENVIRONMENT ANALYSIS")
            report_lines.append("-" * 40)

            for env_type, count in sorted(env["environment_counts"].items(), key=lambda x: x[1], reverse=True):
                report_lines.append(f"{env_type}: {count} rooms")
                examples = env["environment_examples"][env_type][:3]
                if examples:
                    report_lines.append(f"  Examples: {', '.join(examples)}")
            report_lines.append("")

        # Zone Analysis
        if "zones" in analysis_results:
            zones = analysis_results["zones"]
            report_lines.append("🗺️  ZONE ANALYSIS")
            report_lines.append("-" * 40)

            for zone, data in sorted(zones.items()):
                report_lines.append(f"{zone}: {data['room_count']} rooms, {len(data['subzones'])} subzones")
                for subzone in sorted(data["subzones"]):
                    subzone_data = zones["subzone_stats"][subzone]
                    report_lines.append(f"  {subzone}: {subzone_data['room_count']} rooms")
            report_lines.append("")

        return "\n".join(report_lines)

    def generate_json_report(self, analysis_results: dict[str, Any]) -> str:
        """Generate JSON-formatted analysis report"""
        return json.dumps(analysis_results, indent=2, ensure_ascii=False)

    def generate_html_report(self, analysis_results: dict[str, Any]) -> str:
        """Generate HTML-formatted analysis report"""
        html = []
        html.append("<!DOCTYPE html>")
        html.append("<html>")
        html.append("<head>")
        html.append("<title>MythosMUD Room Analysis Report</title>")
        html.append("<style>")
        html.append("body { font-family: Arial, sans-serif; margin: 20px; }")
        html.append("h1, h2 { color: #333; }")
        html.append("table { border-collapse: collapse; width: 100%; margin: 10px 0; }")
        html.append("th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }")
        html.append("th { background-color: #f2f2f2; }")
        html.append(".section { margin: 20px 0; }")
        html.append("</style>")
        html.append("</head>")
        html.append("<body>")

        html.append("<h1>MythosMUD Room Analysis Report</h1>")

        # Connectivity Section
        if "connectivity" in analysis_results:
            conn = analysis_results["connectivity"]
            html.append('<div class="section">')
            html.append("<h2>Connectivity Analysis</h2>")
            html.append(f"<p><strong>Total Rooms:</strong> {conn['total_rooms']}</p>")
            html.append(
                f"<p><strong>Connected Components:</strong> {conn['connectivity_stats']['total_components']}</p>"
            )
            html.append(
                f"<p><strong>Largest Component:</strong> {conn['connectivity_stats']['largest_component']} rooms</p>"
            )
            html.append(f"<p><strong>Isolated Rooms:</strong> {conn['connectivity_stats']['isolated_rooms']}</p>")
            html.append("</div>")

        # Environment Section
        if "environment" in analysis_results:
            env = analysis_results["environment"]
            html.append('<div class="section">')
            html.append("<h2>Environment Analysis</h2>")
            html.append("<table>")
            html.append("<tr><th>Environment</th><th>Count</th><th>Examples</th></tr>")

            for env_type, count in sorted(env["environment_counts"].items(), key=lambda x: x[1], reverse=True):
                examples = env["environment_examples"][env_type][:3]
                examples_str = ", ".join(examples) if examples else "None"
                html.append(f"<tr><td>{env_type}</td><td>{count}</td><td>{examples_str}</td></tr>")

            html.append("</table>")
            html.append("</div>")

        # Zone Section
        if "zones" in analysis_results:
            zones = analysis_results["zones"]
            html.append('<div class="section">')
            html.append("<h2>Zone Analysis</h2>")
            html.append("<table>")
            html.append("<tr><th>Zone</th><th>Subzones</th><th>Rooms</th></tr>")

            for zone, data in sorted(zones.items()):
                subzones_str = ", ".join(sorted(data["subzones"]))
                html.append(f"<tr><td>{zone}</td><td>{subzones_str}</td><td>{data['room_count']}</td></tr>")

            html.append("</table>")
            html.append("</div>")

        html.append("</body>")
        html.append("</html>")

        return "\n".join(html)
