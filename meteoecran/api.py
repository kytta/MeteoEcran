# © 2023 Nikita Karamov <n.karamov@tu-braunschweig.de>
#
# SPDX-License-Identifier: EUPL-1.2 OR AGPL-3.0-only

import datetime
from typing import TYPE_CHECKING
from typing import NotRequired
from typing import TypedDict

import httpx

from meteoecran.types import Forecast
from meteoecran.types import GeoLocation
from meteoecran.types import MinMax
from meteoecran.types import Temperature
from meteoecran.types import WeatherConditionCode
from meteoecran.types import WeatherState
from meteoecran.types import get_condition_from_code

if TYPE_CHECKING:
    from collections.abc import Sequence

GEOCODE_URL = "https://geocode.maps.co"
METEO_URL = "https://api.open-meteo.com/v1/dwd-icon"

METEO_PARAMS = {
    "hourly": ",".join((
        "temperature_2m",
        "apparent_temperature",
        "precipitation",
        "weathercode",
        "windspeed_10m",
        "winddirection_10m",
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


class GeoReverseAddress(TypedDict):
    village: NotRequired[str]
    town: NotRequired[str]
    city: NotRequired[str]


class GeoReverseResultPartial(TypedDict):
    address: GeoReverseAddress
    display_name: str


def get_name_for_location(location: GeoLocation) -> str:
    with httpx.Client(base_url=GEOCODE_URL) as client:
        r = client.get(
            "/reverse",
            params={
                "lat": location.latitude,
                "lon": location.longitude,
            },
        )

    r_json: GeoReverseResultPartial = r.json()
    address = r_json["address"]

    if "village" in address:
        return address["village"]

    if "town" in address:
        return address["town"]

    if "city" in address:
        return address["city"]

    return r_json["display_name"]


class GeocodeResultPartial(TypedDict):
    lat: float
    lon: float


def get_geolocation_for_query(query: str) -> GeoLocation | None:
    with httpx.Client(base_url=GEOCODE_URL) as client:
        r = client.get(
            "/search",
            params={
                "q": query,
            },
        )

    results: Sequence[GeocodeResultPartial] = r.json()

    if len(results) == 0:
        return None

    return GeoLocation(results[0]["lat"], results[0]["lon"])


def convert_daily_to_forecast(daily_json) -> list[Forecast]:  # type: ignore
    result = []

    zipped = zip(
        daily_json["time"],
        daily_json["weathercode"],
        daily_json["temperature_2m_max"],
        daily_json["temperature_2m_min"],
        strict=False,
    )

    for date, code, t_max, t_min in zipped:
        result.append(Forecast(
            date=datetime.date.fromisoformat(date),
            condition=get_condition_from_code(code),
            temperature=MinMax(
                t_min,
                t_max,
            ),
        ))

    return result


class Weather(TypedDict):
    current: WeatherState
    daily: list[Forecast]


def get_weather_for_location(location: GeoLocation) -> Weather:
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
        condition=get_condition_from_code(
            WeatherConditionCode(result["current_weather"]["weathercode"]),
        ),
        temperature=Temperature(result["current_weather"]["temperature"]),
    )

    return {
        "current": current,
        "daily": convert_daily_to_forecast(result["daily"]),
    }
