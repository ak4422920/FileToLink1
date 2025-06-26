# Thunder/__main__.py

import os

from dotenv import load_dotenv
from typing import Set, Optional, List, Dict
from Thunder.utils.logger import logger

load_dotenv("config.env")

def str_to_bool(val: str) -> bool:
    return val.lower() in ("true", "1", "t", "y", "yes")

def str_to_int_list(val: str) -> List[int]:
    return [int(x) for x in val.split() if x.isdigit()] if val else []

def str_to_int_set(val: str) -> Set[int]:
    return {int(x) for x in val.split() if x.isdigit()} if val else set()

class Var:
    API_ID: int = int(os.getenv("API_ID", "29171167"))
    API_HASH: str = os.getenv("API_HASH", "7ea2149629e445936619f06a3c0dc716")
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")

    if not all([API_ID, API_HASH, BOT_TOKEN]):
        logger.critical("Missing required Telegram API configuration")
        raise ValueError("Missing required Telegram API configuration")

    NAME: str = os.getenv("NAME", "ak_filestreambot")
    SLEEP_THRESHOLD: int = int(os.getenv("SLEEP_THRESHOLD", "120"))
    WORKERS: int = int(os.getenv("WORKERS", "8"))
    TIMEOUT: int = int(os.getenv("TIMEOUT", "90"))

    BIN_CHANNEL: int = int(os.getenv("BIN_CHANNEL", "-1002493002460"))

    if not BIN_CHANNEL:
        logger.critical("BIN_CHANNEL is required")
        raise ValueError("BIN_CHANNEL is required")

    PORT: int = int(os.getenv("PORT", "8080"))
    BIND_ADDRESS: str = os.getenv("BIND_ADDRESS", "0.0.0.0")
    PING_INTERVAL: int = int(os.getenv("PING_INTERVAL", "840"))
    NO_PORT: bool = str_to_bool(os.getenv("NO_PORT", "True"))
    CACHE_SIZE: int = int(os.getenv("CACHE_SIZE", "100"))

    OWNER_ID: List[int] = str_to_int_list(os.getenv("OWNER_ID", "7251898668"))

    if not OWNER_ID:
        logger.warning("WARNING: OWNER_ID is empty. No user will have admin access.")

    OWNER_USERNAME: str = os.getenv("OWNER_USERNAME", "The_SonGoku")

    FQDN: str = os.getenv("FQDN", "") or BIND_ADDRESS
    HAS_SSL: bool = str_to_bool(os.getenv("HAS_SSL", "False"))
    PROTOCOL: str = "https" if HAS_SSL else "http"
    PORT_SEGMENT: str = "" if NO_PORT else f":{PORT}"
    URL: str = f"{PROTOCOL}://{FQDN}{PORT_SEGMENT}/"

    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

    if not DATABASE_URL:
        logger.critical("DATABASE_URL is required")
        raise ValueError("DATABASE_URL is required")

    MAX_BATCH_FILES: int = int(os.getenv("MAX_BATCH_FILES", "50"))

    BANNED_CHANNELS: Set[int] = str_to_int_set(os.getenv("BANNED_CHANNELS", ""))

    MULTI_CLIENT: bool = False

    FORCE_CHANNEL_ID: Optional[int] = None

    force_channel_env = os.getenv("FORCE_CHANNEL_ID", "-1002442422204").strip()

    if force_channel_env:
        try:
            FORCE_CHANNEL_ID = int(force_channel_env)
        except ValueError:
            logger.warning(f"Invalid FORCE_CHANNEL_ID '{force_channel_env}' in environment; must be an integer.")

    TOKEN_ENABLED: bool = str_to_bool(os.getenv("TOKEN_ENABLED", "False"))
    TOKEN_TTL_HOURS: int = int(os.getenv("TOKEN_TTL_HOURS", "24"))

    SHORTEN_ENABLED: bool = str_to_bool(os.getenv("SHORTEN_ENABLED", "False"))
    SHORTEN_MEDIA_LINKS: bool = str_to_bool(os.getenv("SHORTEN_MEDIA_LINKS", "False"))
    URL_SHORTENER_API_KEY: str = os.getenv("URL_SHORTENER_API_KEY", "")
    URL_SHORTENER_SITE: str = os.getenv("URL_SHORTENER_SITE", "")
