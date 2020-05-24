from homeassistant.helpers.entity import ToggleEntity

ATTR_BRIGHTNESS: str
ATTR_COLOR_TEMP: str
ATTR_HS_COLOR: str
ATTR_TRANSITION: str
SUPPORT_BRIGHTNESS: int
SUPPORT_COLOR: int
SUPPORT_COLOR_TEMP: int

class LightEntity(ToggleEntity): ...
