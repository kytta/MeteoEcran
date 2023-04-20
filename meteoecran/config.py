# © 2023 Nikita Karamov <n.karamov@tu-braunschweig.de>
#
# SPDX-License-Identifier: EUPL-1.2 OR AGPL-3.0-only

import locale
from zoneinfo import ZoneInfo

from starlette.config import Config

config = Config(".env", env_prefix="METEOECRAN_")

DEBUG = config("DEBUG", cast=bool, default=False)
TIMEZONE = config("TIMEZONE", cast=ZoneInfo, default="UTC")
LOCALE = config("LOCALE", default=False)

if LOCALE:
    locale.setlocale(locale.LC_ALL, LOCALE)

uvicorn_kwargs = {
    "log_level": "trace" if DEBUG else "info",
    "reload": DEBUG,
}
