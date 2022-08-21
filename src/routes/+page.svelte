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

<body>
	{#await getRate()}
		<div class="text-center loader">
			<Spinner color="green" size="48" />
		</div>
	{:then}
		<div class="bigPrice">
			<Card class="text-center" size="sm" padding="sm">
				<div class="text-2xl text-emerald-800 font-bold">
					${$USDprice}
					<p class="text-base">La cotización del momento</p>
				</div>
			</Card>

			<Card class="text-center" size="xl" padding="md">
				<div class="text-8xl text-emerald-800 font-bold">
					${montoCorregido}
				</div>
			</Card>

			<Card class="text-center" size="md" padding="lg">
				<input type="number" min="0" bind:value={monto} />
			</Card>
		</div>
		<div class="buttons">
			<Button
				shadow="red"
				gradient
				color="blue"
				size="xl"
				on:click={() => {
					convertARStoUSD();
				}}>Cambiar Argentinos</Button
			>
			<Button
				shadow="red"
				gradient
				color="green"
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
		background-color: orange;
		align-self: center;
		justify-self: center;
	}

	.bigPrice {
		display: grid;
		padding: 15px 25px;
		grid-template-columns: repeat(1, 1fr);
		grid-gap: 15px;
		justify-items: center;
	}

	.loader {
		padding-top: 50%;
	}
	.buttons {
		padding: 25px 25px;
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		grid-gap: 10px;
		grid-auto-rows: minmax(75px, auto);
	}
</style>
