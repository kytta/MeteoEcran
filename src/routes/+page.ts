// © 2023 Nikita Karamov <n.karamov@tu-braunschweig.de>
//
// SPDX-License-Identifier: EUPL-1.2 OR AGPL-3.0-only

import { error } from "@sveltejs/kit";
import type { OpenMeteoResult, GeocodeMapsCoResponse } from "$lib/types";

const GEOCODE_URL = new URL("https://geocode.maps.co/search");
const METEO_URL = new URL("https://api.open-meteo.com/v1/dwd-icon");

/** @type {import('./$types').PageLoad} */
export async function load() {
	const query = "Braunschweig";

	const geocodeSearchParams = new URLSearchParams({
		q: query,
	});

	const geoUrl = GEOCODE_URL;
	geoUrl.search = geocodeSearchParams.toString();

	const geoResponse = await fetch(geoUrl, {
		headers: { "Accept-Language": "de,en;q=0.5" },
	});
	const geoResults = (await geoResponse.json()) as GeocodeMapsCoResponse;

	if (geoResults.length === 0) {
		throw error(404, `No location found for "${query}"`);
	}

	const location = geoResults[0];

	const meteoSearchParams = new URLSearchParams({
		latitude: location.lat,
		longitude: location.lon,
		hourly:
			"temperature_2m,apparent_temperature,precipitation,weathercode,windspeed_10m,winddirection_10m",
		minutely_15: "precipitation",
		daily: "weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset",
		current_weather: "true",
		timezone: "Europe/Berlin",
	});
	const meteoUrl = METEO_URL;
	meteoUrl.search = meteoSearchParams.toString();

	const meteoResponse = await fetch(meteoUrl);
	const weather = (await meteoResponse.json()) as OpenMeteoResult;

	return {
		cityName: query,
		currentWeather: weather.current_weather,
		daily: weather.daily,
	};
}
