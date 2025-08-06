import os
from datetime import UTC, datetime, timedelta

from jose import JWTError, jwt

# Import our Argon2 implementation
from server.auth.argon2_utils import hash_password as argon2_hash_password
from server.auth.argon2_utils import verify_password as argon2_verify_password
from server.logging_config import get_logger

logger = get_logger(__name__)

# Use environment variable for secret key - CRITICAL: Must be set in production
SECRET_KEY = os.getenv("MYTHOSMUD_SECRET_KEY")
if not SECRET_KEY:
    logger.error("MYTHOSMUD_SECRET_KEY environment variable not set")
    raise ValueError(
        "MYTHOSMUD_SECRET_KEY environment variable must be set. Generate a secure random key for production deployment."
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
        return hashed
    except Exception as e:
        logger.error("Password hashing failed", error=str(e))
        raise


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
        return result
    except Exception as e:
        logger.error("Password verification error", error=str(e))
        return False


def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None,
    secret_key: str = SECRET_KEY,
    algorithm: str = ALGORITHM,
) -> str:
    """Create a JWT access token."""
    logger.debug("Creating access token", user_id=data.get("sub"), expires_delta=expires_delta)

    to_encode = data.copy()
    expire = datetime.now(UTC) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})

    try:
        token = jwt.encode(to_encode, secret_key, algorithm=algorithm)
        logger.debug("Access token created successfully", user_id=data.get("sub"))
        return token
    except Exception as e:
        logger.error("Failed to create access token", error=str(e), user_id=data.get("sub"))
        raise


def decode_access_token(token: str, secret_key: str = SECRET_KEY, algorithm: str = ALGORITHM) -> dict:
    """Decode and validate a JWT access token."""
    if token is None:
        logger.debug("No token provided for decoding")
        return None

    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm], audience="fastapi-users:auth")
        logger.debug("Access token decoded successfully", user_id=payload.get("sub"))
        return payload
    except JWTError as e:
        logger.warning("JWT decode error", error=str(e))
        return None
    except Exception as e:
        logger.error("Unexpected error decoding token", error=str(e))
        return None
