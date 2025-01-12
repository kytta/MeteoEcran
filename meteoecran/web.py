# © 2023 Nikita Karamov <n.karamov@tu-braunschweig.de>
#
# SPDX-License-Identifier: EUPL-1.2 OR AGPL-3.0-only

import datetime
from pathlib import Path

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.responses import RedirectResponse
from starlette.responses import Response
from starlette.routing import Mount
from starlette.routing import Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from meteoecran import api
from meteoecran import config
from meteoecran.types import GeoLocation

ONE_DAY = datetime.timedelta(days=1)

SOURCE_DIR = Path(__file__).parent

templates = Jinja2Templates(directory=SOURCE_DIR / "templates")


async def homepage(request: Request) -> Response:
    return templates.TemplateResponse("index.html.jinja", {
        "request": request,
        "title": "MeteoEcran",
        "lang": "en",
    })


async def search(request: Request) -> Response:
    query: str | None = request.query_params.get("q", None)

    if not query:
        return JSONResponse(
            {
                "error": "Please provide search request in the 'q' parameter",
            },
            status_code=400,
        )

    location = api.get_geolocation_for_query(query)

    if location is None:
        return JSONResponse(
            {
                "error": f"Location for {query!r} not found",
            },
            status_code=404,
        )

    url = request.url_for("geo").include_query_params(
        lat=location.latitude,
        lon=location.longitude,
    )

    return RedirectResponse(url)


async def geo(request: Request) -> Response:
    lat: str | None = request.query_params.get("lat", None)
    lon: str | None = request.query_params.get("lon", None)

    if not (lat and lon):
        return JSONResponse(
            {
                "error": "Please provide both 'lat' and 'lon'",
            },
            status_code=400,
        )

    location = GeoLocation(float(lat), float(lon))

    weather = api.get_weather_for_location(location)
    name = api.get_name_for_location(location)

    is_htmx = "HX-Request" in request.headers

    now = datetime.datetime.now(tz=config.TIMEZONE)

    return templates.TemplateResponse(
        "partial_weather.html.jinja" if is_htmx else "weather.html.jinja",
        {
            "request": request,
            "title": f"Weather in {name}",
            "lang": "en",
            "location_name": name,
            "now": {
                "weekday": now.strftime("%A"),
                "time": now.strftime("%H:%M"),
                "date": now.strftime("%x"),
            },
            "weather": {
                "current": weather["current"],
                "tomorrow": weather["daily"][1],
            },
        },
    )


static_files = StaticFiles(directory=SOURCE_DIR / "static")

routes = [
    Route("/", homepage),
    Route("/search", search),
    Route("/geo", geo, name="geo"),
    Mount("/static", app=static_files, name="static"),
]

app = Starlette(debug=config.DEBUG, routes=routes)
