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
		<br />
		<div class="bigPrice">
			<!-- <Card class="text-center" size="sm" padding="sm">
			</Card> -->
			<div class="text-5xl text-white text-center font-bold montoCorregido">
				<p>{montoCorregido}</p>
				<p class="currency">{currency}</p>
			</div>
			<br />
			<!-- 			<Card class="text-center" size="xl" padding="md">
			</Card> -->
			<!-- 			<Input type="number" size="1" class="inputCard text-center" min="0" bind:value={monto} />
 -->
			<input type="number" class="inputCard text-center font-bold " min="0" bind:value={monto} />

			<!-- 			<Card class="text-center" size="md" padding="lg">
			</Card> -->
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
	body {
		background-color: rgb(27, 33, 39);
		align-self: center;
		justify-self: center;
		color: white;
		padding-top: 25px;
	}
	.loader {
		padding-top: 50%;
		box-shadow: 5cm;
	}
	.bigPrice {
		color: rgb(240, 46, 170);
		display: grid;
		padding: 15px 20px;
		grid-template-columns: repeat(1, 1fr);
		grid-gap: 15px;
		justify-items: center;
		margin: 120px 0px 80px 0px;
	}
	.currency {
		font-size: 24pt;
		color: rgb(240, 46, 170);
	}
	.inputCard {
		text-align: center;
		font-weight: bold;
		font-size: 14pt;
		color: rgb(240, 46, 170);
		box-shadow: rgb(240, 46, 170) 0px 25px 20px -20px, rgba(240, 46, 170, 1) 0px -15px 20px -20px;
	}
	.buttons {
		padding: 25px 25px;
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		grid-gap: 10px;
		grid-auto-rows: minmax(75px, auto);
		box-shadow: rgba(240, 46, 170, 0.45) 0px 25px 75px -23px;
	}
	.montoCorregido {
		box-shadow: rgba(255, 0, 255, 0.55) 10px 10px 20px 1px,
			rgba(0, 255, 255, 0.25) -10px -10px 20px 0px;
	}
	.error {
		text-align: center;
		font-weight: bold;
		font-size: 24pt;
		box-shadow: rgba(255, 0, 255, 0.55) 10px 10px 20px 1px,
			rgba(0, 255, 255, 0.25) -10px -10px 20px 0px;
	}
	.label {
		color: #999;
		font-size: 18px;
		font-weight: normal;
		position: absolute;
		pointer-events: none;
		left: 5px;
		top: 10px;
		transition: 0.2s ease all;
		-moz-transition: 0.2s ease all;
		-webkit-transition: 0.2s ease all;
	}
</style>
