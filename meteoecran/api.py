# © 2023 Nikita Karamov <n.karamov@tu-braunschweig.de>
#
# SPDX-License-Identifier: EUPL-1.2 OR AGPL-3.0-only

from typing import NamedTuple
from typing import Optional

import httpx

from meteoecran.types import Temperature
from meteoecran.types import WeatherCondition
from meteoecran.types import WeatherConditionCode
from meteoecran.types import WeatherState

GEOCODE_URL = "https://geocode.maps.co"
METEO_URL = "https://api.open-meteo.com/v1/dwd-icon"

METEO_PARAMS = {
    "hourly": ",".join((
        "temperature_2m",
        "apparent_temperature",
        "precipitation",
        "weathercode",
        "windspeed_10m",
        "winddirection_10",
    )),
    "minutely_15": "precipitation",
    "daily": ",".join((
        "weathercode",
        "temperature_2m_max",
        "temperature_2m_min",
        "sunrise",
        "sunset",
    )),
    "current_weather": "true",
    "timezone": "Europe/Berlin",
}


class GeoLocation(NamedTuple):
    latitude: float
    longitude: float


def get_geolocation_for_query(query: str) -> Optional[GeoLocation]:
    with httpx.Client(base_url=GEOCODE_URL) as client:
        r = client.get(
            "/search",
            params={
                "q": query,
            },
        )

    results: list = r.json()

    if len(results) == 0:
        return None

    return GeoLocation(results[0]["lat"], results[0]["lon"])


def get_weather_for_location(location: GeoLocation):
    with httpx.Client(base_url=METEO_URL) as client:
        r = client.get(
            "",
            params={
                **METEO_PARAMS,
                "latitude": location.latitude,
                "longitude": location.longitude,
            },
        )

    result = r.json()

    current = WeatherState(
        condition=WeatherCondition.from_code(
            WeatherConditionCode(result["current_weather"]["weathercode"]),
        ),
        temperature=Temperature(result["current_weather"]["temperature"]),
    )

    return {
        "city": "Blah-blah",
        "current": current,
        "current_weather": result["current_weather"],
        "daily": result["daily"],
    }
