import os
import subprocess
import sys
from pathlib import Path


def run_server_coverage():
    """Run server-side coverage with pytest"""
    print("🐍 Running server coverage with pytest...")
    cmd = ["uv", "run", "pytest", "--cov=.", "--cov-report=term-missing", "tests"]
    env = dict(**os.environ)

    # Set up environment for server tests
    env["DATABASE_URL"] = "sqlite+aiosqlite:///server/tests/data/players/test_players.db"
    env["ALIASES_DIR"] = "server/tests/data/players/aliases"

    result = subprocess.run(cmd, env=env, cwd="server")
    return result.returncode


def run_client_coverage():
    """Run client-side coverage with Vitest"""
    print("⚛️  Running client coverage with Vitest...")

    # Get the project root
    project_root = Path(__file__).parent.parent
    client_dir = project_root / "client"

    # Run client coverage tests using shell
    cmd = "npm run test:coverage"
    result = subprocess.run(cmd, shell=True, cwd=client_dir)
    return result.returncode


def main():
    """Run coverage for both server and client"""
    print("📊 Running MythosMUD Coverage Suite")
    print("=" * 50)

    # Run server coverage
    server_result = run_server_coverage()
    if server_result != 0:
        print(f"❌ Server coverage failed with exit code: {server_result}")
        sys.exit(server_result)
    else:
        print("✅ Server coverage completed!")

    print()

    # Run client coverage
    client_result = run_client_coverage()
    if client_result != 0:
        print(f"❌ Client coverage failed with exit code: {client_result}")
        sys.exit(client_result)
    else:
        print("✅ Client coverage completed!")

    print()
    print("🎉 All coverage reports generated successfully!")
    print("📈 Server coverage: Check terminal output above")
    print("📊 Client coverage: Check client/coverage/index.html")


if __name__ == "__main__":
    main()
