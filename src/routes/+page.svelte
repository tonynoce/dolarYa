<script lang="ts">
	import { onMount } from 'svelte';

	import { USDprice, ARSprice } from '../stores/stores';
	import { getRate } from '../stores/stores';

	onMount(() => {
		getRate();
	});
</script>

<!-- <main>
	<h1>Welcome to SvelteKit</h1>
	<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
</main>
 -->

<main>
	{#await getRate()}
		Loading...
	{:then}
		<div class="bigPrice">
			{$USDprice}
		</div>
	{/await}
</main>

<style>
	.bigPrice {
		text-align: center;
		font-size: 140px;
		font-family: sans-serif;
	}
</style>
