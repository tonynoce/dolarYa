<script lang="ts">
	import { onMount } from 'svelte';

	import { browser } from '$app/env';
	import { Spinner, Card, Button } from 'flowbite-svelte';
	import { Input } from 'flowbite-svelte';

	import Swap from '$lib/components/Swap.svelte';

	import { USDprice, ARSprice } from '../stores/stores';
	import { getRate, dataARS, dataUSD } from '../stores/stores';

	let offline = false;
	let lastUpdated: any;
	let theDate: Date;

	$: offline;

	onMount(async () => {
		await getRate();
		localStorage.setItem('USDprice', dataARS);
		localStorage.setItem('ARSprice', dataUSD);
		localStorage.setItem('Date', String(Date.now()));
	});

	function offlineModeOn() {
		offline = true;

		$USDprice = Number(localStorage.getItem('ARSprice'));
		$ARSprice = Number(localStorage.getItem('USDprice'));
		lastUpdated = localStorage.getItem('Date');
		theDate = new Date(Number(lastUpdated));
	}

	if (browser) {
		addEventListener('deviceorientation', (event) => {
			/* console.log('I moved !'); */
		});
		addEventListener('online', () => {
			/* console.log('Onlineeee'); */
			offline = false;
		});
		addEventListener('offline', () => {
			/* console.log('offlineeeee'); */
			offlineModeOn();
		});

		/* 		if (navigator.onLine) {
			console.log('online');
		} else {
			console.log('offline');
			offline = true;
		} */
	}
</script>

<svelte:head>
	<title>DolarYa => ${($ARSprice * 1e5).toFixed(2)} -- ${$USDprice.toFixed(2)}</title>
	<link rel="manifest" href="/manifest.json" />
	<meta
		name="description"
		content="Convertidor de divisas entre pesos argentinos y dolares estadounidenses"
	/>
</svelte:head>

<main>
	{#await getRate()}
		<div class="loader">
			<Spinner color="green" size="48" />
		</div>
	{:then}
		<Swap {offline} {theDate} />
	{:catch error}
		{#key offline}
			{#if offline == true}
				<div class="text-center text-white text-center font-bold">
					<h1 class="text-2xl">Modo Offline activado:</h1>
					<!-- 
					<p>Último precio de la cotización del día:</p>
					<div>{theDate.toUTCString()}</div>
				-->
				</div>
				<Swap {offline} {theDate} />
			{:else}
				<div class="loader text-center">
					<h1 class="text-2xl">No se detectó una conexión</h1>
					<p>Activar el modo offline ?</p>
					<br />
					<div class="margin-top: 24pt;">
						<Button
							shadow="green"
							gradient
							color="alternative"
							size="xl"
							on:click={() => {
								offlineModeOn();
							}}>Modo Offline</Button
						>
					</div>
					<!-- 

						<div class="error">
							<h1>Se produjo el siguiente error:</h1>
							<p style="font-size:32pt;color: rgb(240, 46, 170)">{error}</p>
						</div>
					-->
					<!-- Offline Div -->
				</div>
			{/if}
		{/key}
	{/await}
	<!-- 
		<div class="favoritos">
			<a
			href="#"
			on:click={() => {
				addToFavorites();
			}}>Add to Favorites</a
			>
		</div>
	-->
</main>
