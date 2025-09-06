"""
Comprehensive test suite for dual connection system testing strategy.

This module integrates all testing strategy components including test data management,
test environment setup, risk mitigation, and success criteria validation.
"""

import time

import pytest

from server.tests.data.dual_connection_test_data import (
    DualConnectionTestData,
    ErrorTestData,
    PerformanceTestData,
    ScenarioTestData,
)
from server.tests.utils.risk_mitigation import RiskMitigationTester, RiskMitigationValidator
from server.tests.utils.success_criteria_validator import SuccessCriteriaValidator, SuccessLevel
from server.tests.utils.test_environment import TestCleanup, TestDataSetup, TestMonitoringSetup


class TestDualConnectionTestingStrategy:
    """Test suite for dual connection system testing strategy"""

    @pytest.fixture
    async def test_environment(self):
        """Set up test environment for testing strategy validation"""
        from server.tests.utils.test_environment import test_environment

        async with test_environment as env:
            yield env

    @pytest.fixture
    def test_data(self):
        """Set up test data for testing strategy validation"""
        return DualConnectionTestData()

    @pytest.fixture
    def risk_tester(self, test_environment):
        """Set up risk mitigation tester"""
        return RiskMitigationTester(test_environment.connection_manager)

    @pytest.fixture
    def success_validator(self, test_environment):
        """Set up success criteria validator"""
        return SuccessCriteriaValidator(test_environment.connection_manager)

    # Test Data Management Tests

    def test_test_data_generation(self, test_data):
        """Test that test data is generated correctly"""
        # Test basic data generation
        assert len(test_data.players) > 0
        assert len(test_data.connections) > 0
        assert len(test_data.sessions) > 0
        assert len(test_data.messages) > 0

        # Test data statistics
        stats = test_data.get_statistics()
        assert stats["total_players"] > 0
        assert stats["total_connections"] > 0
        assert stats["total_sessions"] > 0
        assert stats["total_messages"] > 0

        # Test data filtering
        dual_players = test_data.get_players_by_connection_type("dual")
        assert len(dual_players) > 0

        websocket_connections = test_data.get_connections_by_type("websocket")
        assert len(websocket_connections) > 0

        sse_connections = test_data.get_connections_by_type("sse")
        assert len(sse_connections) > 0

    def test_performance_test_data_generation(self):
        """Test performance test data generation"""
        # Test load test data
        load_players = PerformanceTestData.generate_load_test_players(50)
        assert len(load_players) == 50

        # Test stress test data
        stress_connections = PerformanceTestData.generate_stress_test_connections(20, 4)
        assert len(stress_connections) == 80  # 20 players * 4 connections each

        # Test message burst data
        message_burst = PerformanceTestData.generate_message_burst(100, "test_player")
        assert len(message_burst) == 100

    def test_error_test_data_generation(self):
        """Test error test data generation"""
        # Test authentication errors
        auth_errors = ErrorTestData.get_authentication_errors()
        assert len(auth_errors) > 0
        assert all("error_type" in error for error in auth_errors)

        # Test connection errors
        conn_errors = ErrorTestData.get_connection_errors()
        assert len(conn_errors) > 0
        assert all("connection_type" in error for error in conn_errors)

        # Test session errors
        session_errors = ErrorTestData.get_session_errors()
        assert len(session_errors) > 0
        assert all("session_id" in error for error in session_errors)

    def test_scenario_test_data_generation(self):
        """Test scenario test data generation"""
        # Test dual connection scenario
        dual_scenario = ScenarioTestData.get_dual_connection_scenario()
        assert "player_id" in dual_scenario
        assert "websocket_connection" in dual_scenario
        assert "sse_connection" in dual_scenario

        # Test session switch scenario
        session_scenario = ScenarioTestData.get_session_switch_scenario()
        assert "player_id" in session_scenario
        assert "old_session" in session_scenario
        assert "new_session" in session_scenario

        # Test connection cleanup scenario
        cleanup_scenario = ScenarioTestData.get_connection_cleanup_scenario()
        assert "player_id" in cleanup_scenario
        assert "healthy_connections" in cleanup_scenario
        assert "unhealthy_connections" in cleanup_scenario

    # Test Environment Setup Tests

    @pytest.mark.asyncio
    async def test_test_environment_setup(self):
        """Test test environment setup"""
        # Create test environment
        from server.tests.utils.test_environment import test_environment_context

        async with test_environment_context("test_setup") as env:
            # Test environment initialization
            assert env.connection_manager is not None
            assert env.config is not None

            # Test configuration
            config = env.get_test_config()
            assert "dual_connections" in config
            assert config["dual_connections"]["enabled"] is True

            # Test database path
            db_path = env.get_database_path()
            assert db_path is not None
            assert db_path.endswith(".db")

    @pytest.mark.asyncio
    async def test_dual_connection_scenario_setup(self, test_environment):
        """Test dual connection scenario setup"""
        # Set up dual connection scenario
        scenario = await TestDataSetup.setup_dual_connection_scenario(test_environment, "test_dual_player")

        assert scenario["player_id"] == "test_dual_player"
        assert scenario["websocket_connection_id"] is not None
        assert scenario["sse_connection_id"] is not None
        assert scenario["session_id"] == "test_session"

        # Verify connections exist
        player_connections = test_environment.connection_manager.get_connections_by_player("test_dual_player")
        assert len(player_connections) == 2

        # Cleanup
        await TestCleanup.cleanup_player_data(test_environment, "test_dual_player")

    @pytest.mark.asyncio
    async def test_multiple_players_setup(self, test_environment):
        """Test multiple players setup"""
        # Set up multiple players
        players = await TestDataSetup.setup_multiple_players(test_environment, 5)

        assert len(players) == 5

        for i, player in enumerate(players):
            assert player["player_id"] == f"test_player_{i}"
            assert player["websocket_connection_id"] is not None
            assert player["sse_connection_id"] is not None

        # Cleanup
        for player in players:
            await TestCleanup.cleanup_player_data(test_environment, player["player_id"])

    @pytest.mark.asyncio
    async def test_session_switch_scenario_setup(self, test_environment):
        """Test session switch scenario setup"""
        # Set up session switch scenario
        scenario = await TestDataSetup.setup_session_switch_scenario(test_environment, "test_session_player")

        assert scenario["player_id"] == "test_session_player"
        assert scenario["old_session_id"] == "test_session"
        assert scenario["new_session_id"] == "new_test_session"
        assert len(scenario["old_connections"]) == 2

        # Cleanup
        await TestCleanup.cleanup_player_data(test_environment, "test_session_player")

    @pytest.mark.asyncio
    async def test_monitoring_setup(self, test_environment):
        """Test monitoring setup"""
        # Set up monitoring endpoints
        monitoring = await TestMonitoringSetup.setup_monitoring_endpoints(test_environment)

        assert monitoring["monitoring_enabled"] is True
        assert "metrics_endpoint" in monitoring
        assert "health_endpoint" in monitoring

        # Set up performance monitoring
        perf_monitoring = await TestMonitoringSetup.setup_performance_monitoring(test_environment)

        assert perf_monitoring["performance_monitoring_enabled"] is True
        assert perf_monitoring["connection_establishment_tracking"] is True
        assert perf_monitoring["message_delivery_tracking"] is True

    # Risk Mitigation Tests

    @pytest.mark.asyncio
    async def test_connection_management_complexity_mitigation(self, risk_tester):
        """Test connection management complexity mitigation"""
        result = await risk_tester.test_connection_management_complexity()

        assert result.scenario_name == "connection_management_complexity"
        assert result.test_passed is True
        assert result.mitigation_effective is True
        assert result.error_count == 0
        assert result.performance_impact < 10.0  # Should complete within 10 seconds

        # Verify details
        assert "players_created" in result.details
        assert "cleanup_time" in result.details
        assert "final_connection_count" in result.details
        assert result.details["final_connection_count"] == 0

    @pytest.mark.asyncio
    async def test_message_delivery_issues_mitigation(self, risk_tester):
        """Test message delivery issues mitigation"""
        result = await risk_tester.test_message_delivery_issues()

        assert result.scenario_name == "message_delivery_issues"
        assert result.test_passed is True
        assert result.mitigation_effective is True
        assert result.error_count == 0

        # Verify delivery rate
        assert result.details["delivery_rate"] >= 95.0

    @pytest.mark.asyncio
    async def test_resource_usage_escalation_mitigation(self, risk_tester):
        """Test resource usage escalation mitigation"""
        result = await risk_tester.test_resource_usage_escalation()

        assert result.scenario_name == "resource_usage_escalation"
        assert result.test_passed is True
        assert result.mitigation_effective is True
        assert result.error_count == 0

        # Verify connection limits were enforced
        assert result.details["connections_created"] <= result.details["max_connections_attempted"]

    @pytest.mark.asyncio
    async def test_performance_degradation_mitigation(self, risk_tester):
        """Test performance degradation mitigation"""
        result = await risk_tester.test_performance_degradation()

        assert result.scenario_name == "performance_degradation"
        assert result.test_passed is True
        assert result.mitigation_effective is True
        assert result.error_count == 0

        # Verify performance metrics
        assert result.details["performance_degradation"] < 50.0
        assert result.details["message_rate"] > 10.0

    @pytest.mark.asyncio
    async def test_system_stability_mitigation(self, risk_tester):
        """Test system stability mitigation"""
        result = await risk_tester.test_system_stability()

        assert result.scenario_name == "system_stability_issues"
        assert result.test_passed is True
        assert result.mitigation_effective is True
        assert result.error_count == 0

        # Verify system remained stable
        assert result.details["final_connection_count"] == 0
        assert result.details["memory_stats"]["memory_usage_mb"] < 1000

    @pytest.mark.asyncio
    async def test_all_risk_mitigation_tests(self, risk_tester):
        """Test all risk mitigation tests"""
        results = await risk_tester.run_all_risk_tests()

        assert len(results) == 5  # Should have 5 risk tests

        # All tests should pass
        for result in results:
            assert result.test_passed is True
            assert result.mitigation_effective is True
            assert result.error_count == 0

        # Validate results
        validator = RiskMitigationValidator()
        validation_summary = validator.validate_mitigation_results(results)

        assert validation_summary["total_tests"] == 5
        assert validation_summary["passed_tests"] == 5
        assert validation_summary["failed_tests"] == 0
        assert validation_summary["effective_mitigations"] == 5
        assert validation_summary["overall_risk_level"] == "low"

    # Success Criteria Validation Tests

    @pytest.mark.asyncio
    async def test_dual_connection_support_validation(self, success_validator):
        """Test dual connection support validation"""
        await success_validator.validate_all_criteria()

        # Find dual connection support result
        dual_connection_result = None
        for result in success_validator.validation_results:
            if result.criteria_name == "dual_connection_support":
                dual_connection_result = result
                break

        assert dual_connection_result is not None
        assert dual_connection_result.level == SuccessLevel.PASSED
        assert dual_connection_result.score == 1.0
        assert dual_connection_result.details["both_connection_types_active"] is True
        assert dual_connection_result.details["both_connections_received_message"] is True

    @pytest.mark.asyncio
    async def test_message_delivery_validation(self, success_validator):
        """Test message delivery validation"""
        await success_validator.validate_all_criteria()

        # Find message delivery result
        message_delivery_result = None
        for result in success_validator.validation_results:
            if result.criteria_name == "message_delivery_to_all_connections":
                message_delivery_result = result
                break

        assert message_delivery_result is not None
        assert message_delivery_result.level == SuccessLevel.PASSED
        assert message_delivery_result.score == 1.0
        assert message_delivery_result.details["delivery_rate"] >= 95.0

    @pytest.mark.asyncio
    async def test_connection_persistence_validation(self, success_validator):
        """Test connection persistence validation"""
        await success_validator.validate_all_criteria()

        # Find connection persistence result
        persistence_result = None
        for result in success_validator.validation_results:
            if result.criteria_name == "connection_persistence":
                persistence_result = result
                break

        assert persistence_result is not None
        assert persistence_result.level == SuccessLevel.PASSED
        assert persistence_result.score == 1.0
        assert persistence_result.details["connections_after_wait"] >= 2

    @pytest.mark.asyncio
    async def test_disconnection_rules_validation(self, success_validator):
        """Test disconnection rules validation"""
        await success_validator.validate_all_criteria()

        # Find disconnection rules result
        disconnection_result = None
        for result in success_validator.validation_results:
            if result.criteria_name == "disconnection_rules":
                disconnection_result = result
                break

        assert disconnection_result is not None
        assert disconnection_result.level == SuccessLevel.PASSED
        assert disconnection_result.score == 1.0
        assert disconnection_result.details["connections_after_force_disconnect"] == 0

    @pytest.mark.asyncio
    async def test_performance_criteria_validation(self, success_validator):
        """Test performance criteria validation"""
        await success_validator.validate_all_criteria()

        # Check performance category results
        performance_results = [r for r in success_validator.validation_results if r.category == "performance"]

        assert len(performance_results) == 4  # Should have 4 performance criteria

        for result in performance_results:
            assert result.level == SuccessLevel.PASSED
            assert result.score >= 0.7  # At least partial success

    @pytest.mark.asyncio
    async def test_quality_criteria_validation(self, success_validator):
        """Test quality criteria validation"""
        await success_validator.validate_all_criteria()

        # Check quality category results
        quality_results = [r for r in success_validator.validation_results if r.category == "quality"]

        assert len(quality_results) == 3  # Should have 3 quality criteria

        for result in quality_results:
            assert result.level == SuccessLevel.PASSED
            assert result.score >= 0.7  # At least partial success

    @pytest.mark.asyncio
    async def test_comprehensive_success_criteria_validation(self, success_validator):
        """Test comprehensive success criteria validation"""
        summary = await success_validator.validate_all_criteria()

        # Verify summary structure
        assert summary.total_criteria > 0
        assert summary.passed_criteria > 0
        assert summary.overall_score > 0.0
        assert len(summary.category_scores) > 0

        # Verify all categories have scores
        expected_categories = ["functional", "performance", "quality"]
        for category in expected_categories:
            assert category in summary.category_scores
            assert summary.category_scores[category] > 0.0

        # Verify overall success
        assert summary.overall_score >= 0.8  # At least 80% overall success
        assert len(summary.critical_issues) == 0  # No critical issues

    # Integration Tests

    @pytest.mark.asyncio
    async def test_full_testing_strategy_integration(self, test_environment, test_data, risk_tester, success_validator):
        """Test full testing strategy integration"""
        # This test integrates all components of the testing strategy

        # 1. Test data management
        assert len(test_data.players) > 0
        assert len(test_data.connections) > 0

        # 2. Test environment setup
        assert test_environment.connection_manager is not None

        # 3. Risk mitigation testing
        risk_results = await risk_tester.run_all_risk_tests()
        assert len(risk_results) == 5
        assert all(r.test_passed for r in risk_results)

        # 4. Success criteria validation
        success_summary = await success_validator.validate_all_criteria()
        assert success_summary.overall_score >= 0.8
        assert len(success_summary.critical_issues) == 0

        # 5. Verify integration
        assert len(risk_results) > 0
        assert success_summary.total_criteria > 0

        # 6. Cleanup
        await TestCleanup.cleanup_all_connections(test_environment)

    @pytest.mark.asyncio
    async def test_testing_strategy_performance(self, test_environment):
        """Test testing strategy performance"""
        start_time = time.time()

        # Run a comprehensive test scenario
        DualConnectionTestData()
        risk_tester = RiskMitigationTester(test_environment.connection_manager)
        success_validator = SuccessCriteriaValidator(test_environment.connection_manager)

        # Run risk tests
        risk_results = await risk_tester.run_all_risk_tests()

        # Run success criteria validation
        success_summary = await success_validator.validate_all_criteria()

        total_time = time.time() - start_time

        # Verify performance
        assert total_time < 60.0  # Should complete within 60 seconds
        assert len(risk_results) == 5
        assert success_summary.total_criteria > 0

        # Cleanup
        await TestCleanup.cleanup_all_connections(test_environment)


# Test coverage validation
class TestCoverageValidation:
    """Test coverage validation for testing strategy"""

    def test_test_data_coverage(self):
        """Test that test data covers all scenarios"""
        test_data = DualConnectionTestData()

        # Verify all connection types are covered
        connection_types = set()
        for connection in test_data.connections:
            connection_types.add(connection.connection_type)

        assert "websocket" in connection_types
        assert "sse" in connection_types

        # Verify different player scenarios
        player_types = set()
        for player in test_data.players:
            if player.connection_count == 1:
                player_types.add("single")
            elif player.connection_count == 2:
                player_types.add("dual")
            elif player.connection_count >= 3:
                player_types.add("multi")
            elif not player.is_online:
                player_types.add("offline")

        assert "single" in player_types
        assert "dual" in player_types
        assert "multi" in player_types
        assert "offline" in player_types

    def test_risk_scenario_coverage(self):
        """Test that risk scenarios cover all risk types"""
        from server.tests.utils.risk_mitigation import RiskMitigationTester

        # Create a minimal connection manager for testing
        class MockConnectionManager:
            def __init__(self):
                self.connection_metadata = {}

        risk_tester = RiskMitigationTester(MockConnectionManager())

        # Verify all risk types are covered
        risk_types = set()
        for scenario in risk_tester.risk_scenarios:
            risk_types.add(scenario.risk_type)

        assert "technical" in risk_types
        assert "operational" in risk_types

        # Verify all severity levels are covered
        severity_levels = set()
        for scenario in risk_tester.risk_scenarios:
            severity_levels.add(scenario.severity)

        assert "high" in severity_levels
        assert "medium" in severity_levels
        assert "critical" in severity_levels

    def test_success_criteria_coverage(self):
        """Test that success criteria cover all categories"""
        from server.tests.utils.success_criteria_validator import SuccessCriteriaValidator

        # Create a minimal connection manager for testing
        class MockConnectionManager:
            def __init__(self):
                self.connection_metadata = {}

        success_validator = SuccessCriteriaValidator(MockConnectionManager())

        # Verify all categories are covered
        categories = set()
        for result in success_validator.validation_results:
            categories.add(result.category)

        assert "functional" in categories
        assert "performance" in categories
        assert "quality" in categories


# Export test classes
__all__ = ["TestDualConnectionTestingStrategy", "TestCoverageValidation"]
