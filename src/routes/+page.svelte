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
		montoCorregido = monto / $USDprice;
		montoCorregido = montoCorregido.toFixed(2);
		console.log('el cambio es: ', monto);
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
	{:then}<div class="bigPrice" padding="lg">
			<Card class="text-center" size="sm" padding="sm">
				<div class="text-2xl text-emerald-800 font-bold">
					{$USDprice}
				</div>
			</Card>
			<Card class="text-center" size="sm" padding="lg">
				<div class="text-8xl text-emerald-800 font-bold">
					{montoCorregido}
				</div>
			</Card>
			<Card class="text-center" size="lg" padding="lg">
				<input type="number" min="0" bind:value={monto} />
			</Card>
			<Button
				shadow="green"
				gradient
				color="green"
				on:click={() => {
					convertARStoUSD();
				}}>Cambiar</Button
			>
		</div>
	{/await}
</main>

<style>
	.bigPrice {
		text-align: center;
		align-items: center;
		padding: 150px 150px;
	}

	.main {
		background-color: orange;
	}
</style>
