"""Custom JWT strategy that invalidates tokens after server restart.

Tokens must include the current auth epoch (srv claim). Tokens issued
before the current server process started are rejected.
"""

from typing import Any

import jwt
from fastapi_users import exceptions, models
from fastapi_users.authentication.strategy.jwt import JWTStrategy
from fastapi_users.jwt import decode_jwt
from fastapi_users.manager import BaseUserManager

from .token_epoch import get_auth_epoch


class RestartInvalidatingJWTStrategy(JWTStrategy[models.UP, models.ID]):
    """JWT strategy that rejects tokens issued before the current server start."""

    async def read_token(
        self, token: str | None, user_manager: BaseUserManager[models.UP, models.ID]
    ) -> models.UP | None:
        """Reads a JWT token, validating its signature, audience, and server epoch."""
        from ..structured_logging.enhanced_logging_config import get_logger

        logger = get_logger(__name__)

        if token is None:
            logger.debug("JWT read_token: token is None")
            return None

        logger.debug(
            "JWT read_token: token received", token_length=len(token), token_preview=token[:50] if token else None
        )

        try:
            data: dict[str, Any] = decode_jwt(token, self.decode_key, self.token_audience, algorithms=[self.algorithm])
            logger.debug(
                "JWT decode successful", has_srv=("srv" in data), srv_value=data.get("srv"), has_sub=("sub" in data)
            )
        except jwt.PyJWTError as e:
            logger.warning("JWT decode failed", error=str(e), error_type=type(e).__name__)
            return None

        # Reject tokens from before this server restart
        current_epoch = get_auth_epoch()
        token_epoch = data.get("srv")
        if token_epoch != current_epoch:
            logger.warning(
                "JWT epoch mismatch",
                token_epoch=token_epoch,
                current_epoch=current_epoch,
                epoch_match=token_epoch == current_epoch,
            )
            return None

        user_id = data.get("sub")
        if user_id is None:
            logger.warning("JWT missing sub claim")
            return None

        try:
            parsed_id = user_manager.parse_id(user_id)
            user = await user_manager.get(parsed_id)
            if user:
                logger.debug("JWT validation successful", user_id=str(user.id))
            else:
                logger.warning("JWT user lookup returned None", parsed_user_id=str(parsed_id))
            return user
        except (exceptions.UserNotExists, exceptions.InvalidID) as e:
            logger.warning("JWT user lookup failed", user_id=user_id, error=str(e), error_type=type(e).__name__)
            return None
