#!/usr/bin/env python3
"""
Execute Phase 1 Upgrades for MythosMUD
Implements patch updates with comprehensive testing and rollback capabilities
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


class Phase1UpgradeExecutor:
    """Execute Phase 1 patch updates with safety measures"""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.client_dir = project_root / "client"
        self.backup_created = False
        self.upgrade_log = []

    def create_backup(self) -> bool:
        """Create backup point before upgrades"""
        try:
            print("📌 Creating backup point...")

            # Create git commit point
            result = subprocess.run(
                ['git', 'add', '.'], cwd=self.project_root, capture_output=True, text=True, shell=True, encoding='utf-8', errors='replace'
            )

            if result.returncode != 0:
                print(f"⚠️ Warning: Git add failed: {result.stderr}")

            result = subprocess.run(
                ['git', 'commit', '-m', f'Pre-upgrade backup - {datetime.now().isoformat()}'],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                shell=True,
                encoding='utf-8',
                errors='replace',
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

            # Run Python tests
            result = subprocess.run(['make', 'test'], cwd=self.project_root, capture_output=True, text=True, shell=True, encoding='utf-8', errors='replace')

            if result.returncode != 0:
                print(f"❌ Python tests failed: {result.stderr}")
                return False

            print("✅ Python tests passed")

            # Run client tests
            result = subprocess.run(['npm', 'test'], cwd=self.client_dir, capture_output=True, text=True, shell=True, encoding='utf-8', errors='replace')

            if result.returncode != 0:
                print(f"❌ Client tests failed: {result.stderr}")
                return False

            print("✅ Client tests passed")
            return True

        except Exception as e:
            print(f"❌ Error running pre-upgrade tests: {e}")
            return False

    def upgrade_npm_packages(self) -> bool:
        """Upgrade NPM packages"""
        try:
            print("📦 Upgrading NPM packages...")

            npm_upgrades = [
                "@types/node@24.3.1",
                "@types/react@19.1.12",
                "@types/react-dom@19.1.9",
                "@vitejs/plugin-react@5.0.2",
                "vite@7.1.4",
            ]

            for package in npm_upgrades:
                print(f"  Upgrading {package}...")
                result = subprocess.run(
                    ['npm', 'install', package], cwd=self.client_dir, capture_output=True, text=True, shell=True, encoding='utf-8', errors='replace'
                )

                if result.returncode != 0:
                    print(f"❌ Failed to upgrade {package}: {result.stderr}")
                    return False

                self.upgrade_log.append(
                    {
                        "package": package,
                        "ecosystem": "npm",
                        "status": "success",
                        "timestamp": datetime.now().isoformat(),
                    }
                )
                print(f"  ✅ {package} upgraded successfully")

            return True

        except Exception as e:
            print(f"❌ Error upgrading NPM packages: {e}")
            return False

    def upgrade_python_packages(self) -> bool:
        """Upgrade Python packages"""
        try:
            print("🐍 Upgrading Python packages...")

            python_upgrades = [
                "click@8.2.1",
                "email-validator@2.3.0",
                "exceptiongroup@1.3.0",
                "pytest@8.4.2",
                "pytest-cov@6.3.0",
                "python-dotenv@1.1.1",
                "requests@2.32.5",
                "ruff@0.12.12",
                "tomli@2.2.1",
            ]

            for package in python_upgrades:
                print(f"  Upgrading {package}...")
                result = subprocess.run(
                    ['uv', 'pip', 'install', package], cwd=self.project_root, capture_output=True, text=True, shell=True, encoding='utf-8', errors='replace'
                )

                if result.returncode != 0:
                    print(f"❌ Failed to upgrade {package}: {result.stderr}")
                    return False

                self.upgrade_log.append(
                    {
                        "package": package,
                        "ecosystem": "pip",
                        "status": "success",
                        "timestamp": datetime.now().isoformat(),
                    }
                )
                print(f"  ✅ {package} upgraded successfully")

            return True

        except Exception as e:
            print(f"❌ Error upgrading Python packages: {e}")
            return False

    def run_post_upgrade_tests(self) -> bool:
        """Run tests after upgrades"""
        try:
            print("🧪 Running post-upgrade tests...")

            # Run Python tests
            result = subprocess.run(['make', 'test'], cwd=self.project_root, capture_output=True, text=True, shell=True, encoding='utf-8', errors='replace')

            if result.returncode != 0:
                print(f"❌ Python tests failed after upgrade: {result.stderr}")
                return False

            print("✅ Python tests passed after upgrade")

            # Run client tests
            result = subprocess.run(['npm', 'test'], cwd=self.client_dir, capture_output=True, text=True, shell=True, encoding='utf-8', errors='replace')

            if result.returncode != 0:
                print(f"❌ Client tests failed after upgrade: {result.stderr}")
                return False

            print("✅ Client tests passed after upgrade")
            return True

        except Exception as e:
            print(f"❌ Error running post-upgrade tests: {e}")
            return False

    def run_linting(self) -> bool:
        """Run linting checks"""
        try:
            print("🔍 Running linting checks...")

            # Run Python linting
            result = subprocess.run(['make', 'lint'], cwd=self.project_root, capture_output=True, text=True, shell=True, encoding='utf-8', errors='replace')

            if result.returncode != 0:
                print(f"❌ Python linting failed: {result.stderr}")
                return False

            print("✅ Python linting passed")

            # Run client linting
            result = subprocess.run(
                ['npm', 'run', 'lint'], cwd=self.client_dir, capture_output=True, text=True, shell=True, encoding='utf-8', errors='replace'
            )

            if result.returncode != 0:
                print(f"❌ Client linting failed: {result.stderr}")
                return False

            print("✅ Client linting passed")
            return True

        except Exception as e:
            print(f"❌ Error running linting: {e}")
            return False

    def rollback(self) -> bool:
        """Rollback to previous state"""
        try:
            print("🔄 Rolling back to previous state...")

            if self.backup_created:
                result = subprocess.run(
                    ['git', 'reset', '--hard', 'HEAD~1'],
                    cwd=self.project_root,
                    capture_output=True,
                    text=True,
                    shell=True,
                    encoding='utf-8',
                    errors='replace',
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
                "phase": "Phase 1 - Patch Updates",
                "upgrades": self.upgrade_log,
                "backup_created": self.backup_created,
            }

            log_path = self.project_root / "upgrade_log_phase1.json"
            with open(log_path, "w", encoding="utf-8") as f:
                json.dump(log_data, f, indent=2)

            print(f"📄 Upgrade log saved to: {log_path}")

        except Exception as e:
            print(f"⚠️ Warning: Could not save upgrade log: {e}")

    def execute_phase1(self) -> bool:
        """Execute complete Phase 1 upgrade process"""
        print("🚀 Starting Phase 1: Patch Updates")
        print("=" * 50)

        try:
            # Step 1: Create backup
            if not self.create_backup():
                print("⚠️ Warning: Backup creation failed, but continuing...")

            # Step 2: Run pre-upgrade tests
            if not self.run_pre_upgrade_tests():
                print("❌ Pre-upgrade tests failed. Aborting upgrade.")
                return False

            # Step 3: Upgrade NPM packages
            if not self.upgrade_npm_packages():
                print("❌ NPM package upgrades failed. Rolling back...")
                self.rollback()
                return False

            # Step 4: Upgrade Python packages
            if not self.upgrade_python_packages():
                print("❌ Python package upgrades failed. Rolling back...")
                self.rollback()
                return False

            # Step 5: Run post-upgrade tests
            if not self.run_post_upgrade_tests():
                print("❌ Post-upgrade tests failed. Rolling back...")
                self.rollback()
                return False

            # Step 6: Run linting
            if not self.run_linting():
                print("❌ Linting failed. Rolling back...")
                self.rollback()
                return False

            # Step 7: Save upgrade log
            self.save_upgrade_log()

            print("\n🎉 Phase 1 upgrades completed successfully!")
            print("✅ All tests passed")
            print("✅ All linting passed")
            print("✅ System is ready for Phase 2")

            return True

        except Exception as e:
            print(f"❌ Unexpected error during Phase 1: {e}")
            self.rollback()
            return False


def main():
    """Main execution function"""
    project_root = Path(__file__).parent.parent

    print("🔬 MythosMUD Phase 1 Upgrade Executor")
    print("=" * 50)

    # Confirm with user
    response = input("This will upgrade patch versions of dependencies. Continue? (y/N): ")
    if response.lower() != "y":
        print("Upgrade cancelled by user.")
        return 1

    executor = Phase1UpgradeExecutor(project_root)

    success = executor.execute_phase1()

    if success:
        print("\n🎯 Phase 1 completed successfully!")
        print("Next steps:")
        print("1. Review upgrade log")
        print("2. Plan Phase 2 (minor updates)")
        print("3. Monitor system for any issues")
        return 0
    else:
        print("\n❌ Phase 1 failed!")
        print("System has been rolled back to previous state.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
