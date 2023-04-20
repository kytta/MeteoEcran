# © 2023 Nikita Karamov <n.karamov@tu-braunschweig.de>
#
# SPDX-License-Identifier: EUPL-1.2 OR AGPL-3.0-only

from uvicorn.workers import UvicornWorker

from meteoecran.web import app
from meteoecran.web import config


class MeteoEcranWorker(UvicornWorker):
    CONFIG_KWARGS = config.uvicorn_kwargs


__all__ = [
    "app",
    "MeteoEcranWorker",
]
