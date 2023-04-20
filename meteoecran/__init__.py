# © 2023 Nikita Karamov <n.karamov@tu-braunschweig.de>
#
# SPDX-License-Identifier: EUPL-1.2 OR AGPL-3.0-only

import locale

from meteoecran.web import app

# TODO: set via settings
locale.setlocale(locale.LC_ALL, "de_DE")

__all__ = [
    "app",
]
