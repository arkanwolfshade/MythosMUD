"""
Test file containment to ensure database and log files are only created in approved
locations.

These tests verify that no database or log files are created outside of their
designated directories during test execution.
"""

from pathlib import Path


def test_no_database_files_outside_approved_locations():
    """
    Test that no .db files exist outside of approved locations.

    Approved locations:
    - /data/players/ (production databases)
    - /server/tests/data/players/ (test databases)
    """
    # Get the project root directory
    project_root = Path(__file__).parent.parent.parent

    # Define approved database locations (relative to project root)
    approved_db_locations = [
        project_root / "data" / "players",
        project_root / "server" / "tests" / "data" / "players",
    ]

    # Find all .db files in the project
    db_files = []
    for db_file in project_root.rglob("*.db"):
        db_files.append(db_file)

    # Check each .db file to ensure it's in an approved location
    unauthorized_db_files = []
    for db_file in db_files:
        is_approved = False
        for approved_location in approved_db_locations:
            try:
                db_file.relative_to(approved_location)
                is_approved = True
                break
            except ValueError:
                # File is not in this approved location, check next
                continue

        if not is_approved:
            unauthorized_db_files.append(str(db_file))

    # If unauthorized database files are found, fail the test
    if unauthorized_db_files:
        error_message = (
            "Database files found outside approved locations:\n"
            f"Approved locations: {[str(loc) for loc in approved_db_locations]}\n"
            f"Unauthorized files: {unauthorized_db_files}"
        )
        raise AssertionError(error_message)

    # Test passes if no unauthorized database files are found
    assert True, "All database files are in approved locations"


def test_no_log_files_outside_approved_locations():
    """
    Test that no .log files exist outside of approved locations.

    Approved locations:
    - /logs/ (project root logs - all environment subdirectories)
    - /server/tests/logs/ (test logs - all environment subdirectories)
    - /client/logs/ (client logs)
    - /room_validator/ (room validator logs)
    - /server/logs/ (server logs - all environment subdirectories)
    """
    # Get the project root directory
    project_root = Path(__file__).parent.parent.parent

    # Define approved log locations (relative to project root)
    # These are the base directories - all subdirectories within them are approved
    approved_log_locations = [
        project_root / "logs",
        project_root / "server" / "tests" / "logs",
        project_root / "client" / "logs",
        project_root / "room_validator",
        project_root / "server" / "logs",
    ]

    # Find all .log files in the project
    log_files = []
    for log_file in project_root.rglob("*.log"):
        log_files.append(log_file)

    # Check each .log file to ensure it's in an approved location
    unauthorized_log_files = []
    for log_file in log_files:
        is_approved = False
        for approved_location in approved_log_locations:
            try:
                # Check if the log file is within the approved location
                # This allows for subdirectories like logs/development/, etc.
                log_file.relative_to(approved_location)
                is_approved = True
                break
            except ValueError:
                # File is not in this approved location, check next
                continue

        if not is_approved:
            unauthorized_log_files.append(str(log_file))

    # If unauthorized log files are found, fail the test
    if unauthorized_log_files:
        error_message = (
            "Log files found outside approved locations:\n"
            f"Approved locations: {[str(loc) for loc in approved_log_locations]}\n"
            f"Unauthorized files: {unauthorized_log_files}"
        )
        raise AssertionError(error_message)

    # Test passes if no unauthorized log files are found
    assert True, "All log files are in approved locations"
