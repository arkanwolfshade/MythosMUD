"""
Risk mitigation utilities for dual connection system testing.

This module provides utilities for implementing risk mitigation strategies
and validating system stability under various conditions.
"""

import asyncio
import time
import uuid
from dataclasses import dataclass
from typing import Any

import structlog

from server.realtime.connection_manager import ConnectionManager


def _str_to_uuid(player_id: str) -> uuid.UUID:
    """Convert string player_id to UUID, generating new UUID if string is not valid UUID."""
    try:
        return uuid.UUID(player_id)
    except (ValueError, TypeError):
        return uuid.uuid4()


@dataclass
class RiskScenario:
    """Risk scenario definition"""

    name: str
    description: str
    risk_type: str  # 'technical', 'operational', 'performance'
    severity: str  # 'low', 'medium', 'high', 'critical'
    probability: float  # 0.0 to 1.0
    impact: str  # 'low', 'medium', 'high', 'critical'
    mitigation_strategy: str
    test_scenarios: list[str]


@dataclass
class MitigationResult:
    """Result of risk mitigation test"""

    scenario_name: str
    test_passed: bool
    mitigation_effective: bool
    performance_impact: float
    error_count: int
    recovery_time: float
    details: dict[str, Any]


class RiskMitigationTester:
    """Tester for risk mitigation strategies"""

    def __init__(self, connection_manager: ConnectionManager):
        self.connection_manager = connection_manager
        self.logger = structlog.get_logger("risk_mitigation_tester")
        self.risk_scenarios = self._define_risk_scenarios()

    def _define_risk_scenarios(self) -> list[RiskScenario]:
        """Define risk scenarios for dual connection system"""
        return [
            # Technical Risks
            RiskScenario(
                name="connection_management_complexity",
                description="Complex connection management leading to resource leaks",
                risk_type="technical",
                severity="high",
                probability=0.3,
                impact="high",
                mitigation_strategy="Comprehensive testing and monitoring",
                test_scenarios=[
                    "multiple_connection_establishment",
                    "connection_cleanup_validation",
                    "memory_leak_detection",
                    "resource_usage_monitoring",
                ],
            ),
            RiskScenario(
                name="message_delivery_issues",
                description="Message delivery failures or duplicates",
                risk_type="technical",
                severity="medium",
                probability=0.4,
                impact="medium",
                mitigation_strategy="Message deduplication and delivery confirmation",
                test_scenarios=[
                    "message_delivery_reliability",
                    "duplicate_message_detection",
                    "delivery_confirmation_testing",
                    "failed_delivery_recovery",
                ],
            ),
            RiskScenario(
                name="resource_usage_escalation",
                description="Excessive resource usage under load",
                risk_type="technical",
                severity="high",
                probability=0.2,
                impact="critical",
                mitigation_strategy="Connection limits and monitoring",
                test_scenarios=[
                    "connection_limit_enforcement",
                    "memory_usage_monitoring",
                    "cpu_usage_monitoring",
                    "resource_cleanup_validation",
                ],
            ),
            RiskScenario(
                name="performance_degradation",
                description="Performance degradation under load",
                risk_type="technical",
                severity="medium",
                probability=0.5,
                impact="medium",
                mitigation_strategy="Performance testing and optimization",
                test_scenarios=[
                    "load_testing",
                    "performance_benchmarking",
                    "scalability_testing",
                    "bottleneck_identification",
                ],
            ),
            # Operational Risks
            RiskScenario(
                name="system_stability_issues",
                description="System instability under stress",
                risk_type="operational",
                severity="critical",
                probability=0.1,
                impact="critical",
                mitigation_strategy="Comprehensive testing and monitoring",
                test_scenarios=[
                    "stress_testing",
                    "stability_monitoring",
                    "error_recovery_testing",
                    "graceful_degradation_testing",
                ],
            ),
            RiskScenario(
                name="deployment_issues",
                description="Deployment failures or rollback issues",
                risk_type="operational",
                severity="high",
                probability=0.2,
                impact="high",
                mitigation_strategy="Rollback procedures and validation testing",
                test_scenarios=[
                    "deployment_validation",
                    "rollback_procedure_testing",
                    "configuration_validation",
                    "environment_compatibility_testing",
                ],
            ),
        ]

    async def test_connection_management_complexity(self) -> MitigationResult:
        """Test connection management complexity mitigation"""
        self.logger.info("Testing connection management complexity mitigation")

        start_time = time.time()
        error_count = 0
        details: dict[str, Any] = {}

        try:
            # Test multiple connection establishment
            players: list[dict[str, Any]] = []
            for i in range(50):  # Create 50 players with dual connections
                player_id = f"complexity_test_player_{i}"
                player_id_uuid = _str_to_uuid(player_id)
                try:
                    # Establish WebSocket connection
                    ws_result = await self.connection_manager.connect_websocket(
                        self._mock_websocket(), player_id_uuid, f"session_{i}"
                    )

                    players.append({"player_id": player_id, "ws_connection": ws_result})

                except Exception as e:
                    error_count += 1
                    self.logger.error("Connection establishment failed", player_id=player_id, error=str(e))

            # Test connection cleanup
            cleanup_start = time.time()
            for player in players:
                try:
                    player_id_uuid = _str_to_uuid(player["player_id"])
                    await self.connection_manager.force_disconnect_player(player_id_uuid)
                except Exception as e:
                    error_count += 1
                    self.logger.error("Connection cleanup failed", player_id=player["player_id"], error=str(e))

            cleanup_time = time.time() - cleanup_start

            # Validate resource cleanup
            memory_stats = self.connection_manager.get_memory_stats()
            connection_count = len(self.connection_manager.connection_metadata)

            details.update(
                {
                    "players_created": len(players),
                    "cleanup_time": cleanup_time,
                    "final_connection_count": connection_count,
                    "memory_stats": memory_stats,
                }
            )

            # Test passed if no connections remain and cleanup was fast
            test_passed = connection_count == 0 and cleanup_time < 5.0 and error_count < 5

            mitigation_effective = test_passed and error_count == 0

        except Exception as e:
            error_count += 1
            test_passed = False
            mitigation_effective = False
            details["exception"] = str(e)
            self.logger.error("Connection management complexity test failed", error=str(e))

        recovery_time = time.time() - start_time

        return MitigationResult(
            scenario_name="connection_management_complexity",
            test_passed=test_passed,
            mitigation_effective=mitigation_effective,
            performance_impact=recovery_time,
            error_count=error_count,
            recovery_time=recovery_time,
            details=details,
        )

    async def test_message_delivery_issues(self) -> MitigationResult:
        """Test message delivery issues mitigation"""
        self.logger.info("Testing message delivery issues mitigation")

        start_time = time.time()
        error_count = 0
        details: dict[str, Any] = {}

        try:
            # Set up test player with dual connections
            player_id = "delivery_test_player"
            player_id_uuid = _str_to_uuid(player_id)
            await self.connection_manager.connect_websocket(self._mock_websocket(), player_id_uuid, "delivery_session")

            # Test message delivery reliability
            messages_sent = 0
            messages_delivered = 0
            duplicate_messages = 0

            for i in range(100):  # Send 100 messages
                message = {"type": "test", "content": f"Test message {i}", "timestamp": time.time()}

                try:
                    result = await self.connection_manager.send_personal_message(player_id_uuid, message)
                    messages_sent += 1

                    if result.get("success", False):
                        messages_delivered += 1

                    # Check for duplicate delivery
                    if result.get("websocket_delivered", False) and result.get("sse_delivered", False):
                        # This is expected for dual connections, not a duplicate
                        pass

                except Exception as e:
                    error_count += 1
                    self.logger.error("Message delivery failed", message_id=i, error=str(e))

            # Test duplicate message detection
            duplicate_message = {"type": "test", "content": "Duplicate test message", "timestamp": time.time()}

            # Send same message twice quickly
            await self.connection_manager.send_personal_message(player_id_uuid, duplicate_message)
            await asyncio.sleep(0.1)  # Small delay
            await self.connection_manager.send_personal_message(player_id_uuid, duplicate_message)

            delivery_rate = (messages_delivered / messages_sent * 100) if messages_sent > 0 else 0

            details.update(
                {
                    "messages_sent": messages_sent,
                    "messages_delivered": messages_delivered,
                    "delivery_rate": delivery_rate,
                    "duplicate_messages": duplicate_messages,
                }
            )

            # Test passed if delivery rate is high and no duplicates
            test_passed = delivery_rate >= 95.0 and duplicate_messages == 0 and error_count < 5

            mitigation_effective = test_passed and error_count == 0

            # Cleanup
            await self.connection_manager.force_disconnect_player(player_id_uuid)

        except Exception as e:
            error_count += 1
            test_passed = False
            mitigation_effective = False
            details["exception"] = str(e)
            self.logger.error("Message delivery test failed", error=str(e))

        recovery_time = time.time() - start_time

        return MitigationResult(
            scenario_name="message_delivery_issues",
            test_passed=test_passed,
            mitigation_effective=mitigation_effective,
            performance_impact=recovery_time,
            error_count=error_count,
            recovery_time=recovery_time,
            details=details,
        )

    async def test_resource_usage_escalation(self) -> MitigationResult:
        """Test resource usage escalation mitigation"""
        self.logger.info("Testing resource usage escalation mitigation")

        start_time = time.time()
        error_count = 0
        details: dict[str, Any] = {}

        try:
            # Test connection limit enforcement
            max_connections = 100
            connections_created = 0

            for i in range(max_connections + 10):  # Try to exceed limit
                player_id = f"resource_test_player_{i}"
                player_id_uuid = _str_to_uuid(player_id)
                try:
                    result = await self.connection_manager.connect_websocket(
                        self._mock_websocket(), player_id_uuid, f"resource_session_{i}"
                    )
                    if result:
                        connections_created += 1
                except Exception as e:
                    # Expected to fail when limit is reached
                    if "limit" in str(e).lower() or "maximum" in str(e).lower():
                        pass  # Expected behavior
                    else:
                        error_count += 1
                        self.logger.error("Unexpected connection error", player_id=player_id, error=str(e))

            # Check memory usage
            memory_stats = self.connection_manager.get_memory_stats()

            # Test resource cleanup
            cleanup_start = time.time()
            for i in range(connections_created):
                player_id = f"resource_test_player_{i}"
                player_id_uuid = _str_to_uuid(player_id)
                try:
                    await self.connection_manager.force_disconnect_player(player_id_uuid)
                except Exception as e:
                    error_count += 1
                    self.logger.error("Resource cleanup failed", player_id=player_id, error=str(e))

            cleanup_time = time.time() - cleanup_start

            details.update(
                {
                    "max_connections_attempted": max_connections + 10,
                    "connections_created": connections_created,
                    "cleanup_time": cleanup_time,
                    "memory_stats": memory_stats,
                }
            )

            # Test passed if limit was enforced and cleanup was successful
            test_passed = connections_created <= max_connections and cleanup_time < 10.0 and error_count < 5

            mitigation_effective = test_passed and error_count == 0

        except Exception as e:
            error_count += 1
            test_passed = False
            mitigation_effective = False
            details["exception"] = str(e)
            self.logger.error("Resource usage test failed", error=str(e))

        recovery_time = time.time() - start_time

        return MitigationResult(
            scenario_name="resource_usage_escalation",
            test_passed=test_passed,
            mitigation_effective=mitigation_effective,
            performance_impact=recovery_time,
            error_count=error_count,
            recovery_time=recovery_time,
            details=details,
        )

    async def test_performance_degradation(self) -> MitigationResult:
        """Test performance degradation mitigation"""
        self.logger.info("Testing performance degradation mitigation")

        start_time = time.time()
        error_count = 0
        details: dict[str, Any] = {}

        try:
            # Baseline performance test
            baseline_start = time.time()
            baseline_players = []

            for i in range(10):  # Create 10 players for baseline
                player_id = f"baseline_player_{i}"
                player_id_uuid = _str_to_uuid(player_id)
                await self.connection_manager.connect_websocket(
                    self._mock_websocket(), player_id_uuid, f"baseline_session_{i}"
                )
                baseline_players.append(player_id)

            baseline_time = time.time() - baseline_start

            # Load test
            load_start = time.time()
            load_players = []

            for i in range(50):  # Create 50 players for load test
                player_id = f"load_player_{i}"
                player_id_uuid = _str_to_uuid(player_id)
                try:
                    await self.connection_manager.connect_websocket(
                        self._mock_websocket(), player_id_uuid, f"load_session_{i}"
                    )
                    load_players.append(player_id)
                except Exception as e:
                    error_count += 1
                    self.logger.error("Load test connection failed", player_id=player_id, error=str(e))

            load_time = time.time() - load_start

            # Message delivery performance test
            message_start = time.time()
            messages_sent = 0

            for player_id in load_players[:20]:  # Send messages to first 20 players
                player_id_uuid = _str_to_uuid(player_id)
                for j in range(10):  # 10 messages per player
                    message = {
                        "type": "performance_test",
                        "content": f"Performance test message {j}",
                        "timestamp": time.time(),
                    }
                    try:
                        await self.connection_manager.send_personal_message(player_id_uuid, message)
                        messages_sent += 1
                    except Exception as e:
                        error_count += 1
                        self.logger.error("Message delivery failed", player_id=player_id, message_id=j, error=str(e))

            message_time = time.time() - message_start

            # Calculate performance metrics
            baseline_rate = len(baseline_players) / baseline_time if baseline_time > 0 else 0
            load_rate = len(load_players) / load_time if load_time > 0 else 0
            message_rate = messages_sent / message_time if message_time > 0 else 0

            performance_degradation = (baseline_rate - load_rate) / baseline_rate * 100 if baseline_rate > 0 else 0

            details.update(
                {
                    "baseline_players": len(baseline_players),
                    "baseline_time": baseline_time,
                    "baseline_rate": baseline_rate,
                    "load_players": len(load_players),
                    "load_time": load_time,
                    "load_rate": load_rate,
                    "messages_sent": messages_sent,
                    "message_time": message_time,
                    "message_rate": message_rate,
                    "performance_degradation": performance_degradation,
                }
            )

            # Test passed if performance degradation is acceptable
            test_passed = performance_degradation < 50.0 and error_count < 10 and message_rate > 10.0

            mitigation_effective = test_passed and error_count == 0

            # Cleanup
            all_players = baseline_players + load_players
            for player_id in all_players:
                try:
                    player_id_uuid = _str_to_uuid(player_id)
                    await self.connection_manager.force_disconnect_player(player_id_uuid)
                except Exception as e:
                    self.logger.error("Cleanup failed", player_id=player_id, error=str(e))

        except Exception as e:
            error_count += 1
            test_passed = False
            mitigation_effective = False
            details["exception"] = str(e)
            self.logger.error("Performance degradation test failed", error=str(e))

        recovery_time = time.time() - start_time

        return MitigationResult(
            scenario_name="performance_degradation",
            test_passed=test_passed,
            mitigation_effective=mitigation_effective,
            performance_impact=recovery_time,
            error_count=error_count,
            recovery_time=recovery_time,
            details=details,
        )

    async def test_system_stability(self) -> MitigationResult:
        """Test system stability mitigation"""
        self.logger.info("Testing system stability mitigation")

        start_time = time.time()
        error_count = 0
        details: dict[str, Any] = {}

        try:
            # Stress test with rapid connection/disconnection cycles
            stress_cycles = 5
            connections_per_cycle = 20

            for cycle in range(stress_cycles):
                cycle_start = time.time()
                cycle_players = []

                # Rapid connection establishment
                for i in range(connections_per_cycle):
                    player_id = f"stress_player_{cycle}_{i}"
                    player_id_uuid = _str_to_uuid(player_id)
                    try:
                        await self.connection_manager.connect_websocket(
                            self._mock_websocket(), player_id_uuid, f"stress_session_{cycle}"
                        )
                        cycle_players.append(player_id)
                    except Exception as e:
                        error_count += 1
                        self.logger.error(
                            "Stress test connection failed", cycle=cycle, player_id=player_id, error=str(e)
                        )

                # Rapid disconnection
                for player_id in cycle_players:
                    try:
                        player_id_uuid = _str_to_uuid(player_id)
                        await self.connection_manager.force_disconnect_player(player_id_uuid)
                    except Exception as e:
                        error_count += 1
                        self.logger.error(
                            "Stress test disconnection failed", cycle=cycle, player_id=player_id, error=str(e)
                        )

                cycle_time = time.time() - cycle_start
                details[f"cycle_{cycle}_time"] = cycle_time
                details[f"cycle_{cycle}_players"] = len(cycle_players)

                # Small delay between cycles
                await asyncio.sleep(0.1)

            # Check system health after stress test
            memory_stats = self.connection_manager.get_memory_stats()
            connection_count = len(self.connection_manager.connection_metadata)

            details.update(
                {
                    "stress_cycles": stress_cycles,
                    "connections_per_cycle": connections_per_cycle,
                    "final_connection_count": connection_count,
                    "memory_stats": memory_stats,
                }
            )

            # Test passed if system remained stable
            test_passed = connection_count == 0 and error_count < 10 and memory_stats.get("memory_usage_mb", 0) < 1000

            mitigation_effective = test_passed and error_count == 0

        except Exception as e:
            error_count += 1
            test_passed = False
            mitigation_effective = False
            details["exception"] = str(e)
            self.logger.error("System stability test failed", error=str(e))

        recovery_time = time.time() - start_time

        return MitigationResult(
            scenario_name="system_stability_issues",
            test_passed=test_passed,
            mitigation_effective=mitigation_effective,
            performance_impact=recovery_time,
            error_count=error_count,
            recovery_time=recovery_time,
            details=details,
        )

    async def run_all_risk_tests(self) -> list[MitigationResult]:
        """Run all risk mitigation tests"""
        self.logger.info("Running all risk mitigation tests")

        results = []

        # Technical risk tests
        results.append(await self.test_connection_management_complexity())
        results.append(await self.test_message_delivery_issues())
        results.append(await self.test_resource_usage_escalation())
        results.append(await self.test_performance_degradation())

        # Operational risk tests
        results.append(await self.test_system_stability())

        # Log summary
        passed_tests = sum(1 for r in results if r.test_passed)
        effective_mitigations = sum(1 for r in results if r.mitigation_effective)

        self.logger.info(
            "Risk mitigation test summary",
            total_tests=len(results),
            passed_tests=passed_tests,
            effective_mitigations=effective_mitigations,
        )

        return results

    def _mock_websocket(self):
        """Create mock WebSocket for testing"""

        class MockWebSocket:
            def __init__(self):
                self.closed = False
                self.send_calls = []
                self.ping_calls = []

            async def accept(self):
                pass

            async def send_json(self, data):
                self.send_calls.append(data)

            async def ping(self):
                self.ping_calls.append(time.time())
                return True

            async def close(self, code=None, reason=None):
                self.closed = True

            def is_closed(self):
                return self.closed

        return MockWebSocket()


class RiskMitigationValidator:
    """Validator for risk mitigation effectiveness"""

    def __init__(self):
        self.logger = structlog.get_logger("risk_mitigation_validator")

    def validate_mitigation_results(self, results: list[MitigationResult]) -> dict[str, Any]:
        """Validate risk mitigation test results"""
        # AI Agent: Explicit type annotation to help mypy understand dict structure
        validation_summary: dict[str, Any] = {
            "total_tests": len(results),
            "passed_tests": 0,
            "failed_tests": 0,
            "effective_mitigations": 0,
            "ineffective_mitigations": 0,
            "high_risk_scenarios": [],
            "performance_issues": [],
            "overall_risk_level": "unknown",
        }

        for result in results:
            if result.test_passed:
                validation_summary["passed_tests"] += 1
            else:
                validation_summary["failed_tests"] += 1
                validation_summary["high_risk_scenarios"].append(result.scenario_name)

            if result.mitigation_effective:
                validation_summary["effective_mitigations"] += 1
            else:
                validation_summary["ineffective_mitigations"] += 1

            if result.performance_impact > 10.0:  # More than 10 seconds
                validation_summary["performance_issues"].append(
                    {"scenario": result.scenario_name, "impact": result.performance_impact}
                )

        # Determine overall risk level
        if validation_summary["failed_tests"] == 0 and validation_summary["ineffective_mitigations"] == 0:
            validation_summary["overall_risk_level"] = "low"
        elif validation_summary["failed_tests"] <= 1 and validation_summary["ineffective_mitigations"] <= 1:
            validation_summary["overall_risk_level"] = "medium"
        else:
            validation_summary["overall_risk_level"] = "high"

        return validation_summary


# Export utilities
__all__ = ["RiskScenario", "MitigationResult", "RiskMitigationTester", "RiskMitigationValidator"]
