import argparse
import os
import subprocess
import sys
from pathlib import Path


def run_server_tests():
    """Run server-side Python tests"""
    print("🧹 Cleaning test database...")
    clean_cmd = ["python", "scripts/clean_test_db.py"]

    # Set the required environment variables for the subprocess
    env = os.environ.copy()
    env["DATABASE_URL"] = "sqlite+aiosqlite:///server/tests/data/players/test_players.db"
    # Get the project root (one level up from scripts directory)
    project_root = Path(__file__).parent.parent
    # Ensure we're using the correct path for test logs
    test_logs_dir = project_root / "server" / "tests" / "logs"
    test_logs_dir.mkdir(parents=True, exist_ok=True)
    # Legacy logging environment variables no longer needed -
    # logging is handled by centralized system
    env["ALIASES_DIR"] = "server/tests/data/players/aliases"

    clean_result = subprocess.run(clean_cmd, env=env)

    if clean_result.returncode != 0:
        print("⚠️  Warning: Failed to clean test database, continuing anyway...")

    print("🐍 Running server tests with pytest...")
    # Change to server directory to use the pytest configuration there
    server_dir = project_root / "server"
    cmd = ["uv", "run", "pytest", "tests", "-v", "--tb=short"]
    result = subprocess.run(cmd, env=env, cwd=server_dir)

    return result.returncode


def run_client_tests():
    """Run client-side tests (Vitest unit tests and Playwright E2E tests)"""
    print("⚛️  Running client tests...")

    # Get the project root
    project_root = Path(__file__).parent.parent
    client_dir = project_root / "client"

    # Run Vitest unit tests using shell
    print("  📊 Running Vitest unit tests...")
    vitest_cmd = "npm run test:unit:run"
    vitest_result = subprocess.run(vitest_cmd, shell=True, cwd=client_dir)

    if vitest_result.returncode != 0:
        print("  ❌ Vitest unit tests failed")
        return vitest_result.returncode

    # Run Playwright E2E tests using shell
    print("  🌐 Running Playwright E2E tests...")
    playwright_cmd = "npm run test"
    playwright_result = subprocess.run(playwright_cmd, shell=True, cwd=client_dir)

    if playwright_result.returncode != 0:
        print("  ❌ Playwright E2E tests failed")
        return playwright_result.returncode

    print("  ✅ Client tests passed!")
    return 0


def main():
    """Run all tests (server and client)"""
    parser = argparse.ArgumentParser(description="Run MythosMUD tests")
    parser.add_argument("--server-only", action="store_true", help="Run only server tests")
    parser.add_argument("--client-only", action="store_true", help="Run only client tests")

    args = parser.parse_args()

    if args.server_only:
        print("🧪 Running Server Tests Only")
        print("=" * 30)
        server_result = run_server_tests()
        if server_result != 0:
            print(f"❌ Server tests failed with exit code: {server_result}")
            sys.exit(server_result)
        else:
            print("✅ Server tests passed!")
        return

    if args.client_only:
        print("🧪 Running Client Tests Only")
        print("=" * 30)
        client_result = run_client_tests()
        if client_result != 0:
            print(f"❌ Client tests failed with exit code: {client_result}")
            sys.exit(client_result)
        else:
            print("✅ Client tests passed!")
        return

    # Run all tests
    print("🧪 Running MythosMUD Test Suite")
    print("=" * 50)

    # Run server tests
    server_result = run_server_tests()
    if server_result != 0:
        print(f"❌ Server tests failed with exit code: {server_result}")
        sys.exit(server_result)
    else:
        print("✅ Server tests passed!")

    print()

    # Run client tests
    client_result = run_client_tests()
    if client_result != 0:
        print(f"❌ Client tests failed with exit code: {client_result}")
        sys.exit(client_result)
    else:
        print("✅ Client tests passed!")

    print()
    print("🎉 All tests passed! MythosMUD is ready for deployment.")


if __name__ == "__main__":
    main()
