"""NATS connect options, TLS setup, and client connect helper."""

# pylint: disable=missing-class-docstring,missing-function-docstring,too-few-public-methods  # Reason: TypedDict/Protocol stubs (PEP 544); nats_connect mirrors nats.connect kwargs

from __future__ import annotations

import ssl
from pathlib import Path
from typing import NotRequired, Protocol, TypedDict, cast

import nats
from nats.aio.client import Client

from ..config.models import NATSConfig
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger("nats")


class NatsConnectOptions(TypedDict):
    reconnect_time_wait: int
    max_reconnect_attempts: int
    connect_timeout: int
    ping_interval: int
    max_outstanding_pings: int
    token: NotRequired[str]
    user: NotRequired[str]
    password: NotRequired[str]
    tls: NotRequired[ssl.SSLContext]


class _NatsConnectFn(Protocol):
    async def __call__(self, _servers: str, **options: object) -> Client: ...


async def nats_connect(url: str, options: NatsConnectOptions) -> Client:
    connect = cast(_NatsConnectFn, nats.connect)
    if "tls" in options:
        return await connect(
            url,
            reconnect_time_wait=options["reconnect_time_wait"],
            max_reconnect_attempts=options["max_reconnect_attempts"],
            connect_timeout=options["connect_timeout"],
            ping_interval=options["ping_interval"],
            max_outstanding_pings=options["max_outstanding_pings"],
            token=options.get("token"),
            user=options.get("user"),
            password=options.get("password"),
            tls=options["tls"],
        )
    return await connect(
        url,
        reconnect_time_wait=options["reconnect_time_wait"],
        max_reconnect_attempts=options["max_reconnect_attempts"],
        connect_timeout=options["connect_timeout"],
        ping_interval=options["ping_interval"],
        max_outstanding_pings=options["max_outstanding_pings"],
        token=options.get("token"),
        user=options.get("user"),
        password=options.get("password"),
    )


def configure_nats_tls(config: NATSConfig, connect_options: NatsConnectOptions) -> None:
    """Apply TLS settings from NATS config onto connect options."""
    if not config.tls_enabled:
        return

    ssl_context = ssl.create_default_context()

    if config.tls_cert_file and config.tls_key_file:
        cert_path = Path(config.tls_cert_file)
        key_path = Path(config.tls_key_file)
        ssl_context.load_cert_chain(cert_path, key_path)
        logger.debug("Loaded TLS client certificate", cert_file=str(cert_path), key_file=str(key_path))

    if config.tls_ca_file:
        ca_path = Path(config.tls_ca_file)
        ssl_context.load_verify_locations(ca_path)
        logger.debug("Loaded TLS CA certificate", ca_file=str(ca_path))

    if config.tls_verify:
        ssl_context.check_hostname = True
        ssl_context.verify_mode = ssl.CERT_REQUIRED
    else:
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        logger.warning("TLS verification disabled - using unverified certificates")

    connect_options["tls"] = ssl_context
    logger.info("TLS enabled for NATS connection", verify=config.tls_verify)
