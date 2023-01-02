<script lang="ts">
	import { onMount } from 'svelte';
	import { browser } from '$app/env';
	import { Spinner, Card, Button } from 'flowbite-svelte';
	import { Input } from 'flowbite-svelte';

	import { USDprice, ARSprice } from '../stores/stores';
	import { getRate } from '../stores/stores';

	/* 	onMount(() => {
		getRate();
	}); */

	let monto: any = 0;
	let montoCorregido: any = 0;

	let storeARStoUSD: any = [];
	let storeUSDtoARS: any = [];

	let currency = '';

	function saveARStoUSD() {
		monto = monto.toLocaleString('es-AR', {
			maximumFractionDigits: 2
		});
		storeARStoUSD.push([monto, montoCorregido]);
		sessionStorage.setItem('arstousd', JSON.stringify(storeARStoUSD));
	}

	function saveUSDtoARS() {
		monto = monto.toLocaleString('es-AR', {
			maximumFractionDigits: 2
		});
		storeUSDtoARS.push([monto, montoCorregido]);
		sessionStorage.setItem('usdtoars', JSON.stringify(storeUSDtoARS));
	}

	function addZeros(numberTo: number) {}

	function convertARStoUSD() {
		if (monto == 0) {
			0;
			/**
			 * @dev this is because argentinian peso has many zeros in front, sight !
			 */
		} else if (monto < Number($USDprice)) {
			try {
				montoCorregido = Math.abs(monto / $USDprice);
				//montoCorregido = Number(montoCorregido.toFixed(4));
				montoCorregido = montoCorregido.toLocaleString('es-AR', {
					maximumFractionDigits: 4
				});
				currency = 'usd$';
				getRate();
				saveARStoUSD();
			} catch (e) {
				console.log(e);
			}
		} else {
			try {
				montoCorregido = Math.abs(monto / $USDprice);
				//montoCorregido = Number(montoCorregido.toFixed(2));
				montoCorregido = montoCorregido.toLocaleString('es-AR', {
					maximumFractionDigits: 2
				});
				currency = 'usd$';
				getRate();
				saveARStoUSD();
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
				//montoCorregido = Number(montoCorregido.toFixed(2));
				montoCorregido = montoCorregido.toLocaleString('es-AR', {
					maximumFractionDigits: 2
				});
				currency = 'ars$';
				getRate();
				saveUSDtoARS();
			} catch (e) {
				console.log(e);
			}
		}
	}

	/*
	onMount(() => {
		sessionStorage.setItem('arstousd', '');
		sessionStorage.setItem('usdtoars', '');
	});
	*/

	/*
	function addToFavorites() {
		if (browser) {
			var title = document.title;
			var url = document.location;
			try {
				window.external.AddFavorite(url, title);
				AddFavorite(url, title);
			} catch (e) {}
			try {
				window.sidebar.addPanel(title, url, '');
			} catch (e) {
				alert(
					'Su navegador no nos deja agregar a favoritos.\n\nPlease use Ctrl+D to bookmark this page.'
					);
				}
			}
		}
	*/
</script>

<main>
	{#await getRate()}
		<div class="loader">
			<Spinner color="green" size="48" />
		</div>
	{:then}
		<!-- Top prices -->
		<div class="text-2xl text-white text-center font-bold">
			Compra ${($ARSprice * 1e5).toLocaleString('es-AR', {
				minimumFractionDigits: 2,
				maximumFractionDigits: 2
			})}
			<br />
			Venta ${$USDprice.toLocaleString('es-AR', {
				minimumFractionDigits: 2,
				maximumFractionDigits: 2
			})}
		</div>
		<br />
		<p class="text-white font-thin text-center">La cotización del momento, provista por Yadio</p>

		<!-- Big price -->
		<div class="bigPrice">
			<div class="text-5xl text-white text-center font-bold montoCorregido">
				<p>{montoCorregido}</p>
				<p class="currency">{currency}</p>
			</div>
			<input type="number" class="inputCard text-center font-bold " min="0" bind:value={monto} />
		</div>
		<!-- Buy and sell buttons -->
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
