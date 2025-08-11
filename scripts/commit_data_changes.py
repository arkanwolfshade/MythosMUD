#!/usr/bin/env python3
"""
Data Change Commit Script
Automates the two-step commit process for data changes in the submodule
"""

import os
import subprocess
import sys


def run_command(cmd, cwd=None, capture_output=True):
    """Run a command and return the result"""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=capture_output, text=True)
        if result.returncode != 0:
            print(f"❌ Command failed: {cmd}")
            if capture_output and result.stderr:
                print(f"Error: {result.stderr}")
            return False
        return True
    except Exception as e:
        print(f"❌ Error running command '{cmd}': {e}")
        return False


def check_git_status(cwd):
    """Check if there are changes to commit"""
    result = subprocess.run("git status --porcelain", shell=True, cwd=cwd, capture_output=True, text=True)
    return result.stdout.strip() != ""


def commit_data_changes(commit_message=None):
    """Commit data changes in both repositories"""
    print("=== COMMITTING DATA CHANGES ===\n")

    # Check if we're in the right directory
    if not os.path.exists("data/.git"):
        print("❌ Data submodule not found. Are you in the project root?")
        return False

    # Check if there are changes in the data directory
    if not check_git_status("data"):
        print("✅ No changes detected in data directory")
        return True

    # Get commit message
    if not commit_message:
        commit_message = input("Enter commit message for data changes: ").strip()
        if not commit_message:
            print("❌ Commit message is required")
            return False

    print(f"📝 Commit message: {commit_message}")

    # Step 1: Commit and push data changes
    print("\n=== STEP 1: COMMITTING DATA CHANGES ===")

    if not run_command("git add .", cwd="data"):
        print("❌ Failed to stage data changes")
        return False

    if not run_command(f'git commit -m "{commit_message}"', cwd="data"):
        print("❌ Failed to commit data changes")
        return False

    if not run_command("git push origin main", cwd="data"):
        print("❌ Failed to push data changes")
        return False

    print("✅ Data changes committed and pushed")

    # Step 2: Update submodule reference in main repo
    print("\n=== STEP 2: UPDATING SUBMODULE REFERENCE ===")

    if not run_command("git add data", cwd="."):
        print("❌ Failed to stage submodule update")
        return False

    submodule_message = f"Update data submodule: {commit_message}"
    if not run_command(f'git commit -m "{submodule_message}"', cwd="."):
        print("❌ Failed to commit submodule update")
        return False

    if not run_command("git push origin main", cwd="."):
        print("❌ Failed to push submodule update")
        return False

    print("✅ Submodule reference updated and pushed")

    print("\n=== COMMIT COMPLETE ===")
    print("✅ Data changes successfully committed to both repositories!")
    return True


def show_status():
    """Show the status of both repositories"""
    print("=== REPOSITORY STATUS ===\n")

    # Main repository status
    print("📁 Main Repository:")
    run_command("git status", capture_output=False)

    print("\n📁 Data Submodule:")
    if os.path.exists("data/.git"):
        run_command("git status", cwd="data", capture_output=False)
    else:
        print("❌ Data submodule not found")


def main():
    """Main function"""
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "commit":
            commit_message = sys.argv[2] if len(sys.argv) > 2 else None
            success = commit_data_changes(commit_message)
            sys.exit(0 if success else 1)

        elif command == "status":
            show_status()
            return

        else:
            print(f"❌ Unknown command: {command}")
            print("Available commands: commit, status")
            sys.exit(1)

    # Interactive mode
    print("=== MYTHOSMUD DATA COMMIT TOOL ===\n")
    print("1. Commit data changes")
    print("2. Show repository status")
    print("3. Exit")

    choice = input("\nSelect option (1-3): ").strip()

    if choice == "1":
        commit_message = input("Enter commit message (or press Enter for interactive): ").strip()
        if not commit_message:
            commit_message = None
        success = commit_data_changes(commit_message)
        sys.exit(0 if success else 1)

    elif choice == "2":
        show_status()

    elif choice == "3":
        print("Goodbye!")

    else:
        print("❌ Invalid choice")


if __name__ == "__main__":
    main()
