<script lang="ts">
	import { onMount } from 'svelte';
	import { Button } from 'flowbite-svelte';

	/* 
	import type { PageData } from './$types';
	
	export let data: PageData;
	*/
	let storageARS: any = [];
	let storageUSD: any = [];
	let storageCleaned = false;

	$: storageARS;
	$: storageUSD;

	function getStorage() {
		if (storageARS != null) {
			try {
				if (storageARS.lenght != 0) {
					storageARS = JSON.parse(sessionStorage.getItem('arstousd'));
				}
			} catch (e) {
				console.log(e);
			}
		}
		if (storageUSD != null) {
			try {
				if (storageUSD.lenght != 0) {
					storageUSD = JSON.parse(sessionStorage.getItem('usdtoars'));
				}
			} catch (e) {
				console.log(e);
			}
		}
	}

	function cleanStorage() {
		//sessionStorage.clear('arstousd');
		sessionStorage.removeItem('arstousd');
		sessionStorage.removeItem('usdtoars');
		getStorage();
	}

	onMount(() => {
		getStorage();
	});
</script>

<main>
	{#if storageARS == null && storageUSD == null}
		<div class="shinyTitle loader">
			<h1 class="text-4xl text-white  font-bold">Aquí verás tus conversiones</h1>
		</div>
	{/if}
	<div class="listWrapper">
		{#if storageARS != null || storageUSD != null}
			<div class="buttonWrapper">
				<Button
					shadow="blue"
					gradient
					color="alternative"
					size="xl"
					on:click={() => {
						cleanStorage();
					}}>Borrar historial</Button
				>
			</div>
		{/if}
		{#if storageARS != null}
			<!-- ARS storage -->
			<h1 class="text-2xl text-white text-center font-bold">ARS convertido a USD</h1>
			<div class="exchangeWrapper">
				{#each storageARS as monto, i}
					<!-- 				<li>
					{i + 1} = ars${monto[0]} => usd${monto[1]}
				</li> -->
					<p>
						{i + 1}
					</p>
					<p>
						ars${monto[0]}
					</p>
					<p>
						usd${monto[1]}
					</p>
				{/each}
			</div>

			<!-- USD storage -->
		{/if}
		<br />
		{#if storageUSD != null}
			<h1 class="text-2xl text-white text-center font-bold">USD convertido a ARS</h1>
			<div class="exchangeWrapper">
				{#each storageUSD as monto, i}
					<p>
						{i + 1}
					</p>
					<p>
						usd${monto[0]}
					</p>
					<p>
						ars${monto[1]}
					</p>
				{/each}
			</div>
		{/if}
	</div>
</main>

<style>
	main {
		margin-bottom: 18pt;
	}
	li {
		list-style: none;
	}

	.listWrapper {
		display: grid;
		grid-template-columns: 100%;
		justify-items: center;
	}

	.buttonWrapper {
		margin: 0 0 25px 0;
	}

	.exchangeWrapper {
		display: grid;
		grid-template-columns: 1fr 2fr 2fr;
		width: 80%;
	}

	.shinyTitle {
		text-align: center;
		animation-name: changecolor;
		animation-duration: 2.5s;
		animation-iteration-count: infinite;
		animation-direction: alternate;
		animation-timing-function: ease-in-out;
	}

	@keyframes changecolor {
		from {
			text-shadow: rgb(240, 46, 170) 0px 5px 20px;
		}
		to {
			text-shadow: rgb(46, 201, 240) 0px -5px 10px;
		}
	}
</style>
