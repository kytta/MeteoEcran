<!--
© 2023 Nikita Karamov <n.karamov@tu-braunschweig.de>
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# MeteoÉcran

> Current weather and forecast for digital signage

## Deploy

1. Clone the project

2. **(recommended)** Create a virtualenv for the project

   ```sh
   virtualenv --python python3.9 --no-download --no-periodic-update venv
   ```

3. Install dependencies

   ```sh
   . venv/bin/activate
   pip install -r requirements.txt
   ```

4. Define settings as environment variables and/or inside the `.env` file

5. You can now run the app. For production, it's recommended you use Gunicorn:

   ```sh
   gunicorn \
          --workers 2 \  # Gunicorn recommends 2-4 workers per core
          --worker-class meteoecran.MeteoEcranWorker \
          --bind unix:/run/gunicorn.sock \  # you can also bind to a port
          meteoecran:app
   ```

   Inside [`contrib/`](./contrib/) you can find example files, like systemd
   services, Nginx configs, etc.

## Licence

© 2023 [Nikita Karamov]\
Dual-licensed under the [European Union Public License 1.2][EUPL-1.2] and
[GNU Affero General Public License v3.0 only][AGPL-3.0-only].\
Config files and examples are licensed under the
[BSD 2-Clause "Simplified" License][BSD-2-Clause].\
Documentation is licensed under the
[Creative Commons Attribution Share Alike 4.0 International][CC-BY-SA-4.0].

---

This project is hosted on GitHub:
<https://github.com/kytta/MeteoEcran.git>

[agpl-3.0-only]: https://spdx.org/licenses/AGPL-3.0-only.html
[BSD-2-Clause]: https://spdx.org/licenses/BSD-2-Clause.html
[CC-BY-SA-4.0]: https://spdx.org/licenses/CC-BY-SA-4.0.html
[eupl-1.2]: https://spdx.org/licenses/EUPL-1.2.html
[nikita karamov]: https://www.kytta.dev/
