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

	function convertARStoUSD() {
		montoCorregido = Math.abs(monto / $USDprice);
		montoCorregido = montoCorregido.toFixed(2);
		return montoCorregido;
	}

	function convertUSDtoARS() {
		montoCorregido = Math.abs(monto * $USDprice);
		montoCorregido = montoCorregido.toFixed(2);
		return montoCorregido;
	}
</script>

<!-- <main>
	<h1>Welcome to SvelteKit</h1>
	<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
</main>
 -->

<main class="main">
	{#await getRate()}
		<div class="text-center">
			<Spinner color="green" size="8" />
		</div>
	{:then}
		<div class="bigPrice">
			<Card class="text-center" size="sm" padding="sm">
				<div class="text-2xl text-emerald-800 font-bold">
					{$USDprice}
					<p class="text-base">La cotización del día</p>
				</div>
			</Card>
			<br />
			<Card class="text-center" size="sm" padding="lg">
				<div class="text-8xl text-emerald-800 font-bold">
					{montoCorregido}
				</div>
			</Card>
			<br />
			<Card class="text-center" size="lg" padding="lg">
				<input type="number" min="0" bind:value={monto} />
			</Card>
			<div class="btBuy">
				<Button
					shadow="green"
					gradient
					color="green"
					size="xl"
					on:click={() => {
						convertARStoUSD();
					}}>Cambiar Argentinos</Button
				>
			</div>
			<div class="btBuy">
				<Button
					shadow="red"
					gradient
					color="red"
					size="xl"
					on:click={() => {
						convertUSDtoARS();
					}}>Cambiar Dólares</Button
				>
			</div>
		</div>
	{/await}
</main>

<style>
	div {
		padding: 15px 15px;
	}

	.bigPrice {
		text-align: center;
		align-items: center;
		padding: 150px 25px;
	}

	main {
		background-color: orange;
		align-content: center;
	}
	.btBuy {
		padding: 25px 25px;
	}
</style>
