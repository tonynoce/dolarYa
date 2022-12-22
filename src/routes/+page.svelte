<script lang="ts">
	import { onMount } from 'svelte';
	import { Spinner, Card, Button } from 'flowbite-svelte';
	import { Input } from 'flowbite-svelte';

	import { USDprice, ARSprice } from '../stores/stores';
	import { getRate } from '../stores/stores';

	/* 	onMount(() => {
		getRate();
	}); */

	let monto = 0;
	let montoCorregido = 0;

	let currency = '';

	function convertARStoUSD() {
		if (monto == 0) {
			0;
		} else if (monto < Number($USDprice)) {
			try {
				montoCorregido = Math.abs(monto / $USDprice);
				montoCorregido = Number(montoCorregido.toFixed(4));
				currency = 'usd$';
				getRate();
			} catch (e) {
				console.log(e);
			}
		} else {
			try {
				montoCorregido = Math.abs(monto / $USDprice);
				montoCorregido = Number(montoCorregido.toFixed(2));
				currency = 'usd$';
				getRate();
			} catch (e) {
				console.log(e);
			}
		}
	}

	function convertUSDtoARS() {
		if (monto == 0) {
			0;
		} else {
			try {
				montoCorregido = Math.abs(monto * ($ARSprice * 1e5));
				montoCorregido = Number(montoCorregido.toFixed(2));
				currency = 'ars$';
				getRate();
			} catch (e) {
				console.log(e);
			}
		}
	}
</script>

<body>
	{#await getRate()}
		<div class="text-center loader">
			<Spinner color="green" size="48" />
		</div>
	{:then}
		<div class="text-2xl text-white text-center font-bold">
			Compra ${($ARSprice * 1e5).toFixed(2)} <br />
			Venta ${$USDprice.toFixed(2)}
		</div>
		<br />
		<p class="text-white font-thin text-center">La cotización del momento, provista por Yadio</p>

		<div class="bigPrice">
			<!-- <Card class="text-center" size="sm" padding="sm">
			</Card> -->
			<div class="text-5xl text-white text-center font-bold montoCorregido">
				<p>{montoCorregido}</p>
				<p class="currency">{currency}</p>
			</div>
			<input type="number" class="inputCard text-center font-bold " min="0" bind:value={monto} />
		</div>
		<div class="buttons">
			<Button
				shadow="blue"
				gradient
				color="alternative"
				size="xl"
				on:click={() => {
					convertARStoUSD();
				}}>Cambiar Argentinos</Button
			>
			<Button
				shadow="green"
				gradient
				color="alternative"
				size="xl"
				on:click={() => {
					convertUSDtoARS();
				}}>Cambiar Dólares</Button
			>
		</div>
	{:catch error}
		<div class="error">
			<h1>Se produjo el siguiente error:</h1>
			<p style="font-size:32pt;color: rgb(240, 46, 170)">{error}</p>
		</div>
	{/await}
</body>

<style>
</style>
