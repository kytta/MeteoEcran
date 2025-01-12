# © 2023 Nikita Karamov <n.karamov@tu-braunschweig.de>
#
# SPDX-License-Identifier: EUPL-1.2 OR AGPL-3.0-only

from uvicorn.workers import UvicornWorker

from meteoecran.config import uvicorn_kwargs
from meteoecran.web import app


class MeteoEcranWorker(UvicornWorker):
    CONFIG_KWARGS = uvicorn_kwargs


__all__ = [
    "MeteoEcranWorker",
    "app",
]
