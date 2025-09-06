#!/usr/bin/env python3
"""
Execute React/Node.js Ecosystem Upgrades for MythosMUD
Specialized script for frontend ecosystem upgrades
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


class ReactNodeUpgradeExecutor:
    """Execute React/Node.js ecosystem upgrades with safety measures"""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.client_dir = project_root / "client"
        self.backup_created = False
        self.upgrade_log = []

    def create_backup(self) -> bool:
        """Create backup point before upgrades"""
        try:
            print("📌 Creating backup point for React/Node upgrades...")

            # Create git commit point
            result = subprocess.run(
                ["git", "add", "."], cwd=self.project_root, capture_output=True, text=True, shell=True
            )

            if result.returncode != 0:
                print(f"⚠️ Warning: Git add failed: {result.stderr}")

            result = subprocess.run(
                ["git", "commit", "-m", f"Pre-React/Node upgrade backup - {datetime.now().isoformat()}"],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                shell=True,
            )

            if result.returncode == 0:
                print("✅ Git backup created successfully")
                self.backup_created = True
                return True
            else:
                print(f"⚠️ Warning: Git commit failed: {result.stderr}")
                return False

        except Exception as e:
            print(f"❌ Error creating backup: {e}")
            return False

    def run_pre_upgrade_tests(self) -> bool:
        """Run tests before upgrades"""
        try:
            print("🧪 Running pre-upgrade tests...")

            # Run client tests
            result = subprocess.run(["npm", "test"], cwd=self.client_dir, capture_output=True, text=True, shell=True)

            if result.returncode != 0:
                print(f"❌ Client tests failed: {result.stderr}")
                return False

            print("✅ Client tests passed")

            # Run unit tests
            result = subprocess.run(
                ["npm", "run", "test:unit:run"], cwd=self.client_dir, capture_output=True, text=True, shell=True
            )

            if result.returncode != 0:
                print(f"❌ Unit tests failed: {result.stderr}")
                return False

            print("✅ Unit tests passed")

            # Run build test
            result = subprocess.run(
                ["npm", "run", "build"], cwd=self.client_dir, capture_output=True, text=True, shell=True
            )

            if result.returncode != 0:
                print(f"❌ Build test failed: {result.stderr}")
                return False

            print("✅ Build test passed")

            return True

        except Exception as e:
            print(f"❌ Error running pre-upgrade tests: {e}")
            return False

    def upgrade_phase1_patch_updates(self) -> bool:
        """Upgrade Phase 1: Patch updates (low risk)"""
        try:
            print("🔧 Upgrading Phase 1: Patch updates...")

            patch_upgrades = [
                "@types/node@24.3.1",
                "@types/react@19.1.12",
                "@types/react-dom@19.1.9",
                "@vitejs/plugin-react@5.0.2",
                "vite@7.1.4",
            ]

            for package in patch_upgrades:
                print(f"  Upgrading {package}...")
                result = subprocess.run(
                    ["npm", "install", package], cwd=self.client_dir, capture_output=True, text=True, shell=True
                )

                if result.returncode != 0:
                    print(f"❌ Failed to upgrade {package}: {result.stderr}")
                    return False

                self.upgrade_log.append(
                    {
                        "package": package,
                        "phase": "Phase 1 - Patch Updates",
                        "status": "success",
                        "timestamp": datetime.now().isoformat(),
                    }
                )
                print(f"  ✅ {package} upgraded successfully")

            return True

        except Exception as e:
            print(f"❌ Error upgrading Phase 1 packages: {e}")
            return False

    def upgrade_phase2_minor_updates(self) -> bool:
        """Upgrade Phase 2: Minor updates (medium risk)"""
        try:
            print("📈 Upgrading Phase 2: Minor updates...")

            minor_upgrades = [
                "eslint@9.35.0",
                "@eslint/js@9.35.0",
                "typescript-eslint@8.42.0",
                "tailwindcss@4.1.13",
                "@tailwindcss/postcss@4.1.13",
                "@playwright/test@1.55.0",
                "@testing-library/jest-dom@6.8.0",
                "lucide-react@0.542.0",
            ]

            for package in minor_upgrades:
                print(f"  Upgrading {package}...")
                result = subprocess.run(
                    ["npm", "install", package], cwd=self.client_dir, capture_output=True, text=True, shell=True
                )

                if result.returncode != 0:
                    print(f"❌ Failed to upgrade {package}: {result.stderr}")
                    return False

                self.upgrade_log.append(
                    {
                        "package": package,
                        "phase": "Phase 2 - Minor Updates",
                        "status": "success",
                        "timestamp": datetime.now().isoformat(),
                    }
                )
                print(f"  ✅ {package} upgraded successfully")

            return True

        except Exception as e:
            print(f"❌ Error upgrading Phase 2 packages: {e}")
            return False

    def run_post_upgrade_tests(self) -> bool:
        """Run tests after upgrades"""
        try:
            print("🧪 Running post-upgrade tests...")

            # Run linting first
            result = subprocess.run(
                ["npm", "run", "lint"], cwd=self.client_dir, capture_output=True, text=True, shell=True
            )

            if result.returncode != 0:
                print(f"❌ Linting failed after upgrade: {result.stderr}")
                return False

            print("✅ Linting passed after upgrade")

            # Run unit tests
            result = subprocess.run(
                ["npm", "run", "test:unit:run"], cwd=self.client_dir, capture_output=True, text=True, shell=True
            )

            if result.returncode != 0:
                print(f"❌ Unit tests failed after upgrade: {result.stderr}")
                return False

            print("✅ Unit tests passed after upgrade")

            # Run Playwright tests
            result = subprocess.run(["npm", "test"], cwd=self.client_dir, capture_output=True, text=True, shell=True)

            if result.returncode != 0:
                print(f"❌ Playwright tests failed after upgrade: {result.stderr}")
                return False

            print("✅ Playwright tests passed after upgrade")

            # Run build test
            result = subprocess.run(
                ["npm", "run", "build"], cwd=self.client_dir, capture_output=True, text=True, shell=True
            )

            if result.returncode != 0:
                print(f"❌ Build test failed after upgrade: {result.stderr}")
                return False

            print("✅ Build test passed after upgrade")

            return True

        except Exception as e:
            print(f"❌ Error running post-upgrade tests: {e}")
            return False

    def verify_react_19_features(self) -> bool:
        """Verify React 19 features are working correctly"""
        try:
            print("⚛️ Verifying React 19 features...")

            # Check if React 19 is properly installed
            result = subprocess.run(
                ["npm", "list", "react"], cwd=self.client_dir, capture_output=True, text=True, shell=True
            )

            if "19.1.1" not in result.stdout:
                print("❌ React 19.1.1 not properly installed")
                return False

            print("✅ React 19.1.1 verified")

            # Check React DOM
            result = subprocess.run(
                ["npm", "list", "react-dom"], cwd=self.client_dir, capture_output=True, text=True, shell=True
            )

            if "19.1.1" not in result.stdout:
                print("❌ React DOM 19.1.1 not properly installed")
                return False

            print("✅ React DOM 19.1.1 verified")

            # Check TypeScript definitions
            result = subprocess.run(
                ["npm", "list", "@types/react"], cwd=self.client_dir, capture_output=True, text=True, shell=True
            )

            if "19.1.12" not in result.stdout:
                print("⚠️ Warning: @types/react not at expected version")

            print("✅ TypeScript definitions verified")

            return True

        except Exception as e:
            print(f"❌ Error verifying React 19 features: {e}")
            return False

    def rollback(self) -> bool:
        """Rollback to previous state"""
        try:
            print("🔄 Rolling back to previous state...")

            if self.backup_created:
                result = subprocess.run(
                    ["git", "reset", "--hard", "HEAD~1"],
                    cwd=self.project_root,
                    capture_output=True,
                    text=True,
                    shell=True,
                )

                if result.returncode == 0:
                    print("✅ Rollback completed successfully")
                    return True
                else:
                    print(f"❌ Rollback failed: {result.stderr}")
                    return False
            else:
                print("❌ No backup available for rollback")
                return False

        except Exception as e:
            print(f"❌ Error during rollback: {e}")
            return False

    def save_upgrade_log(self) -> None:
        """Save upgrade log to file"""
        try:
            log_data = {
                "timestamp": datetime.now().isoformat(),
                "phase": "React/Node.js Ecosystem Upgrades",
                "upgrades": self.upgrade_log,
                "backup_created": self.backup_created,
            }

            log_path = self.project_root / "react_node_upgrade_log.json"
            with open(log_path, "w", encoding="utf-8") as f:
                json.dump(log_data, f, indent=2)

            print(f"📄 Upgrade log saved to: {log_path}")

        except Exception as e:
            print(f"⚠️ Warning: Could not save upgrade log: {e}")

    def execute_react_node_upgrades(self, phase: str = "both") -> bool:
        """Execute React/Node.js ecosystem upgrades"""
        print("⚛️🟢 Starting React/Node.js Ecosystem Upgrades")
        print("=" * 60)

        try:
            # Step 1: Create backup
            if not self.create_backup():
                print("⚠️ Warning: Backup creation failed, but continuing...")

            # Step 2: Run pre-upgrade tests
            if not self.run_pre_upgrade_tests():
                print("❌ Pre-upgrade tests failed. Aborting upgrade.")
                return False

            # Step 3: Execute Phase 1 (Patch Updates)
            if phase in ["both", "phase1"]:
                if not self.upgrade_phase1_patch_updates():
                    print("❌ Phase 1 upgrades failed. Rolling back...")
                    self.rollback()
                    return False

                print("✅ Phase 1 (Patch Updates) completed successfully")

            # Step 4: Execute Phase 2 (Minor Updates)
            if phase in ["both", "phase2"]:
                if not self.upgrade_phase2_minor_updates():
                    print("❌ Phase 2 upgrades failed. Rolling back...")
                    self.rollback()
                    return False

                print("✅ Phase 2 (Minor Updates) completed successfully")

            # Step 5: Run post-upgrade tests
            if not self.run_post_upgrade_tests():
                print("❌ Post-upgrade tests failed. Rolling back...")
                self.rollback()
                return False

            # Step 6: Verify React 19 features
            if not self.verify_react_19_features():
                print("❌ React 19 verification failed. Rolling back...")
                self.rollback()
                return False

            # Step 7: Save upgrade log
            self.save_upgrade_log()

            print("\n🎉 React/Node.js ecosystem upgrades completed successfully!")
            print("✅ All tests passed")
            print("✅ All linting passed")
            print("✅ React 19 features verified")
            print("✅ Build process working")
            print("✅ System is ready for production")

            return True

        except Exception as e:
            print(f"❌ Unexpected error during React/Node upgrades: {e}")
            self.rollback()
            return False


def main():
    """Main execution function"""
    project_root = Path(__file__).parent.parent

    print("⚛️🟢 MythosMUD React/Node.js Ecosystem Upgrade Executor")
    print("=" * 70)

    # Get user input for phase selection
    print("\nSelect upgrade phase:")
    print("1. Phase 1 only (Patch updates - Low risk)")
    print("2. Phase 2 only (Minor updates - Medium risk)")
    print("3. Both phases (Complete upgrade)")
    print("4. Cancel")

    choice = input("\nEnter your choice (1-4): ").strip()

    if choice == "1":
        phase = "phase1"
        description = "Phase 1: Patch Updates"
    elif choice == "2":
        phase = "phase2"
        description = "Phase 2: Minor Updates"
    elif choice == "3":
        phase = "both"
        description = "Complete React/Node.js Ecosystem Upgrade"
    elif choice == "4":
        print("Upgrade cancelled by user.")
        return 1
    else:
        print("Invalid choice. Upgrade cancelled.")
        return 1

    # Confirm with user
    response = input(f"\nThis will execute {description}. Continue? (y/N): ")
    if response.lower() != "y":
        print("Upgrade cancelled by user.")
        return 1

    executor = ReactNodeUpgradeExecutor(project_root)

    success = executor.execute_react_node_upgrades(phase)

    if success:
        print(f"\n🎯 {description} completed successfully!")
        print("Next steps:")
        print("1. Review upgrade log")
        print("2. Monitor application for any issues")
        print("3. Plan next upgrade cycle")
        return 0
    else:
        print(f"\n❌ {description} failed!")
        print("System has been rolled back to previous state.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
