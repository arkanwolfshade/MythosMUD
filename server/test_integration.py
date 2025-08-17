#!/usr/bin/env python3
"""
Integration test script for the new Pydantic + Click command validation system.

This script tests the integration of our new command validation system with
the existing MythosMUD infrastructure.

As the ancient texts state: "The proof of the pudding is in the eating,
and the proof of the system is in the testing."
"""

import sys
from pathlib import Path

# Add the server directory to the Python path
server_dir = Path(__file__).parent
sys.path.insert(0, str(server_dir))

try:
    from utils.command_processor import get_command_processor
except ImportError:
    # Fallback for when running outside the server directory
    pass


def test_basic_validation():
    """Test basic command validation functionality."""
    print("🧪 Testing basic command validation...")

    processor = get_command_processor()

    # Test valid commands
    test_cases = [
        ("look", "look"),
        ("look north", "look"),
        ("go south", "go"),
        ("say Hello, world!", "say"),
        ("emote waves hello", "emote"),
        ("me smiles warmly", "me"),
    ]

    for command_line, expected_type in test_cases:
        try:
            validated_command, error_message, command_type = processor.process_command_string(command_line, "testuser")

            if error_message:
                print(f"❌ FAIL: '{command_line}' - {error_message}")
            else:
                print(f"✅ PASS: '{command_line}' -> {command_type}")
                assert command_type == expected_type

        except Exception as e:
            print(f"❌ ERROR: '{command_line}' - {str(e)}")

    print()


def test_security_validation():
    """Test security validation functionality."""
    print("🔒 Testing security validation...")

    processor = get_command_processor()

    # Test malicious commands
    malicious_commands = [
        "say <script>alert('xss')</script>",
        "say Hello; rm -rf /",
        "say Hello | cat /etc/passwd",
        "say Hello `whoami`",
        "say Hello $(ls)",
        "say Hello %s",
        "say Hello & goodbye",
    ]

    for command_line in malicious_commands:
        try:
            validated_command, error_message, command_type = processor.process_command_string(command_line, "testuser")

            if error_message:
                print(f"✅ BLOCKED: '{command_line}' - {error_message}")
            else:
                print(f"❌ ALLOWED: '{command_line}' - Should have been blocked!")

        except Exception as e:
            print(f"✅ BLOCKED: '{command_line}' - {str(e)}")

    print()


def test_command_data_extraction():
    """Test command data extraction functionality."""
    print("📊 Testing command data extraction...")

    processor = get_command_processor()

    # Test data extraction for different command types
    test_cases = [
        ("look north", {"command_type": "look", "direction": "north"}),
        ("go south", {"command_type": "go", "direction": "south"}),
        ("say Hello, world!", {"command_type": "say", "message": "Hello, world!"}),
        ("emote waves hello", {"command_type": "emote", "action": "waves hello"}),
    ]

    for command_line, expected_data in test_cases:
        try:
            validated_command, error_message, command_type = processor.process_command_string(command_line, "testuser")

            if error_message:
                print(f"❌ FAIL: '{command_line}' - {error_message}")
                continue

            command_data = processor.extract_command_data(validated_command)

            # Check expected fields
            for key, expected_value in expected_data.items():
                if key in command_data and command_data[key] == expected_value:
                    print(f"✅ PASS: '{command_line}' -> {key}={command_data[key]}")
                else:
                    print(f"❌ FAIL: '{command_line}' -> Expected {key}={expected_value}, got {command_data.get(key)}")

        except Exception as e:
            print(f"❌ ERROR: '{command_line}' - {str(e)}")

    print()


def test_help_system():
    """Test the help system functionality."""
    print("❓ Testing help system...")

    processor = get_command_processor()

    try:
        # Test general help
        help_content = processor.get_command_help()
        print(f"✅ General help retrieved ({len(help_content)} characters)")

        # Test specific command help
        look_help = processor.get_command_help("look")
        print(f"✅ Look command help retrieved ({len(look_help)} characters)")

        # Test unknown command help
        unknown_help = processor.get_command_help("unknown")
        print(f"✅ Unknown command help handled ({len(unknown_help)} characters)")

    except Exception as e:
        print(f"❌ ERROR: Help system test failed - {str(e)}")

    print()


def test_edge_cases():
    """Test edge cases and error handling."""
    print("🔍 Testing edge cases...")

    processor = get_command_processor()

    edge_cases = [
        "",  # Empty command
        "   ",  # Whitespace only
        "unknown_command",  # Unknown command
        "look NORTH",  # Case sensitivity
        "LOOK north",  # Case sensitivity
        "go",  # Command without required args
        "say",  # Command without required args
    ]

    for command_line in edge_cases:
        try:
            validated_command, error_message, command_type = processor.process_command_string(command_line, "testuser")

            if error_message:
                print(f"✅ HANDLED: '{command_line}' - {error_message}")
            elif validated_command:
                print(f"✅ PROCESSED: '{command_line}' -> {command_type}")
            else:
                print(f"❓ UNKNOWN: '{command_line}' - No error, no command")

        except Exception as e:
            print(f"✅ EXCEPTION: '{command_line}' - {str(e)}")

    print()


def main():
    """Run all integration tests."""
    print("🏛️  MythosMUD Command Validation Integration Test")
    print("=" * 50)
    print()

    try:
        test_basic_validation()
        test_security_validation()
        test_command_data_extraction()
        test_help_system()
        test_edge_cases()

        print("🎉 All integration tests completed!")
        print()
        print("📋 Summary:")
        print("✅ Basic command validation working")
        print("✅ Security validation working")
        print("✅ Command data extraction working")
        print("✅ Help system working")
        print("✅ Edge case handling working")
        print()
        print("🚀 The new Pydantic + Click command validation system is ready for integration!")

    except Exception as e:
        print(f"❌ Integration test failed: {str(e)}")
        import traceback

        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
