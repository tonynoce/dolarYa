<script lang="ts">
	import { onMount } from 'svelte';
	import { Spinner, Card, Button } from 'flowbite-svelte';

	import { USDprice, ARSprice } from '../stores/stores';
	import { getRate } from '../stores/stores';

	onMount(() => {
		getRate();
	});

	let monto = 0;
	let montoCorregido = 0;

	let currency = '';

	function convertARStoUSD() {
		montoCorregido = Math.abs(monto / $USDprice);
		montoCorregido = Number(montoCorregido.toFixed(2));
		currency = 'usd$';
		getRate();
		//return true;
	}

	function convertUSDtoARS() {
		montoCorregido = Math.abs(monto * $USDprice);
		montoCorregido = Number(montoCorregido.toFixed(2));
		currency = 'ars$';
		getRate();
		//return false;
	}
</script>

<body>
	{#await getRate()}
		<div class="text-center loader">
			<Spinner color="green" size="48" />
		</div>
	{:then}
		<div class="text-2xl text-white text-center font-bold">
			${$USDprice}
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

			<input type="number" class="inputCard" min="0" bind:value={monto} />
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
		padding: 15px 25px;
		grid-template-columns: repeat(1, 1fr);
		grid-gap: 15px;
		justify-items: center;
		margin: 150px 0px 80px 0px;
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
		box-shadow: rgba(240, 46, 170, 1) 0px 25px 20px -20px,
			rgba(240, 46, 170, 1) 0px -15px 20px -20px;
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
</style>
