# © 2023 Nikita Karamov <n.karamov@tu-braunschweig.de>
#
# SPDX-License-Identifier: EUPL-1.2 OR AGPL-3.0-only

import uvicorn

from meteoecran import config

if __name__ == "__main__":
    uvicorn.run("meteoecran:app", **config.uvicorn_kwargs)
