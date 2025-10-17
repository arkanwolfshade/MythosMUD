#!/usr/bin/env python3
"""
MythosMUD Test Runner - Clean Test Framework

This module provides a modern, clean test running framework that properly
integrates with the MythosMUD logging standards and test structure.

As noted in the restricted archives of Miskatonic University, proper test
organization is essential for maintaining the integrity of our research
into the forbidden territories of the Mythos.

Author: Professor of Occult Studies, Miskatonic University
"""

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

import structlog

# Configure basic logging for the test runner itself
structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.dev.ConsoleRenderer(colors=True),
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger("test_runner")


class TestRunner:
    """
    Clean test runner for MythosMUD server tests.

    This class provides a modern, maintainable approach to running tests
    that respects the project's logging standards and test organization.
    """

    def __init__(self, project_root: Path):
        """Initialize the test runner with project root."""
        self.project_root = project_root
        self.server_dir = project_root / "server"
        self.test_dir = self.server_dir / "tests"
        self.data_dir = project_root / "data" / "unit_test"
        self.logs_dir = project_root / "logs" / "unit_test"

        # Ensure directories exist
        self.logs_dir.mkdir(parents=True, exist_ok=True)
        self.data_dir.mkdir(parents=True, exist_ok=True)

        logger.info(
            "Test runner initialized",
            project_root=str(project_root),
            server_dir=str(self.server_dir),
            test_dir=str(self.test_dir),
            data_dir=str(self.data_dir),
            logs_dir=str(self.logs_dir),
        )

    def setup_test_environment(self) -> dict[str, str]:
        """
        Set up the test environment with proper configuration.

        Returns:
            Environment variables dictionary for test execution
        """
        env = os.environ.copy()

        # Test environment configuration
        env.update(
            {
                "LOGGING_ENVIRONMENT": "unit_test",
                "MYTHOSMUD_TEST_MODE": "true",
                "DATABASE_URL": f"sqlite+aiosqlite:///{self.data_dir}/players/unit_test_players.db",
                "DATABASE_NPC_URL": f"sqlite+aiosqlite:///{self.data_dir}/npcs/unit_test_npcs.db",
                "GAME_ALIASES_DIR": str(self.data_dir / "players" / "aliases"),
                "PYTHONPATH": str(self.server_dir),
            }
        )

        logger.info(
            "Test environment configured",
            database_url=env["DATABASE_URL"],
            database_npc_url=env["DATABASE_NPC_URL"],
            logging_environment=env["LOGGING_ENVIRONMENT"],
        )

        return env

    def clean_test_databases(self, env: dict[str, str]) -> bool:
        """
        Clean test databases before running tests.

        Args:
            env: Environment variables dictionary

        Returns:
            True if cleanup was successful, False otherwise
        """
        logger.info("Cleaning test databases")

        try:
            # Clean player database
            player_db_path = self.data_dir / "players" / "unit_test_players.db"
            if player_db_path.exists():
                player_db_path.unlink()
                logger.info("Cleaned player database", path=str(player_db_path))

            # Clean NPC database
            npc_db_path = self.data_dir / "npcs" / "unit_test_npcs.db"
            if npc_db_path.exists():
                npc_db_path.unlink()
                logger.info("Cleaned NPC database", path=str(npc_db_path))

            # Ensure directories exist
            player_db_path.parent.mkdir(parents=True, exist_ok=True)
            npc_db_path.parent.mkdir(parents=True, exist_ok=True)

            return True

        except Exception as e:
            logger.error("Failed to clean test databases", error=str(e))
            return False

    def get_pytest_command(self, test_paths: list[str], extra_args: list[str]) -> list[str]:
        """
        Build the pytest command with proper configuration.

        Args:
            test_paths: List of test paths to run
            extra_args: Additional pytest arguments

        Returns:
            Complete pytest command as list of strings
        """
        # Base pytest command
        cmd = [
            "uv",
            "run",
            "pytest",
            "-v",  # Verbose output
            "--tb=short",  # Short traceback format
            "--strict-markers",  # Strict marker validation
            "--strict-config",  # Strict config validation
            "--disable-warnings",  # Disable warnings for cleaner output
            "--timeout=300",  # 5 minute timeout per test
            "--timeout-method=thread",  # Use thread-based timeout
            "--maxfail=10",  # Stop after 10 failures
            "--durations=10",  # Show 10 slowest tests
        ]

        # Add test paths
        cmd.extend(test_paths)

        # Add coverage configuration
        cmd.extend(
            [
                "--cov=.",  # Measure coverage for current directory
                "--cov-report=term-missing",  # Show terminal report with missing lines
                "--cov-report=html",  # Generate HTML coverage report
                "--cov-report=xml",  # Generate XML coverage report for CI
                "--cov-fail-under=80",  # Fail if coverage is less than 80%
            ]
        )

        # Add extra arguments
        cmd.extend(extra_args)

        logger.info("Built pytest command", command=" ".join(cmd))
        return cmd

    def run_tests(
        self, test_paths: list[str] | None = None, extra_args: list[str] | None = None, markers: str | None = None
    ) -> int:
        """
        Run the test suite with proper configuration.

        Args:
            test_paths: List of test paths to run (default: all tests)
            extra_args: Additional pytest arguments
            markers: pytest markers to filter tests

        Returns:
            Exit code from pytest (0 for success, non-zero for failure)
        """
        if test_paths is None:
            test_paths = ["tests"]

        if extra_args is None:
            extra_args = []

        # Set up environment
        env = self.setup_test_environment()

        # Clean test databases
        if not self.clean_test_databases(env):
            logger.warning("Database cleanup failed, continuing anyway")

        # Build pytest command
        cmd = self.get_pytest_command(test_paths, extra_args)

        # Add markers if specified
        if markers:
            cmd.extend(["-m", markers])

        # Add marker exclusions for E2E tests by default
        if "-m" not in cmd:
            cmd.extend(["-m", "not e2e"])

        logger.info("Starting test execution", command=" ".join(cmd), working_directory=str(self.server_dir))

        # Record start time
        start_time = time.time()

        try:
            # Run pytest
            result = subprocess.run(
                cmd,
                cwd=self.server_dir,
                env=env,
                capture_output=False,  # Let output go to console
                text=True,
            )

            # Calculate duration
            duration = time.time() - start_time

            logger.info("Test execution completed", exit_code=result.returncode, duration=f"{duration:.2f}s")

            return result.returncode

        except Exception as e:
            logger.error("Test execution failed", error=str(e))
            return 1

    def run_unit_tests(self, extra_args: list[str] | None = None) -> int:
        """Run unit tests only."""
        logger.info("Running unit tests")
        return self.run_tests(test_paths=["tests/unit"], extra_args=extra_args, markers="not e2e")

    def run_integration_tests(self, extra_args: list[str] | None = None) -> int:
        """Run integration tests only."""
        logger.info("Running integration tests")
        return self.run_tests(test_paths=["tests/integration"], extra_args=extra_args, markers="not e2e")

    def run_e2e_tests(self, extra_args: list[str] | None = None) -> int:
        """Run E2E tests only."""
        logger.info("Running E2E tests")
        return self.run_tests(test_paths=["tests/e2e"], extra_args=extra_args, markers="e2e")

    def run_all_tests(self, extra_args: list[str] | None = None) -> int:
        """Run all tests (unit, integration, but not E2E by default)."""
        logger.info("Running all tests (excluding E2E)")
        return self.run_tests(test_paths=["tests"], extra_args=extra_args, markers="not e2e")

    def run_coverage_report(self) -> int:
        """Generate coverage report only."""
        logger.info("Generating coverage report")
        return self.run_tests(
            test_paths=["tests"], extra_args=["--cov-report=html", "--cov-report=term-missing"], markers="not e2e"
        )


def main():
    """Main entry point for the test runner."""
    parser = argparse.ArgumentParser(
        description="MythosMUD Test Runner - Clean Test Framework",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                    # Run all tests (excluding E2E)
  %(prog)s --unit             # Run unit tests only
  %(prog)s --integration      # Run integration tests only
  %(prog)s --e2e              # Run E2E tests only
  %(prog)s --coverage         # Generate coverage report
  %(prog)s --path tests/unit/commands  # Run specific test path
  %(prog)s --markers "not slow"  # Run tests with specific markers
        """,
    )

    # Test type selection
    parser.add_argument("--unit", action="store_true", help="Run unit tests only")
    parser.add_argument("--integration", action="store_true", help="Run integration tests only")
    parser.add_argument("--e2e", action="store_true", help="Run E2E tests only")
    parser.add_argument("--coverage", action="store_true", help="Generate coverage report only")

    # Test path and marker selection
    parser.add_argument("--path", action="append", dest="paths", help="Specific test path(s) to run")
    parser.add_argument("--markers", "-m", help="Pytest markers to filter tests")

    # Additional pytest arguments
    parser.add_argument("--pytest-args", nargs=argparse.REMAINDER, help="Additional arguments to pass to pytest")

    # Project root override
    parser.add_argument("--project-root", type=Path, help="Override project root directory")

    args = parser.parse_args()

    # Determine project root
    if args.project_root:
        project_root = args.project_root
    else:
        # Find project root (where pyproject.toml is located)
        current_dir = Path.cwd()
        project_root = None

        for parent in [current_dir] + list(current_dir.parents):
            if (parent / "pyproject.toml").exists():
                project_root = parent
                break

        if not project_root:
            logger.error("Could not find project root (pyproject.toml)")
            sys.exit(1)

    # Initialize test runner
    runner = TestRunner(project_root)

    # Determine which tests to run
    exit_code = 0

    if args.coverage:
        exit_code = runner.run_coverage_report()
    elif args.unit:
        exit_code = runner.run_unit_tests(args.pytest_args)
    elif args.integration:
        exit_code = runner.run_integration_tests(args.pytest_args)
    elif args.e2e:
        exit_code = runner.run_e2e_tests(args.pytest_args)
    elif args.paths:
        exit_code = runner.run_tests(test_paths=args.paths, extra_args=args.pytest_args, markers=args.markers)
    else:
        # Default: run all tests (excluding E2E)
        exit_code = runner.run_all_tests(args.pytest_args)

    # Exit with the same code as pytest
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
