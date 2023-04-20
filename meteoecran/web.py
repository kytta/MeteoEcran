# © 2023 Nikita Karamov <n.karamov@tu-braunschweig.de>
#
# SPDX-License-Identifier: EUPL-1.2 OR AGPL-3.0-only

from pathlib import Path
from typing import Optional

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.responses import RedirectResponse
from starlette.routing import Mount
from starlette.routing import Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from meteoecran import api

SOURCE_DIR = Path(__file__).parent

templates = Jinja2Templates(directory=SOURCE_DIR / "templates")


async def homepage(request):
    return templates.TemplateResponse("index.html.jinja", {
        "request": request,
        "title": "MeteoEcran",
        "lang": "en",
    })


async def search(request):
    query: Optional[str] = request.query_params.get("q", None)

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


async def geo(request):
    lat: Optional[str] = request.query_params.get("lat", None)
    lon: Optional[str] = request.query_params.get("lon", None)

    if not (lat and lon):
        return JSONResponse(
            {
                "error": "Please provide both 'lat' and 'lon'",
            },
            status_code=400,
        )

    weather = api.get_weather_for_location(
        api.GeoLocation(float(lat), float(lon)))

    is_htmx = "HX-Request" in request.headers

    return templates.TemplateResponse(
        "partial_weather.html.jinja" if is_htmx else "weather.html.jinja",
        {
            "request": request,
            "title": "MeteoEcran",
            "lang": "en",
            "city": weather["city"],
            "weather": {
                "current": weather["current"],
            },
            "weather_data": {
                "tomorrow": {
                    "min_t": round(weather["daily"]["temperature_2m_min"][1]),
                    "max_t": round(weather["daily"]["temperature_2m_max"][1]),
                },
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

app = Starlette(debug=False, routes=routes)
