// © 2023 Nikita Karamov <n.karamov@tu-braunschweig.de>
//
// SPDX-License-Identifier: EUPL-1.2 OR AGPL-3.0-only

export enum WMOWeatherCode {
	CLEAR_SKY = 0,
	MAINLY_CLEAR = 1,
	PARTLY_CLOUDY = 2,
	OVERCAST = 3,
	FOG = 45,
	RIME_FOG = 48,
	DRIZZLE_LIGHT = 51,
	DRIZZLE_MODERATE = 53,
	DRIZZLE_DENSE = 55,
	FREEZING_DRIZZLE_LIGHT = 56,
	FREEZING_DRIZZLE_DENSE = 57,
	RAIN_SLIGHT = 61,
	RAIN_MODERATE = 63,
	RAIN_HEAVY = 65,
	FREEZING_RAIN_LIGHT = 66,
	FREEZING_RAIN_HEAVY = 67,
	SNOW_FALL_SLIGHT = 71,
	SNOW_FALL_MODERATE = 73,
	SNOW_FALL_HEAVY = 75,
	SNOW_GRAINS = 77,
	RAIN_SHOWERS_SLIGHT = 80,
	RAIN_SHOWERS_MODERATE = 81,
	RAIN_SHOWERS_VIOLENT = 82,
	SNOW_SHOWERS_SLIGHT = 85,
	SNOW_SHOWERS_HEAVY = 86,
	THUNDERSTORM_SLIGHT = 95,
	THUNDERSTORM_WITH_HAIL_SLIGHT = 96,
	THUNDERSTORM_WITH_HAIL_HEAVY = 99,
}

interface GeocodeMapsCoResult {
	place_id: number;
	licence: string;
	powered_by: string;
	osm_type: string;
	osm_id: number;
	boundingbox: [string, string, string, string];
	lat: string;
	lon: string;
	display_name: string;
	class: string;
	type: string;
	importance: number;
}

export type GeocodeMapsCoResponse = Array<GeocodeMapsCoResult>;

export interface OpenMeteoResult {
	latitude: number;
	longitude: number;
	generationtime_ms: number;
	utc_offset_seconds: number;
	timezone: string;
	timezone_abbreviation: string;
	elevation: number;

	current_weather: {
		temperature: number;
		windspeed: number;
		winddirection: number;
		weathercode: WMOWeatherCode;
		time: string;
	};

	minutely_15_units: {
		time: string;
		precipitation: string;
	};
	minutely_15: {
		time: string[];
		precipitation: number[];
	};

	hourly_units: {
		time: string;
		temperature_2m: string;
		apparent_temperature: string;
		precipitation: string;
		weathercode: string;
		windspeed_10m: string;
		winddirection_10m: string;
	};
	hourly: {
		time: string[];
		temperature_2m: number[];
		apparent_temperature: number[];
		precipitation: number[];
		weathercode: WMOWeatherCode[];
		windspeed_10m: number[];
		winddirection_10m: number[];
	};

	daily_units: {
		time: string;
		weathercode: string;
		temperature_2m_max: string;
		temperature_2m_min: string;
		sunrise: string;
		sunset: string;
	};
	daily: {
		time: Date[];
		weathercode: WMOWeatherCode[];
		temperature_2m_max: number[];
		temperature_2m_min: number[];
		sunrise: string[];
		sunset: string[];
	};
}
