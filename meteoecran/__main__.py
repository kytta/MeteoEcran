# © 2023 Nikita Karamov <n.karamov@tu-braunschweig.de>
#
# SPDX-License-Identifier: EUPL-1.2 OR AGPL-3.0-only

import uvicorn

from meteoecran.config import uvicorn_kwargs

if __name__ == "__main__":
    uvicorn.run("meteoecran:app", **uvicorn_kwargs)  # type: ignore
