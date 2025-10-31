import os
from datetime import UTC, datetime, timedelta

from jose import JWTError, jwt

# Import our Argon2 implementation
from server.auth.argon2_utils import hash_password as argon2_hash_password
from server.auth.argon2_utils import verify_password as argon2_verify_password
from server.exceptions import AuthenticationError
from server.logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)

# Use environment variable for secret key - CRITICAL: Must be set in production
# Use MYTHOSMUD_JWT_SECRET for consistency with FastAPI Users system
SECRET_KEY = os.getenv("MYTHOSMUD_JWT_SECRET")
if not SECRET_KEY:
    logger.error("MYTHOSMUD_JWT_SECRET environment variable not set")
    log_and_raise(
        AuthenticationError,
        "MYTHOSMUD_JWT_SECRET environment variable must be set. Generate a secure random key for production deployment.",
        details={"missing_env_var": "MYTHOSMUD_JWT_SECRET"},
        user_friendly="Server configuration error",
    )
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

logger.info("Auth utilities initialized", algorithm=ALGORITHM, token_expire_minutes=ACCESS_TOKEN_EXPIRE_MINUTES)


def hash_password(password: str) -> str:
    """
    Hash a plaintext password using Argon2id.

    This function provides superior security compared to bcrypt,
    implementing the gold standard for password hashing as documented
    in the restricted archives of Miskatonic University.
    """
    logger.debug("Hashing password")
    try:
        hashed = argon2_hash_password(password)
        logger.debug("Password hashed successfully")
        assert isinstance(hashed, str)
        return hashed
    except Exception as e:
        logger.error("Password hashing failed", error=str(e))
        log_and_raise(
            AuthenticationError,
            f"Password hashing failed: {e}",
            details={"original_error": str(e), "error_type": type(e).__name__},
            user_friendly="Password processing failed",
        )


def verify_password(password: str, password_hash: str) -> bool:
    """
    Verify a plaintext password against a hash.

    This function safely handles both Argon2 and legacy bcrypt hashes,
    ensuring backward compatibility during the transition period.
    """
    logger.debug("Verifying password")
    try:
        result = argon2_verify_password(password, password_hash)
        if result:
            logger.debug("Password verification successful")
        else:
            logger.debug("Password verification failed")
        assert isinstance(result, bool)
        return result
    except Exception as e:
        logger.error("Password verification error", error=str(e))
        return False


def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None,
    secret_key: str | None = SECRET_KEY,
    algorithm: str = ALGORITHM,
) -> str:
    """Create a JWT access token."""
    logger.debug("Creating access token", expires_delta=expires_delta)

    to_encode = data.copy()
    expire = datetime.now(UTC) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})

    try:
        token = jwt.encode(to_encode, secret_key, algorithm=algorithm)
        logger.debug("Access token created successfully")
        assert isinstance(token, str)
        return token
    except Exception as e:
        logger.error("Failed to create access token", error=str(e))
        log_and_raise(
            AuthenticationError,
            f"Failed to create access token: {e}",
            details={"original_error": str(e), "error_type": type(e).__name__, "user_id": data.get("sub")},
            user_friendly="Authentication token creation failed",
        )


def decode_access_token(
    token: str | None, secret_key: str | None = SECRET_KEY, algorithm: str = ALGORITHM
) -> dict | None:
    """Decode and validate a JWT access token."""
    if token is None:
        logger.debug("No token provided for decoding")
        return None

    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm], audience="fastapi-users:auth")
        logger.debug("Access token decoded successfully")
        assert isinstance(payload, dict)
        return payload
    except JWTError as e:
        logger.warning("JWT decode error", error=str(e))
        return None
    except Exception as e:
        logger.error("Unexpected error decoding token", error=str(e))
        return None
