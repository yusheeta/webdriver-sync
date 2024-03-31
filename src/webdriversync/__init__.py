from .base import WebdriverSyncBase
from .chrome import ChromeDriverManager

AVAILABLE_DRIVERS = {
    "chrome": ChromeDriverManager
}

__all__ = {
  "WebdriverManagerBase"
}