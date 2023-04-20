# © 2023 Nikita Karamov <n.karamov@tu-braunschweig.de>
#
# SPDX-License-Identifier: EUPL-1.2 OR AGPL-3.0-only

import datetime
from enum import IntEnum
from types import MappingProxyType
from typing import NamedTuple
from typing import NewType
from typing import TypedDict

Temperature = NewType("Temperature", float)


class MinMax(NamedTuple):
    minimum: Temperature
    maximum: Temperature


class GeoLocation(NamedTuple):
    latitude: float
    longitude: float


class WeatherConditionCode(IntEnum):
    CLEAR_SKY = 0
    MAINLY_CLEAR = 1
    PARTLY_CLOUDY = 2
    OVERCAST = 3
    FOG = 45
    RIME_FOG = 48
    DRIZZLE_LIGHT = 51
    DRIZZLE_MODERATE = 53
    DRIZZLE_DENSE = 55
    FREEZING_DRIZZLE_LIGHT = 56
    FREEZING_DRIZZLE_DENSE = 57
    RAIN_SLIGHT = 61
    RAIN_MODERATE = 63
    RAIN_HEAVY = 65
    FREEZING_RAIN_LIGHT = 66
    FREEZING_RAIN_HEAVY = 67
    SNOW_FALL_SLIGHT = 71
    SNOW_FALL_MODERATE = 73
    SNOW_FALL_HEAVY = 75
    SNOW_GRAINS = 77
    RAIN_SHOWERS_SLIGHT = 80
    RAIN_SHOWERS_MODERATE = 81
    RAIN_SHOWERS_VIOLENT = 82
    SNOW_SHOWERS_SLIGHT = 85
    SNOW_SHOWERS_HEAVY = 86
    THUNDERSTORM_SLIGHT = 95
    THUNDERSTORM_WITH_HAIL_SLIGHT = 96
    THUNDERSTORM_WITH_HAIL_HEAVY = 99


CODE_CONDITION_MAP = MappingProxyType({
    WeatherConditionCode.CLEAR_SKY: {
        "prefix": "Es ist",
        "condition": "klar",
        "icon": "material-symbols:sunny-outline-rounded",
        "color": "#F9C74F",
    },
    WeatherConditionCode.MAINLY_CLEAR: {
        "prefix": "Es ist",
        "condition": "meist klar",
        "icon": "material-symbols:sunny-outline-rounded",
        "color": "#F9C74F",
    },
    WeatherConditionCode.PARTLY_CLOUDY: {
        "prefix": "Es ist",
        "condition": "teilweise bewölkt",
        "icon": "material-symbols:partly-cloudy-day-outline-rounded",
        "color": "#F9C74F",
    },
    WeatherConditionCode.OVERCAST: {
        "prefix": "Es ist",
        "condition": "bewölkt",
        "icon": "material-symbols:cloud-outline",
        "color": "#A8DADC",
    },
    WeatherConditionCode.FOG: {
        "prefix": "Es ist",
        "condition": "neblig",
        "icon": "material-symbols:foggy-outline",
        "color": "#A8A8A8",
    },
    WeatherConditionCode.RIME_FOG: {
        "prefix": "Es ist",
        "condition": "neblig",
        "icon": "material-symbols:foggy-outline",
        "color": "#A8A8A8",
    },
    WeatherConditionCode.DRIZZLE_LIGHT: {
        "prefix": "Es",
        "condition": "nieselt",
        "icon": "material-symbols:grain",
        "color": "#F8F8FF",
    },
    WeatherConditionCode.DRIZZLE_MODERATE: {
        "prefix": "Es",
        "condition": "nieselt",
        "icon": "material-symbols:grain",
        "color": "#F8F8FF",
    },
    WeatherConditionCode.DRIZZLE_DENSE: {
        "prefix": "Es",
        "condition": "nieselt",
        "icon": "material-symbols:grain",
        "color": "#F8F8FF",
    },
    WeatherConditionCode.FREEZING_DRIZZLE_LIGHT: {
        "prefix": "Es",
        "condition": "nieselt",
        "icon": "material-symbols:grain",
        "color": "#F8F8FF",
    },
    WeatherConditionCode.FREEZING_DRIZZLE_DENSE: {
        "prefix": "Es",
        "condition": "nieselt",
        "icon": "material-symbols:grain",
        "color": "#F8F8FF",
    },
    WeatherConditionCode.RAIN_SLIGHT: {
        "prefix": "Es",
        "condition": "regnet",
        "icon": "material-symbols:water-drop-outline-rounded",
        "color": "#ADD8E6",
    },
    WeatherConditionCode.RAIN_MODERATE: {
        "prefix": "Es",
        "condition": "regnet",
        "icon": "material-symbols:water-drop-outline-rounded",
        "color": "#ADD8E6",
    },
    WeatherConditionCode.RAIN_HEAVY: {
        "prefix": "Es",
        "condition": "regnet",
        "icon": "material-symbols:water-drop-outline-rounded",
        "color": "#ADD8E6",
    },
    WeatherConditionCode.FREEZING_RAIN_LIGHT: {
        "prefix": "Es",
        "condition": "regnet",
        "icon": "material-symbols:water-drop-outline-rounded",
        "color": "#ADD8E6",
    },
    WeatherConditionCode.FREEZING_RAIN_HEAVY: {
        "prefix": "Es",
        "condition": "regnet",
        "icon": "material-symbols:water-drop-outline-rounded",
        "color": "#ADD8E6",
    },
    WeatherConditionCode.SNOW_FALL_SLIGHT: {
        "prefix": "Es",
        "condition": "schneit",
        "icon": "material-symbols:snowing",
        "color": "#F8F8FF",
    },
    WeatherConditionCode.SNOW_FALL_MODERATE: {
        "prefix": "Es",
        "condition": "schneit",
        "icon": "material-symbols:snowing",
        "color": "#F8F8FF",
    },
    WeatherConditionCode.SNOW_FALL_HEAVY: {
        "prefix": "Es",
        "condition": "schneit",
        "icon": "material-symbols:snowing",
        "color": "#F8F8FF",
    },
    WeatherConditionCode.SNOW_GRAINS: {
        "prefix": "Es",
        "condition": "schneit",
        "icon": "material-symbols:snowing",
        "color": "#F8F8FF",
    },
    WeatherConditionCode.RAIN_SHOWERS_SLIGHT: {
        "prefix": "Es",
        "condition": "schauert",
        "icon": "material-symbols:rainy-outline",
        "color": "#6495ED",
    },
    WeatherConditionCode.RAIN_SHOWERS_MODERATE: {
        "prefix": "Es",
        "condition": "schauert",
        "icon": "material-symbols:rainy-outline",
        "color": "#6495ED",
    },
    WeatherConditionCode.RAIN_SHOWERS_VIOLENT: {
        "prefix": "Es",
        "condition": "schauert",
        "icon": "material-symbols:rainy-outline",
        "color": "#6495ED",
    },
    WeatherConditionCode.SNOW_SHOWERS_SLIGHT: {
        "prefix": "Es ist",
        "condition": "Schneeschauer",
        "icon": "material-symbols:snowing",
        "color": "#F8F8FF",
    },
    WeatherConditionCode.SNOW_SHOWERS_HEAVY: {
        "prefix": "Es ist",
        "condition": "Schneeschauer",
        "icon": "material-symbols:snowing",
        "color": "#F8F8FF",
    },
    WeatherConditionCode.THUNDERSTORM_SLIGHT: {
        "prefix": "Es ist",
        "condition": "Gewitter",
        "icon": "material-symbols:bolt-outline-rounded",
        "color": "#FFD700",
    },
    WeatherConditionCode.THUNDERSTORM_WITH_HAIL_SLIGHT: {
        "prefix": "Es ist",
        "condition": "Gewitter und Hagel",
        "icon": "material-symbols:weather-hail-outline-rounded",
        "color": "#FFD700",
    },
    WeatherConditionCode.THUNDERSTORM_WITH_HAIL_HEAVY: {
        "prefix": "Es ist",
        "condition": "Gewitter und Hagel",
        "icon": "material-symbols:weather-hail-outline-rounded",
        "color": "#FFD700",
    },
})


class WeatherCondition(TypedDict):
    code: WeatherConditionCode
    prefix: str
    condition: str
    color: str
    icon: str


def get_condition_from_code(code: WeatherConditionCode):
    kwargs = {
        "prefix": "Das Wetter ist",
        "condition": "unbekannt",
        "icon": "material-symbols:question-mark-rounded",
        "color": "#ccc",
    }

    if code in CODE_CONDITION_MAP:
        kwargs = CODE_CONDITION_MAP[code]

    return WeatherCondition(
        code=code,
        **kwargs,
    )


class WeatherState(TypedDict):
    condition: WeatherCondition
    temperature: Temperature


class Forecast(TypedDict):
    date: datetime.date
    condition: WeatherCondition
    temperature: MinMax
