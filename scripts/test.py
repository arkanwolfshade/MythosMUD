import argparse
import os
import subprocess
import sys
from pathlib import Path


def run_server_tests():
    """Run server-side Python tests (excluding E2E tests)"""
    print("Cleaning test database...")
    clean_cmd = ["python", "scripts/clean_test_db.py"]

    # Set the required environment variables for the subprocess
    env = os.environ.copy()
    env["DATABASE_URL"] = "sqlite+aiosqlite:///data/unit_test/players/test_players.db"
    # Get the project root (one level up from scripts directory)
    project_root = Path(__file__).parent.parent
    # Ensure we're using the correct path for test logs
    test_logs_dir = project_root / "logs" / "unit_test"
    test_logs_dir.mkdir(parents=True, exist_ok=True)
    # Set test environment variables for logging
    env["MYTHOSMUD_ENV"] = "unit_test"
    env["MYTHOSMUD_TEST_MODE"] = "true"
    env["MYTHOSMUD_CONFIG_PATH"] = str(project_root / "server" / "server_config.unit_test.yaml")
    env["ALIASES_DIR"] = "data/unit_test/players/aliases"

    clean_result = subprocess.run(clean_cmd, env=env)

    if clean_result.returncode != 0:
        print("Warning: Failed to clean test database, continuing anyway...")

    print("Running server tests with pytest (excluding E2E tests)...")
    # Change to server directory to use the pytest configuration there
    server_dir = project_root / "server"
    # Exclude E2E tests from standard test runs
    cmd = [
        "uv",
        "run",
        "pytest",
        "tests",
        "-v",
        "--tb=short",
        "--ignore=tests/test_e2e_multiplayer_connection_messaging.py",
        "-m",
        "not e2e",  # Exclude tests marked with @pytest.mark.e2e
    ]
    result = subprocess.run(cmd, env=env, cwd=server_dir)

    return result.returncode


def run_server_e2e_tests():
    """Run server-side E2E tests (requires running server)"""
    print("Running server E2E tests...")
    print("WARNING: This requires the server to be running!")
    print("   Make sure to run './scripts/start_local.ps1' first.")
    print()

    # Set the required environment variables for the subprocess
    env = os.environ.copy()
    env["DATABASE_URL"] = "sqlite+aiosqlite:///data/unit_test/players/test_players.db"
    # Get the project root (one level up from scripts directory)
    project_root = Path(__file__).parent.parent
    # Ensure we're using the correct path for test logs
    test_logs_dir = project_root / "logs" / "unit_test"
    test_logs_dir.mkdir(parents=True, exist_ok=True)
    # Set test environment variables for logging
    env["MYTHOSMUD_ENV"] = "unit_test"
    env["MYTHOSMUD_TEST_MODE"] = "true"
    env["MYTHOSMUD_CONFIG_PATH"] = str(project_root / "server" / "server_config.unit_test.yaml")
    env["ALIASES_DIR"] = "data/unit_test/players/aliases"

    print("Running server E2E tests with pytest...")
    # Change to server directory to use the pytest configuration there
    server_dir = project_root / "server"
    # Run only E2E tests (only the existing e2e file and tests marked with @pytest.mark.e2e)
    cmd = [
        "uv",
        "run",
        "pytest",
        "tests/test_e2e_multiplayer_connection_messaging.py",
        "-v",
        "--tb=short",
        "-m",
        "e2e",  # Include only tests marked with @pytest.mark.e2e
    ]
    result = subprocess.run(cmd, env=env, cwd=server_dir)

    return result.returncode


def run_client_tests():
    """Run client-side tests (Vitest unit tests only - E2E tests disabled)"""
    print("Running client tests...")

    # Get the project root
    project_root = Path(__file__).parent.parent
    client_dir = project_root / "client"

    # Run Vitest unit tests using shell
    print("  Running Vitest unit tests...")
    vitest_cmd = "npm run test:unit:run"
    vitest_result = subprocess.run(vitest_cmd, shell=True, cwd=client_dir)

    if vitest_result.returncode != 0:
        print("  Vitest unit tests failed")
        return vitest_result.returncode

    # E2E tests are disabled - skipping Playwright tests
    print("  Skipping Playwright E2E tests (disabled)")

    print("  Client tests passed!")
    return 0


def run_client_e2e_tests():
    """Run client-side E2E runtime tests (Automated Playwright tests)"""
    print("Running client E2E runtime tests (automated)...")
    print("WARNING: This requires both server and client to be running!")
    print("   Make sure to run './scripts/start_local.ps1' first.")
    print()

    # Get the project root
    project_root = Path(__file__).parent.parent
    client_dir = project_root / "client"

    # Run Playwright runtime E2E tests (automated tests, not MCP scenarios)
    print("  Running Playwright runtime E2E tests...")
    playwright_cmd = "npm run test:e2e:runtime"
    playwright_result = subprocess.run(playwright_cmd, shell=True, cwd=client_dir)

    if playwright_result.returncode != 0:
        print("  Playwright runtime E2E tests failed")
        return playwright_result.returncode

    print("  Client E2E runtime tests passed!")
    return 0


def main():
    """Run all tests (server and client)"""
    parser = argparse.ArgumentParser(description="Run MythosMUD tests")
    parser.add_argument("--server-only", action="store_true", help="Run only server tests")
    parser.add_argument(
        "--server-e2e-only", action="store_true", help="Run only server E2E tests (requires running server)"
    )
    parser.add_argument("--client-only", action="store_true", help="Run only client unit tests (Vitest)")
    parser.add_argument("--client-e2e-only", action="store_true", help="Run only client E2E tests (Playwright)")
    parser.add_argument("--e2e-only", action="store_true", help="Run only E2E tests (if enabled)")

    args = parser.parse_args()

    if args.server_only:
        print("Running Server Tests Only")
        print("=" * 30)
        server_result = run_server_tests()
        if server_result != 0:
            print(f"Server tests failed with exit code: {server_result}")
            sys.exit(server_result)
        else:
            print("Server tests passed!")
        return

    if args.server_e2e_only:
        print("Running Server E2E Tests Only")
        print("=" * 30)
        server_e2e_result = run_server_e2e_tests()
        if server_e2e_result != 0:
            print(f"Server E2E tests failed with exit code: {server_e2e_result}")
            sys.exit(server_e2e_result)
        else:
            print("Server E2E tests passed!")
        return

    if args.client_only:
        print("Running Client Unit Tests Only")
        print("=" * 30)
        client_result = run_client_tests()
        if client_result != 0:
            print(f"Client tests failed with exit code: {client_result}")
            sys.exit(client_result)
        else:
            print("Client tests passed!")
        return

    if args.client_e2e_only:
        print("Running Client E2E Tests Only")
        print("=" * 30)
        client_e2e_result = run_client_e2e_tests()
        if client_e2e_result != 0:
            print(f"Client E2E tests failed with exit code: {client_e2e_result}")
            sys.exit(client_e2e_result)
        else:
            print("Client E2E tests passed!")
        return

    if args.e2e_only:
        print("E2E Tests are currently disabled")
        print("=" * 30)
        print("To enable E2E tests, modify scripts/test.py to include Playwright test execution")
        print("or run them manually with: cd client && npm run test")
        return

    # Run all tests
    print("Running MythosMUD Test Suite")
    print("=" * 50)

    # Run server tests
    server_result = run_server_tests()
    if server_result != 0:
        print(f"Server tests failed with exit code: {server_result}")
        sys.exit(server_result)
    else:
        print("Server tests passed!")

    print()

    # Run client tests
    client_result = run_client_tests()
    if client_result != 0:
        print(f"Client tests failed with exit code: {client_result}")
        sys.exit(client_result)
    else:
        print("Client tests passed!")

    print()
    print("All tests passed! MythosMUD is ready for deployment.")


if __name__ == "__main__":
    main()
