# 🐙 MythosMUD Command Security Guide

*"The most merciful thing in the world is the inability of malicious input to corrupt our systems."* - H.P. Lovecraft
(adapted)

---

## Table of Contents

1. [Overview](#overview)
2. [Security Principles](#security-principles)
3. [Input Validation](#input-validation)
4. [Authorization and Access Control](#authorization-and-access-control)
5. [Injection Prevention](#injection-prevention)
6. [Rate Limiting](#rate-limiting)
7. [Logging and Monitoring](#logging-and-monitoring)
8. [Error Handling](#error-handling)
9. [Data Protection](#data-protection)
10. [Security Testing](#security-testing)
11. [Common Vulnerabilities](#common-vulnerabilities)
12. [Security Checklist](#security-checklist)

---

## Overview

Security is paramount in MythosMUD command development. This guide provides comprehensive security practices to protect
against common vulnerabilities and ensure the safety of players and the system.

### Security Goals

**Confidentiality**: Protect sensitive player data

**Integrity**: Ensure data accuracy and consistency

**Availability**: Maintain system functionality

**Authentication**: Verify user identity

**Authorization**: Control access to resources

### Threat Model

Common threats to command systems:
**Input Injection**: SQL, XSS, command injection

**Privilege Escalation**: Unauthorized access to admin functions

**Denial of Service**: Resource exhaustion attacks

**Information Disclosure**: Leaking sensitive data

**Session Hijacking**: Unauthorized access to user sessions

---

## Security Principles

### Defense in Depth

Implement multiple layers of security:

```python
# Layer 1: Input validation

validated_input = validate_user_input(raw_input)

# Layer 2: Authorization check

if not is_authorized(user, action):
    return {"result": "Unauthorized"}

# Layer 3: Sanitization

sanitized_input = sanitize_input(validated_input)

# Layer 4: Rate limiting

if not rate_limiter.allow(user, action):
    return {"result": "Rate limit exceeded"}

# Layer 5: Execution with error handling

try:
    result = execute_command(sanitized_input)
except SecurityException as e:
    log_security_event(e)
    return {"result": "Security error"}
```

### Principle of Least Privilege

Commands should only have the minimum permissions necessary:

```python
async def handle_admin_command(command_data, current_user, request, alias_storage, player_name):
    """Admin command with minimal privilege principle."""

    # Check specific permission, not just admin status

    if not current_user.get("can_manage_players", False):
        return {"result": "Insufficient permissions for player management"}

    # Only access necessary data

    target_player = command_data.get("target_player")
    if not target_player:
        return {"result": "Target player required"}

    # Validate target is within scope

    if not can_manage_player(current_user, target_player):
        return {"result": "Cannot manage that player"}

    # Perform action with minimal scope

    return await perform_player_action(target_player, command_data.get("action"))
```

### Fail Securely

Always fail to a secure state:

```python
async def handle_secure_command(command_data, current_user, request, alias_storage, player_name):
    """Command that fails securely."""

    try:
        # Validate input first

        if not validate_command_input(command_data):
            return {"result": "Invalid input"}

        # Check authorization

        if not is_authorized(current_user, "command_action"):
            return {"result": "Unauthorized"}

        # Perform action

        result = await perform_action(command_data)
        return {"result": result}

    except Exception as e:
        # Log the error but don't expose details

        logger.error(f"Command error for {player_name}: {str(e)}")
        return {"result": "An error occurred"}
```

---

## Input Validation

### Pydantic Model Validation

Use Pydantic for comprehensive input validation:

```python
class SecureCommand(BaseCommand):
    """Command with comprehensive input validation."""

    command_type: Literal[CommandType.SECURE] = CommandType.SECURE
    parameter: str = Field(..., min_length=1, max_length=100)

    @field_validator("parameter")
    @classmethod
    def validate_parameter(cls, v):
        """Comprehensive parameter validation."""
        if not v or not v.strip():
            raise ValueError("Parameter cannot be empty")

        # Check for dangerous patterns

        dangerous_patterns = [
            r"<script", r"javascript:", r"onload=", r"onerror=",
            r"';", r"--", r"/*", r"*/", r"xp_", r"sp_"
        ]

        for pattern in dangerous_patterns:
            if re.search(pattern, v, re.IGNORECASE):
                raise ValueError("Parameter contains forbidden content")

        # Check for excessive whitespace

        if len(v) != len(v.strip()):
            raise ValueError("Parameter cannot start or end with whitespace")

        # Check for control characters

        if any(ord(char) < 32 for char in v):
            raise ValueError("Parameter contains control characters")

        return v.strip()
```

### Custom Validation Functions

```python
def validate_player_name(name: str) -> bool:
    """Validate player name for security."""
    if not name or len(name) > 50:
        return False

    # Only allow alphanumeric and underscores

    if not re.match(r"^[a-zA-Z0-9_]+$", name):
        return False

    # Check for reserved names

    reserved_names = {"admin", "root", "system", "guest", "anonymous"}
    if name.lower() in reserved_names:
        return False

    return True

def validate_message_content(message: str) -> bool:
    """Validate message content for security."""
    if not message or len(message) > 500:
        return False

    # Check for HTML/script injection

    html_patterns = [
        r"<[^>]*>", r"javascript:", r"on\w+\s*=", r"data:text/html"
    ]

    for pattern in html_patterns:
        if re.search(pattern, message, re.IGNORECASE):
            return False

    return True
```

### Input Sanitization

```python
import html
import re

def sanitize_input(input_string: str) -> str:
    """Sanitize user input to prevent injection attacks."""

    if not input_string:
        return ""

    # HTML escape

    sanitized = html.escape(input_string)

    # Remove any remaining script tags

    sanitized = re.sub(r"<script[^>]*>.*?</script>", "", sanitized, flags=re.IGNORECASE | re.DOTALL)

    # Remove event handlers

    sanitized = re.sub(r"on\w+\s*=\s*['\"][^'\"]*['\"]", "", sanitized, flags=re.IGNORECASE)

    # Remove javascript: URLs

    sanitized = re.sub(r"javascript:[^'\"]*", "", sanitized, flags=re.IGNORECASE)

    return sanitized.strip()

def sanitize_filename(filename: str) -> str:
    """Sanitize filename to prevent path traversal."""

    # Remove path traversal attempts

    filename = re.sub(r"\.\./|\.\.\\", "", filename)
    filename = re.sub(r"^/|^\\", "", filename)

    # Only allow safe characters

    filename = re.sub(r"[^a-zA-Z0-9._-]", "", filename)

    return filename[:100]  # Limit length
```

---

## Authorization and Access Control

### Role-Based Access Control

```python
class UserRoles:
    """User role definitions."""
    PLAYER = "player"
    MODERATOR = "moderator"
    ADMIN = "admin"
    SUPER_ADMIN = "super_admin"

class CommandPermissions:
    """Command permission definitions."""
    CHAT = "chat"
    MOVE = "move"
    MODERATE = "moderate"
    ADMIN = "admin"
    SYSTEM = "system"

def check_permission(user: dict, permission: str) -> bool:
    """Check if user has specific permission."""

    user_role = user.get("role", UserRoles.PLAYER)

    # Define permission hierarchy

    role_permissions = {
        UserRoles.PLAYER: [CommandPermissions.CHAT, CommandPermissions.MOVE],
        UserRoles.MODERATOR: [CommandPermissions.CHAT, CommandPermissions.MOVE, CommandPermissions.MODERATE],
        UserRoles.ADMIN: [CommandPermissions.CHAT, CommandPermissions.MOVE, CommandPermissions.MODERATE, CommandPermissions.ADMIN],
        UserRoles.SUPER_ADMIN: [CommandPermissions.CHAT, CommandPermissions.MOVE, CommandPermissions.MODERATE,
        CommandPermissions.ADMIN, CommandPermissions.SYSTEM]
    }

    return permission in role_permissions.get(user_role, [])

async def handle_authorized_command(command_data, current_user, request, alias_storage, player_name):
    """Command with proper authorization checks."""

    # Check basic permission

    if not check_permission(current_user, CommandPermissions.ADMIN):
        return {"result": "Insufficient permissions"}

    # Check specific action permission

    action = command_data.get("action")
    if not check_action_permission(current_user, action):
        return {"result": f"Cannot perform action: {action}"}

    # Check target scope

    target = command_data.get("target")
    if target and not can_affect_target(current_user, target):
        return {"result": f"Cannot affect target: {target}"}

    # Perform authorized action

    return await perform_authorized_action(command_data)
```

### Session-Based Authorization

```python
def validate_session(session_token: str, user_id: str) -> bool:
    """Validate user session."""

    try:
        # Decode and verify JWT token

        payload = jwt.decode(session_token, SECRET_KEY, algorithms=["HS256"])

        # Check token expiration

        if payload.get("exp", 0) < time.time():
            return False

        # Check user ID matches

        if payload.get("user_id") != user_id:
            return False

        # Check token is not revoked

        if is_token_revoked(session_token):
            return False

        return True

    except jwt.InvalidTokenError:
        return False

async def handle_session_authorized_command(command_data, current_user, request, alias_storage, player_name):
    """Command with session-based authorization."""

    # Get session token from request

    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return {"result": "Authentication required"}

    session_token = auth_header[7:]  # Remove "Bearer " prefix

    # Validate session

    if not validate_session(session_token, current_user.get("user_id")):
        return {"result": "Invalid or expired session"}

    # Check command-specific permissions

    if not check_command_permission(current_user, command_data.get("command_type")):
        return {"result": "Command not allowed"}

    # Perform authorized action

    return await execute_command(command_data)
```

---

## Injection Prevention

### SQL Injection Prevention

```python
# GOOD - Use parameterized queries

async def get_player_safely(player_name: str) -> Optional[Player]:
    """Get player using parameterized query."""

    query = "SELECT * FROM players WHERE username = ?"
    result = await database.execute(query, (player_name,))
    return result.fetchone() if result else None

# BAD - String concatenation (vulnerable to SQL injection)

async def get_player_unsafe(player_name: str) -> Optional[Player]:
    """Get player using unsafe string concatenation."""

    query = f"SELECT * FROM players WHERE username = '{player_name}'"
    result = await database.execute(query)
    return result.fetchone() if result else None

# Use ORM for additional safety

async def get_player_orm(player_name: str) -> Optional[Player]:
    """Get player using ORM."""

    return await Player.objects.filter(username=player_name).first()
```

### Command Injection Prevention

```python
def validate_command_syntax(command: str) -> bool:
    """Validate command syntax to prevent injection."""

    # Check for shell command injection attempts

    shell_patterns = [
        r";\s*\w+", r"&\s*\w+", r"\|\s*\w+", r"`.*`", r"\$\(.*\)",
        r">\s*\w+", r"<\s*\w+", r"2>&1", r">/dev/null"
    ]

    for pattern in shell_patterns:
        if re.search(pattern, command):
            return False

    # Check for path traversal

    if ".." in command or "~" in command:
        return False

    # Check for absolute paths

    if command.startswith("/") or command.startswith("\\"):
        return False

    return True

async def handle_safe_command(command_data, current_user, request, alias_storage, player_name):
    """Command handler with injection prevention."""

    command_string = command_data.get("command", "")

    # Validate command syntax

    if not validate_command_syntax(command_string):
        logger.warning(f"Invalid command syntax from {player_name}: {command_string}")
        return {"result": "Invalid command syntax"}

    # Use whitelist approach

    allowed_commands = {"look", "go", "say", "emote", "help"}
    command_parts = command_string.split()

    if not command_parts or command_parts[0] not in allowed_commands:
        return {"result": "Unknown command"}

    # Execute command safely

    return await execute_safe_command(command_parts)
```

### XSS Prevention

```python
def prevent_xss(content: str) -> str:
    """Prevent XSS attacks in content."""

    if not content:
        return ""

    # HTML escape

    content = html.escape(content)

    # Remove any remaining script tags

    content = re.sub(r"<script[^>]*>.*?</script>", "", content, flags=re.IGNORECASE | re.DOTALL)

    # Remove event handlers

    content = re.sub(r"on\w+\s*=\s*['\"][^'\"]*['\"]", "", content, flags=re.IGNORECASE)

    # Remove javascript: URLs

    content = re.sub(r"javascript:[^'\"]*", "", content, flags=re.IGNORECASE)

    # Remove data: URLs

    content = re.sub(r"data:text/html[^'\"]*", "", content, flags=re.IGNORECASE)

    return content

async def handle_xss_safe_command(command_data, current_user, request, alias_storage, player_name):
    """Command handler with XSS prevention."""

    message = command_data.get("message", "")

    # Prevent XSS in message

    safe_message = prevent_xss(message)

    # Log original message for moderation

    logger.info(f"Message from {player_name}: {message}")

    # Use safe message in response

    return {"result": f"Message sent: {safe_message}"}
```

---

## Rate Limiting

### Token Bucket Rate Limiting

```python
import time
from collections import defaultdict

class RateLimiter:
    """Token bucket rate limiter for commands."""

    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = defaultdict(lambda: capacity)
        self.last_refill = defaultdict(time.time)

    def allow(self, user_id: str) -> bool:
        """Check if user can perform action."""

        now = time.time()
        last_time = self.last_refill[user_id]

        # Refill tokens

        time_passed = now - last_time
        tokens_to_add = time_passed * self.refill_rate
        self.tokens[user_id] = min(self.capacity, self.tokens[user_id] + tokens_to_add)
        self.last_refill[user_id] = now

        # Check if tokens available

        if self.tokens[user_id] >= 1:
            self.tokens[user_id] -= 1
            return True

        return False

# Global rate limiters

command_rate_limiter = RateLimiter(capacity=10, refill_rate=1.0)  # 10 commands per second
chat_rate_limiter = RateLimiter(capacity=5, refill_rate=0.5)      # 5 messages per 2 seconds

async def handle_rate_limited_command(command_data, current_user, request, alias_storage, player_name):
    """Command handler with rate limiting."""

    user_id = current_user.get("user_id", player_name)
    command_type = command_data.get("command_type")

    # Choose appropriate rate limiter

    if command_type in {"say", "emote", "me", "pose"}:
        limiter = chat_rate_limiter
    else:
        limiter = command_rate_limiter

    # Check rate limit

    if not limiter.allow(user_id):
        logger.warning(f"Rate limit exceeded for {player_name}: {command_type}")
        return {"result": "You're using that command too frequently. Please wait a moment."}

    # Execute command

    return await execute_command(command_data)
```

### Sliding Window Rate Limiting

```python
from collections import deque

class SlidingWindowRateLimiter:
    """Sliding window rate limiter."""

    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(deque)

    def allow(self, user_id: str) -> bool:
        """Check if user can perform action."""

        now = time.time()
        user_requests = self.requests[user_id]

        # Remove old requests outside window

        while user_requests and user_requests[0] < now - self.window_seconds:
            user_requests.popleft()

        # Check if under limit

        if len(user_requests) < self.max_requests:
            user_requests.append(now)
            return True

        return False

# Create rate limiters for different command types

admin_rate_limiter = SlidingWindowRateLimiter(max_requests=5, window_seconds=60)
teleport_rate_limiter = SlidingWindowRateLimiter(max_requests=1, window_seconds=30)
```

---

## Logging and Monitoring

### Security Event Logging

```python
import json
from datetime import datetime

class SecurityLogger:
    """Logger for security events."""

    def __init__(self, log_file: str):
        self.log_file = log_file

    def log_security_event(self, event_type: str, user_id: str, details: dict):
        """Log a security event."""

        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "user_id": user_id,
            "details": details,
            "ip_address": details.get("ip_address", "unknown"),
            "user_agent": details.get("user_agent", "unknown")
        }

        with open(self.log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")

# Global security logger

security_logger = SecurityLogger("logs/security_events.log")

async def handle_logged_command(command_data, current_user, request, alias_storage, player_name):
    """Command handler with security logging."""

    # Log command attempt

    security_logger.log_security_event(
        "command_attempt",
        player_name,
        {
            "command_type": command_data.get("command_type"),
            "parameters": command_data,
            "ip_address": request.client.host if request.client else "unknown",
            "user_agent": request.headers.get("user-agent", "unknown")
        }
    )

    # Check for suspicious patterns

    if is_suspicious_command(command_data):
        security_logger.log_security_event(
            "suspicious_command",
            player_name,
            {
                "command_type": command_data.get("command_type"),
                "parameters": command_data,
                "reason": "Suspicious pattern detected"
            }
        )
        return {"result": "Command blocked for security reasons"}

    # Execute command

    result = await execute_command(command_data)

    # Log successful execution

    security_logger.log_security_event(
        "command_success",
        player_name,
        {
            "command_type": command_data.get("command_type"),
            "result": "success"
        }
    )

    return result
```

### Audit Trail

```python
class AuditTrail:
    """Audit trail for sensitive operations."""

    def __init__(self, database):
        self.database = database

    async def log_operation(self, user_id: str, operation: str, target: str, details: dict):
        """Log an auditable operation."""

        audit_entry = {
            "user_id": user_id,
            "operation": operation,
            "target": target,
            "details": json.dumps(details),
            "timestamp": datetime.utcnow().isoformat(),
            "ip_address": details.get("ip_address", "unknown")
        }

        await self.database.execute(
            "INSERT INTO audit_log (user_id, operation, target, details, timestamp, ip_address) VALUES (?, ?, ?, ?, ?, ?)",
            (audit_entry["user_id"], audit_entry["operation"], audit_entry["target"],
             audit_entry["details"], audit_entry["timestamp"], audit_entry["ip_address"])
        )

# Global audit trail

audit_trail = AuditTrail(database)

async def handle_audited_command(command_data, current_user, request, alias_storage, player_name):
    """Command handler with audit trail."""

    user_id = current_user.get("user_id", player_name)
    operation = command_data.get("command_type")
    target = command_data.get("target", "none")

    # Log operation attempt

    await audit_trail.log_operation(
        user_id,
        operation,
        target,
        {
            "parameters": command_data,
            "ip_address": request.client.host if request.client else "unknown",
            "user_agent": request.headers.get("user-agent", "unknown")
        }
    )

    # Execute command

    result = await execute_command(command_data)

    # Log operation result

    await audit_trail.log_operation(
        user_id,
        f"{operation}_result",
        target,
        {
            "success": "result" in result,
            "result": result.get("result", "error")
        }
    )

    return result
```

---

## Error Handling

### Secure Error Messages

```python
class SecurityException(Exception):
    """Base class for security-related exceptions."""
    pass

class InputValidationException(SecurityException):
    """Exception for input validation failures."""
    pass

class AuthorizationException(SecurityException):
    """Exception for authorization failures."""
    pass

async def handle_secure_error_command(command_data, current_user, request, alias_storage, player_name):
    """Command handler with secure error handling."""

    try:
        # Validate input

        if not validate_command_input(command_data):
            raise InputValidationException("Invalid command input")

        # Check authorization

        if not is_authorized(current_user, command_data.get("command_type")):
            raise AuthorizationException("Insufficient permissions")

        # Execute command

        result = await execute_command(command_data)
        return result

    except InputValidationException as e:
        # Log the error but don't expose details

        logger.warning(f"Input validation failed for {player_name}: {str(e)}")
        return {"result": "Invalid input provided"}

    except AuthorizationException as e:
        # Log authorization failure

        logger.warning(f"Authorization failed for {player_name}: {str(e)}")
        return {"result": "You don't have permission for that action"}

    except Exception as e:
        # Log unexpected errors but don't expose details

        logger.error(f"Unexpected error for {player_name}: {str(e)}")
        return {"result": "An error occurred while processing your command"}
```

### Error Information Disclosure

```python
# GOOD - Don't expose sensitive information

async def handle_secure_error_command(command_data, current_user, request, alias_storage, player_name):
    try:
        # Command logic

        pass
    except Exception as e:
        # Log full error for debugging

        logger.error(f"Command error for {player_name}: {str(e)}", exc_info=True)

        # Return generic error to user

        return {"result": "An error occurred"}

# BAD - Exposing sensitive information

async def handle_insecure_error_command(command_data, current_user, request, alias_storage, player_name):
    try:
        # Command logic

        pass
    except Exception as e:
        # Don't do this - exposes internal details

        return {"result": f"Error: {str(e)}", "traceback": traceback.format_exc()}
```

---

## Data Protection

### Sensitive Data Handling

```python
import hashlib
import secrets

def hash_sensitive_data(data: str) -> str:
    """Hash sensitive data for storage."""
    salt = secrets.token_hex(16)
    hash_obj = hashlib.pbkdf2_hmac('sha256', data.encode(), salt.encode(), 100000)
    return f"{salt}:{hash_obj.hex()}"

def verify_sensitive_data(data: str, hashed_data: str) -> bool:
    """Verify sensitive data against hash."""
    try:
        salt, hash_hex = hashed_data.split(":")
        hash_obj = hashlib.pbkdf2_hmac('sha256', data.encode(), salt.encode(), 100000)
        return hash_obj.hex() == hash_hex
    except:
        return False

async def handle_sensitive_data_command(command_data, current_user, request, alias_storage, player_name):
    """Command handler for sensitive data."""

    sensitive_info = command_data.get("sensitive_info")

    if sensitive_info:
        # Hash sensitive data before storing

        hashed_info = hash_sensitive_data(sensitive_info)

        # Store only the hash

        await store_hashed_data(player_name, hashed_info)

        # Don't return sensitive data in response

        return {"result": "Information stored securely"}

    return {"result": "No sensitive information provided"}
```

### Data Encryption

```python
from cryptography.fernet import Fernet

class DataEncryption:
    """Data encryption utilities."""

    def __init__(self, key: bytes):
        self.cipher = Fernet(key)

    def encrypt_data(self, data: str) -> str:
        """Encrypt sensitive data."""
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt sensitive data."""
        return self.cipher.decrypt(encrypted_data.encode()).decode()

# Global encryption instance

encryption = DataEncryption(ENCRYPTION_KEY)

async def handle_encrypted_command(command_data, current_user, request, alias_storage, player_name):
    """Command handler with data encryption."""

    sensitive_message = command_data.get("message")

    if sensitive_message:
        # Encrypt message before storing

        encrypted_message = encryption.encrypt_data(sensitive_message)

        # Store encrypted message

        await store_encrypted_message(player_name, encrypted_message)

        # Return success without exposing original message

        return {"result": "Message encrypted and stored"}

    return {"result": "No message provided"}
```

---

## Security Testing

### Automated Security Tests

```python
import pytest

class TestCommandSecurity:
    """Security tests for commands."""

    @pytest.mark.asyncio
    async def test_sql_injection_prevention(self):
        """Test SQL injection prevention."""

        malicious_inputs = [
            "'; DROP TABLE players; --",
            "' OR '1'='1",
            "'; INSERT INTO players VALUES ('hacker', 'admin'); --"
        ]

        for malicious_input in malicious_inputs:
            result = await handle_command({"parameter": malicious_input})
            assert "error" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_xss_prevention(self):
        """Test XSS prevention."""

        malicious_inputs = [
            "<script>alert('xss')</script>",
            "javascript:alert('xss')",
            "<img src=x onerror=alert('xss')>"
        ]

        for malicious_input in malicious_inputs:
            result = await handle_command({"message": malicious_input})
            assert "<script>" not in result["result"]
            assert "javascript:" not in result["result"]

    @pytest.mark.asyncio
    async def test_authorization_bypass(self):
        """Test authorization bypass prevention."""

        # Test non-admin user trying admin command

        non_admin_user = {"username": "player", "is_admin": False}
        result = await handle_admin_command(
            {"action": "delete_player"},
            non_admin_user,
            None,
            None,
            "player"
        )
        assert "permission" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_rate_limiting(self):
        """Test rate limiting functionality."""

        # Send multiple requests rapidly

        for _ in range(15):  # Exceed rate limit
            result = await handle_rate_limited_command({"command_type": "test"})

        # Last request should be rate limited

        assert "too frequently" in result["result"]
```

### Penetration Testing

```python
class SecurityPenetrationTests:
    """Penetration testing for commands."""

    @pytest.mark.asyncio
    async def test_command_injection(self):
        """Test command injection vulnerabilities."""

        injection_payloads = [
            "; rm -rf /",
            "& cat /etc/passwd",
            "| whoami",
            "`id`",
            "$(whoami)"
        ]

        for payload in injection_payloads:
            result = await handle_command({"command": payload})
            # Should not execute system commands

            assert "error" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_privilege_escalation(self):
        """Test privilege escalation attempts."""

        # Test user trying to access admin functions

        regular_user = {"username": "user", "role": "player"}

        admin_commands = [
            {"command_type": "add_admin", "target": "hacker"},
            {"command_type": "delete_player", "target": "admin"},
            {"command_type": "system_shutdown"}
        ]

        for command in admin_commands:
            result = await handle_command(command, regular_user)
            assert "permission" in result["result"].lower()
```

---

## Common Vulnerabilities

### 1. SQL Injection

**Vulnerable Code:**

```python
# BAD - Vulnerable to SQL injection

query = f"SELECT * FROM players WHERE username = '{username}'"
```

**Secure Code:**

```python
# GOOD - Use parameterized queries

query = "SELECT * FROM players WHERE username = ?"
result = await database.execute(query, (username,))
```

### 2. XSS (Cross-Site Scripting)

**Vulnerable Code:**

```python
# BAD - Vulnerable to XSS

return {"result": f"Message: {user_message}"}
```

**Secure Code:**

```python
# GOOD - Sanitize output

safe_message = html.escape(user_message)
return {"result": f"Message: {safe_message}"}
```

### 3. Command Injection

**Vulnerable Code:**

```python
# BAD - Vulnerable to command injection

os.system(f"echo {user_input}")
```

**Secure Code:**

```python
# GOOD - Validate and sanitize input

if validate_safe_input(user_input):
    safe_input = sanitize_input(user_input)
    # Use subprocess with proper arguments

    subprocess.run(["echo", safe_input], check=True)
```

### 4. Path Traversal

**Vulnerable Code:**

```python
# BAD - Vulnerable to path traversal

with open(f"files/{filename}", "r") as f:
    content = f.read()
```

**Secure Code:**

```python
# GOOD - Validate and sanitize path

safe_filename = sanitize_filename(filename)
full_path = os.path.join("files", safe_filename)
if os.path.commonpath([full_path, "files"]) != "files":
    raise SecurityException("Invalid file path")
```

---

## Security Checklist

### Before Deploying Any Command

[ ] **Input Validation**

- [ ] All user input is validated
- [ ] Input length limits are enforced
- [ ] Dangerous characters are filtered
- [ ] Type checking is performed

- [ ] **Authorization**
  - [ ] User permissions are checked
  - [ ] Role-based access control is implemented
  - [ ] Admin functions are properly protected
  - [ ] Session validation is performed

- [ ] **Injection Prevention**
  - [ ] SQL injection is prevented
  - [ ] XSS attacks are prevented
  - [ ] Command injection is prevented
  - [ ] Path traversal is prevented

- [ ] **Rate Limiting**
  - [ ] Commands are rate limited
  - [ ] Different limits for different command types
  - [ ] Rate limits are enforced per user

- [ ] **Logging and Monitoring**
  - [ ] Security events are logged
  - [ ] Suspicious activity is detected
  - [ ] Audit trail is maintained
  - [ ] Error details are not exposed

- [ ] **Error Handling**
  - [ ] Errors are handled gracefully
  - [ ] Sensitive information is not exposed
  - [ ] System state remains consistent
  - [ ] Security exceptions are caught

- [ ] **Data Protection**
  - [ ] Sensitive data is encrypted
  - [ ] Passwords are hashed
  - [ ] Data is sanitized before storage
  - [ ] Access to sensitive data is controlled

- [ ] **Testing**
  - [ ] Security tests are written
  - [ ] Penetration testing is performed
  - [ ] Input validation is tested
  - [ ] Authorization is tested

### Regular Security Reviews

[ ] **Monthly**

- [ ] Review security logs
- [ ] Update security dependencies
- [ ] Check for new vulnerabilities
- [ ] Review access controls

- [ ] **Quarterly**
  - [ ] Perform security audit
  - [ ] Update security policies
  - [ ] Review incident response procedures
  - [ ] Conduct penetration testing

- [ ] **Annually**
  - [ ] Comprehensive security review
  - [ ] Update security documentation
  - [ ] Review and update security checklist
  - [ ] Conduct security training

---

## Conclusion

Security is not a one-time effort but an ongoing process. By following these guidelines and maintaining vigilance, you
can help ensure that MythosMUD remains a safe and secure environment for all players.

Remember:
**Security by Design**: Build security into every command from the start

**Defense in Depth**: Use multiple layers of protection

**Principle of Least Privilege**: Only grant necessary permissions

**Fail Securely**: Always fail to a secure state

**Continuous Monitoring**: Watch for security issues and respond quickly

---

*This guide should be updated regularly as new security threats emerge and best practices evolve.*
