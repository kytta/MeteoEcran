<!--
© 2023 Nikita Karamov <n.karamov@tu-braunschweig.de>

SPDX-License-Identifier: EUPL-1.2 OR AGPL-3.0-only
-->

<script lang="ts">
	import { getDataFromCode } from "$lib/weather-code";
	import Icon from "@iconify/svelte";

	export let data;

	$: currentCondition = getDataFromCode(data.currentWeather.weathercode);
	$: conditionTomorrow = getDataFromCode(data.daily.weathercode[1]);
</script>

<div class="title">
	{currentCondition.prefix}
	<span class="condition" style:background-color={currentCondition.color}>
		<Icon inline icon={currentCondition.icon} width="10vh" height="10vh" />
		{currentCondition.condition}
	</span>
</div>
<section class="now">
	<div class="temperature">
		{Math.round(data.currentWeather.temperature)} &#x2103;
	</div>
</section>
<section class="tomorrow">
	<div class="title">
		<strong>Morgen:</strong>
		<Icon inline icon={conditionTomorrow.icon} width="10vh" height="10vh" />
		{Math.round(data.daily.temperature_2m_min[1])}...{Math.round(
			data.daily.temperature_2m_max[1],
		)}
		&#x2103;
	</div>
</section>

<style>
	.title {
		font-size: 10vh;
	}

	.condition {
		font-weight: bolder;
		padding: 0 0.25em;
	}

	.now {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: flex-start;
		gap: 16px;
		margin-bottom: 20vh;
	}

	.tomorrow {
		border-top: 1px solid #888;
		padding-top: 16px;
	}

	.temperature {
		font-size: 30vh;
		font-weight: 300;
	}
</style>
