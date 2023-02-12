"""Constants of the Xiaomi/Viomi Washing Machine component."""
from datetime import timedelta
from dataclasses import dataclass

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass
)

from homeassistant.const import (
    TIME_MINUTES
)

DEFAULT_NAME = "Xiaomi/Viomi Washing Machine"
DOMAIN = "viomi_washer"
DOMAINS = ["fan", "sensor"]
DATA_KEY = "viomi_washer_data"
DATA_STATE = "state"
DATA_DEVICE = "device"

CONF_MODEL = "model"
CONF_MAC = "mac"

MODEL_VIOMI_WASH_V5 = "viomi.washer.v5"

OPT_MODEL = {
    MODEL_VIOMI_WASH_V5: "Viomi Washer V5"
}

MODELS_MIIO = [
    MODEL_VIOMI_WASH_V5
]

MODELS_ALL_DEVICES = MODELS_MIIO

DEFAULT_SCAN_INTERVAL = 60
SCAN_INTERVAL = timedelta(seconds=DEFAULT_SCAN_INTERVAL)

WASHER_PROPS = [
    "program",
    "wash_process",
    "wash_status",
    # "water_temp",
    # "rinse_status",
    # "spin_level",
    "remain_time",
    "appoint_time",
    # "be_status",
    # "run_status",
    "DryMode",
    # "child_lock",
]

WASHER_PROGS = {
    'goldenwash': '黄金洗',
    'quick': '快洗',
    'super_quick': '超快洗',

    'antibacterial': '除菌洗',
    'refresh': '空氣洗',

    'dry': '黄金烘',
    'weak_dry': '低溫烘',

    'rinse_spin': '漂+脱',
    'spin': '單脱水',
    'drumclean': '筒清潔',

    'cottons': '棉織物',
    'down': '羽绒服',
    'wool': '羊毛',
    'shirt': '襯衫',
    'jeans': '牛仔',
    'underwears': '内衣',
}

@dataclass
class ViomiWasherSensorDescription(
    SensorEntityDescription
):
    """Class to describe an Xiaomi/Viomi Washing Machine sensor."""


WASHER_SENSORS: tuple[ViomiWasherSensorDescription, ...] = (
    ViomiWasherSensorDescription(
        key="wash_status",
        name="Status",
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:chip"
    ),
    ViomiWasherSensorDescription(
        key="remain_time",
        name="Remain time",
        native_unit_of_measurement=TIME_MINUTES,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:timelapse"
    )
)
