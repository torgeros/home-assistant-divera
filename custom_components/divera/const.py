"""Constants for the Divera integration."""
from datetime import timedelta
from typing import Final

DOMAIN = "divera"

DEFAULT_NAME = "Divera 24/7"
DEFAULT_SHORT_NAME = "Divera"

ATTR_NAME = "state"
ATTR_LATEST_UPDATE = "latest_update_utc"
DIVERA_STATE_SERVICE: Final = "set_state"
DIVERA_DATA = "divera_data"
DIVERA_COORDINATOR = "divera_coordinator"
DIVERA_NAME = "divera_name"

DEFAULT_TIMEOUT = 2
DIVERA_URL = "https://www.divera247.com/api/v2/pull/all"
DIVERA_STATUS_URL = "https://www.divera247.com/api/v2/statusgeber/set-status"

VEHICLE_ICON = "mdi:fire-truck"
VEHICLE_ENABLED_DEFAULT = True

DEFAULT_SCAN_INTERVAL = timedelta(minutes=1)
