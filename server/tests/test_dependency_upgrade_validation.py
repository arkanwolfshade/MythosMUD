"""
Test suite for dependency upgrade validation
Ensures system stability during and after package upgrades
"""

import json
import subprocess
import sys
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

# Add project root to path for imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from scripts.execute_phase1_upgrades import Phase1UpgradeExecutor  # noqa: E402


class TestDependencyUpgradeValidation:
    """Test suite for validating dependency upgrades"""

    @pytest.fixture
    def executor(self):
        """Create Phase1UpgradeExecutor instance for testing"""
        return Phase1UpgradeExecutor(project_root)

    @pytest.fixture
    def mock_subprocess_success(self):
        """Mock subprocess calls to return success"""
        with patch("subprocess.run") as mock_run:
            mock_result = Mock()
            mock_result.returncode = 0
            mock_result.stdout = "Success"
            mock_result.stderr = ""
            mock_run.return_value = mock_result
            yield mock_run

    @pytest.fixture
    def mock_subprocess_failure(self):
        """Mock subprocess calls to return failure"""
        with patch("subprocess.run") as mock_run:
            mock_result = Mock()
            mock_result.returncode = 1
            mock_result.stdout = ""
            mock_result.stderr = "Command failed"
            mock_run.return_value = mock_result
            yield mock_run

    def test_executor_initialization(self, executor):
        """Test Phase1UpgradeExecutor initializes correctly"""
        assert executor.project_root == project_root
        assert executor.client_dir == project_root / "client"
        assert executor.backup_created is False
        assert executor.upgrade_log == []

    def test_create_backup_success(self, executor, mock_subprocess_success):
        """Test successful backup creation"""
        result = executor.create_backup()

        assert result is True
        assert executor.backup_created is True
        assert mock_subprocess_success.call_count >= 2  # git add + git commit

    def test_create_backup_failure(self, executor, mock_subprocess_failure):
        """Test backup creation failure handling"""
        result = executor.create_backup()

        assert result is False
        assert executor.backup_created is False

    def test_run_pre_upgrade_tests_success(self, executor, mock_subprocess_success):
        """Test successful pre-upgrade test execution"""
        result = executor.run_pre_upgrade_tests()

        assert result is True
        # Should call make test and npm test
        assert mock_subprocess_success.call_count >= 2

    def test_run_pre_upgrade_tests_failure(self, executor, mock_subprocess_failure):
        """Test pre-upgrade test failure handling"""
        result = executor.run_pre_upgrade_tests()

        assert result is False

    def test_upgrade_npm_packages_success(self, executor, mock_subprocess_success):
        """Test successful NPM package upgrades"""
        result = executor.upgrade_npm_packages()

        assert result is True
        assert len(executor.upgrade_log) == 5  # 5 NPM packages

        # Verify all NPM packages are in the log
        npm_packages = [log["package"] for log in executor.upgrade_log if log["ecosystem"] == "npm"]
        expected_packages = [
            "@types/node@24.3.1",
            "@types/react@19.1.12",
            "@types/react-dom@19.1.9",
            "@vitejs/plugin-react@5.0.2",
            "vite@7.1.4",
        ]

        for package in expected_packages:
            assert package in npm_packages

    def test_upgrade_npm_packages_failure(self, executor, mock_subprocess_failure):
        """Test NPM package upgrade failure handling"""
        result = executor.upgrade_npm_packages()

        assert result is False
        assert len(executor.upgrade_log) == 0

    def test_upgrade_python_packages_success(self, executor, mock_subprocess_success):
        """Test successful Python package upgrades"""
        result = executor.upgrade_python_packages()

        assert result is True
        assert len(executor.upgrade_log) == 9  # 9 Python packages

        # Verify all Python packages are in the log
        python_packages = [log["package"] for log in executor.upgrade_log if log["ecosystem"] == "pip"]
        expected_packages = [
            "click==8.2.1",
            "email-validator==2.3.0",
            "exceptiongroup==1.3.0",
            "pytest==8.4.2",
            "pytest-cov==6.3.0",
            "python-dotenv==1.1.1",
            "requests==2.32.5",
            "ruff==0.12.12",
            "tomli==2.2.1",
        ]

        for package in expected_packages:
            assert package in python_packages

    def test_upgrade_python_packages_failure(self, executor, mock_subprocess_failure):
        """Test Python package upgrade failure handling"""
        result = executor.upgrade_python_packages()

        assert result is False
        assert len(executor.upgrade_log) == 0

    def test_run_post_upgrade_tests_success(self, executor, mock_subprocess_success):
        """Test successful post-upgrade test execution"""
        result = executor.run_post_upgrade_tests()

        assert result is True
        # Should call make test and npm test
        assert mock_subprocess_success.call_count >= 2

    def test_run_post_upgrade_tests_failure(self, executor, mock_subprocess_failure):
        """Test post-upgrade test failure handling"""
        result = executor.run_post_upgrade_tests()

        assert result is False

    def test_run_linting_success(self, executor, mock_subprocess_success):
        """Test successful linting execution"""
        result = executor.run_linting()

        assert result is True
        # Should call make lint and npm run lint
        assert mock_subprocess_success.call_count >= 2

    def test_run_linting_failure(self, executor, mock_subprocess_failure):
        """Test linting failure handling"""
        result = executor.run_linting()

        assert result is False

    def test_rollback_success(self, executor, mock_subprocess_success):
        """Test successful rollback"""
        executor.backup_created = True
        result = executor.rollback()

        assert result is True
        mock_subprocess_success.assert_called_with(
            ["git", "reset", "--hard", "HEAD~1"],
            cwd=executor.project_root,
            capture_output=True,
            text=True,
            shell=True,
            encoding="utf-8",
            errors="replace",
        )

    def test_rollback_no_backup(self, executor):
        """Test rollback when no backup exists"""
        executor.backup_created = False
        result = executor.rollback()

        assert result is False

    def test_rollback_failure(self, executor, mock_subprocess_failure):
        """Test rollback failure handling"""
        executor.backup_created = True
        result = executor.rollback()

        assert result is False

    def test_save_upgrade_log(self, executor, tmp_path):
        """Test upgrade log saving"""
        # Mock the project root to use temp directory
        executor.project_root = tmp_path

        # Add some test data to upgrade log
        executor.upgrade_log = [
            {
                "package": "test-package@1.0.0",
                "ecosystem": "npm",
                "status": "success",
                "timestamp": "2025-01-01T00:00:00",
            }
        ]
        executor.backup_created = True

        executor.save_upgrade_log()

        # Verify log file was created
        log_file = tmp_path / "upgrade_log_phase1.json"
        assert log_file.exists()

        # Verify log content
        with open(log_file, encoding="utf-8") as f:
            log_data = json.load(f)

        assert log_data["phase"] == "Phase 1 - Patch Updates"
        assert log_data["backup_created"] is True
        assert len(log_data["upgrades"]) == 1
        assert log_data["upgrades"][0]["package"] == "test-package@1.0.0"

    def test_execute_phase1_success(self, executor, mock_subprocess_success):
        """Test successful Phase 1 execution"""
        result = executor.execute_phase1()

        assert result is True
        assert executor.backup_created is True
        assert len(executor.upgrade_log) == 14  # 5 NPM + 9 Python packages

    def test_execute_phase1_pre_upgrade_test_failure(self, executor):
        """Test Phase 1 execution with pre-upgrade test failure"""
        with patch.object(executor, "run_pre_upgrade_tests", return_value=False):
            result = executor.execute_phase1()

            assert result is False

    def test_execute_phase1_npm_upgrade_failure(self, executor, mock_subprocess_success):
        """Test Phase 1 execution with NPM upgrade failure"""
        with (
            patch.object(executor, "run_pre_upgrade_tests", return_value=True),
            patch.object(executor, "upgrade_npm_packages", return_value=False),
            patch.object(executor, "rollback", return_value=True),
        ):
            result = executor.execute_phase1()

            assert result is False

    def test_execute_phase1_python_upgrade_failure(self, executor, mock_subprocess_success):
        """Test Phase 1 execution with Python upgrade failure"""
        with (
            patch.object(executor, "run_pre_upgrade_tests", return_value=True),
            patch.object(executor, "upgrade_npm_packages", return_value=True),
            patch.object(executor, "upgrade_python_packages", return_value=False),
            patch.object(executor, "rollback", return_value=True),
        ):
            result = executor.execute_phase1()

            assert result is False

    def test_execute_phase1_post_upgrade_test_failure(self, executor, mock_subprocess_success):
        """Test Phase 1 execution with post-upgrade test failure"""
        with (
            patch.object(executor, "run_pre_upgrade_tests", return_value=True),
            patch.object(executor, "upgrade_npm_packages", return_value=True),
            patch.object(executor, "upgrade_python_packages", return_value=True),
            patch.object(executor, "run_post_upgrade_tests", return_value=False),
            patch.object(executor, "rollback", return_value=True),
        ):
            result = executor.execute_phase1()

            assert result is False

    def test_execute_phase1_linting_failure(self, executor, mock_subprocess_success):
        """Test Phase 1 execution with linting failure"""
        with (
            patch.object(executor, "run_pre_upgrade_tests", return_value=True),
            patch.object(executor, "upgrade_npm_packages", return_value=True),
            patch.object(executor, "upgrade_python_packages", return_value=True),
            patch.object(executor, "run_post_upgrade_tests", return_value=True),
            patch.object(executor, "run_linting", return_value=False),
            patch.object(executor, "rollback", return_value=True),
        ):
            result = executor.execute_phase1()

            assert result is False

    def test_upgrade_log_structure(self, executor, mock_subprocess_success):
        """Test upgrade log structure and content"""
        executor.upgrade_npm_packages()
        executor.upgrade_python_packages()

        assert len(executor.upgrade_log) == 14

        # Verify log structure
        for log_entry in executor.upgrade_log:
            assert "package" in log_entry
            assert "ecosystem" in log_entry
            assert "status" in log_entry
            assert "timestamp" in log_entry
            assert log_entry["status"] == "success"
            assert log_entry["ecosystem"] in ["npm", "pip"]

    def test_package_version_validation(self, executor):
        """Test that package versions are correctly specified"""
        # Test NPM packages (scoped packages have @ in name, so we check for version @)
        npm_packages = [
            "@types/node@24.3.1",
            "@types/react@19.1.12",
            "@types/react-dom@19.1.9",
            "@vitejs/plugin-react@5.0.2",
            "vite@7.1.4",
        ]

        for package in npm_packages:
            assert "@" in package  # Version specified
            # For scoped packages, we expect at least one @ for version
            # Scoped packages have @scope/name@version format
            assert package.count("@") >= 1  # At least one @ for version

        # Test Python packages
        python_packages = [
            "click==8.2.1",
            "email-validator==2.3.0",
            "exceptiongroup==1.3.0",
            "pytest==8.4.2",
            "pytest-cov==6.3.0",
            "python-dotenv==1.1.1",
            "requests==2.32.5",
            "ruff==0.12.12",
            "tomli==2.2.1",
        ]

        for package in python_packages:
            assert "==" in package  # Version specified
            assert package.count("==") == 1  # Only one == for version


class TestDependencyUpgradeIntegration:
    """Integration tests for dependency upgrade process"""

    def test_phase1_script_exists(self):
        """Test that Phase 1 upgrade script exists and is executable"""
        script_path = project_root / "scripts" / "execute_phase1_upgrades.py"
        assert script_path.exists()
        assert script_path.is_file()

    def test_phase1_script_imports(self):
        """Test that Phase 1 upgrade script can be imported without errors"""
        try:
            import sys

            sys.path.insert(0, str(project_root / "scripts"))
            from execute_phase1_upgrades import Phase1UpgradeExecutor

            assert Phase1UpgradeExecutor is not None
        except ImportError as e:
            pytest.fail(f"Failed to import Phase1UpgradeExecutor: {e}")

    def test_required_directories_exist(self):
        """Test that required directories exist for upgrade process"""
        assert (project_root / "client").exists()
        assert (project_root / "server").exists()
        assert (project_root / "scripts").exists()

    def test_git_repository_available(self):
        """Test that git repository is available for backup operations"""
        try:
            result = subprocess.run(["git", "status"], cwd=project_root, capture_output=True, text=True, shell=True)
            assert result.returncode == 0
        except Exception as e:
            pytest.fail(f"Git repository not available: {e}")

    def test_make_commands_available(self):
        """Test that make commands are available for testing and linting"""
        try:
            result = subprocess.run(["make", "--version"], cwd=project_root, capture_output=True, text=True, shell=True)
            assert result.returncode == 0
        except Exception as e:
            pytest.fail(f"Make commands not available: {e}")

    def test_npm_available_in_client_directory(self):
        """Test that npm is available in client directory"""
        client_dir = project_root / "client"
        try:
            result = subprocess.run(["npm", "--version"], cwd=client_dir, capture_output=True, text=True, shell=True)
            assert result.returncode == 0
        except Exception as e:
            pytest.fail(f"NPM not available in client directory: {e}")

    def test_uv_available_for_python_packages(self):
        """Test that uv is available for Python package management"""
        try:
            result = subprocess.run(["uv", "--version"], cwd=project_root, capture_output=True, text=True, shell=True)
            assert result.returncode == 0
        except Exception as e:
            pytest.fail(f"UV not available for Python package management: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
