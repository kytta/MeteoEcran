// © 2023 Nikita Karamov <n.karamov@tu-braunschweig.de>
//
// SPDX-License-Identifier: EUPL-1.2 OR AGPL-3.0-only

import { WMOWeatherCode } from "$lib/types";

export type ConditionsWithIcon = {
	prefix: string;
	condition: string;
	icon: string;
	color: string;
};

export const getDataFromCode = (code: WMOWeatherCode): ConditionsWithIcon => {
	if (code === WMOWeatherCode.CLEAR_SKY) {
		return {
			prefix: "Es ist",
			condition: "klar",
			icon: "material-symbols:sunny-outline-rounded",
			color: "#F9C74F",
		};
	}

	if (code === WMOWeatherCode.MAINLY_CLEAR) {
		return {
			prefix: "Es ist",
			condition: "meist klar",
			icon: "material-symbols:sunny-outline-rounded",
			color: "#F9C74F",
		};
	}

	if (code === WMOWeatherCode.PARTLY_CLOUDY) {
		return {
			prefix: "Es ist",
			condition: "teilweise bewölkt",
			icon: "material-symbols:partly-cloudy-day-outline-rounded",
			color: "#F9C74F",
		};
	}

	if (code === WMOWeatherCode.OVERCAST) {
		return {
			prefix: "Es ist",
			condition: "bewölkt",
			icon: "material-symbols:cloud-outline",
			color: "#A8DADC",
		};
	}

	if (code === WMOWeatherCode.FOG || code === WMOWeatherCode.RIME_FOG) {
		return {
			prefix: "Es ist",
			condition: "neblig",
			icon: "material-symbols:foggy-outline",
			color: "#A8A8A8",
		};
	}

	if (
		code === WMOWeatherCode.DRIZZLE_LIGHT ||
		code === WMOWeatherCode.DRIZZLE_MODERATE ||
		code === WMOWeatherCode.DRIZZLE_DENSE ||
		code === WMOWeatherCode.FREEZING_DRIZZLE_LIGHT ||
		code === WMOWeatherCode.FREEZING_DRIZZLE_DENSE
	) {
		return {
			prefix: "Es",
			condition: "nieselt",
			icon: "material-symbols:grain",
			color: "#F8F8FF",
		};
	}

	if (
		code === WMOWeatherCode.RAIN_SLIGHT ||
		code === WMOWeatherCode.RAIN_MODERATE ||
		code === WMOWeatherCode.RAIN_HEAVY ||
		code === WMOWeatherCode.FREEZING_RAIN_LIGHT ||
		code === WMOWeatherCode.FREEZING_RAIN_HEAVY
	) {
		return {
			prefix: "Es",
			condition: "regnet",
			icon: "material-symbols:water-drop-outline-rounded",
			color: "#ADD8E6",
		};
	}

	if (
		code === WMOWeatherCode.SNOW_FALL_SLIGHT ||
		code === WMOWeatherCode.SNOW_FALL_MODERATE ||
		code === WMOWeatherCode.SNOW_FALL_HEAVY ||
		code === WMOWeatherCode.SNOW_GRAINS
	) {
		return {
			prefix: "Es",
			condition: "schneit",
			icon: "material-symbols:snowing",
			color: "#F8F8FF",
		};
	}

	if (
		code === WMOWeatherCode.RAIN_SHOWERS_SLIGHT ||
		code === WMOWeatherCode.RAIN_SHOWERS_MODERATE ||
		code === WMOWeatherCode.RAIN_SHOWERS_VIOLENT
	) {
		return {
			prefix: "Es",
			condition: "schauert",
			icon: "material-symbols:rainy-outline",
			color: "#6495ED",
		};
	}

	if (
		code === WMOWeatherCode.SNOW_SHOWERS_SLIGHT ||
		code === WMOWeatherCode.SNOW_SHOWERS_HEAVY
	) {
		return {
			prefix: "Es ist",
			condition: "Schneeschauer",
			icon: "material-symbols:snowing",
			color: "#F8F8FF",
		};
	}

	if (code === WMOWeatherCode.THUNDERSTORM_SLIGHT) {
		return {
			prefix: "Es ist",
			condition: "Gewitter",
			icon: "material-symbols:bolt-outline-rounded",
			color: "#FFD700",
		};
	}

	if (
		code === WMOWeatherCode.THUNDERSTORM_WITH_HAIL_SLIGHT ||
		code === WMOWeatherCode.THUNDERSTORM_WITH_HAIL_HEAVY
	) {
		return {
			prefix: "Es ist",
			condition: "Gewitter und Hagel",
			icon: "material-symbols:weather-hail-outline-rounded",
			color: "#FFD700",
		};
	}

	return {
		prefix: "Das Wetter ist",
		condition: "unbekannt",
		icon: "material-symbols:question-mark-rounded",
		color: "#ccc",
	};
};
