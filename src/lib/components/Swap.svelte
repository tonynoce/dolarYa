<script lang="ts">
	import { Button } from 'flowbite-svelte';

	import { USDprice, ARSprice } from '../../stores/stores';
	import { getRate } from '../../stores/stores';

	let monto: any = 0;
	let montoCorregido: any = 0;

	let storeARStoUSD: any = [];
	let storeUSDtoARS: any = [];

	let currency = '';

	export let offline: boolean;
	export let theDate: Date;

	$: offline;

	function vibrateARS() {
		navigator.vibrate([100, 30, 100]);
		/* console.log('brrArs'); */
	}

	function vibrateUSD() {
		navigator.vibrate([200, 30, 200, 30, 200]);
		/* console.log('brrUsd'); */
	}

	function saveARStoUSD() {
		storeARStoUSD.push([
			monto.toLocaleString('es-AR', {
				maximumFractionDigits: 2
			}),
			montoCorregido
		]);

		let populateStorage: any = [];

		if (localStorage.getItem('arstousd') != null) {
			populateStorage = JSON.parse(localStorage.getItem('arstousd'));
			//console.log(populateStorage);

			populateStorage.push([
				monto.toLocaleString('es-AR', {
					maximumFractionDigits: 2
				}),
				montoCorregido
			]);

			localStorage.setItem('arstousd', JSON.stringify(populateStorage));
		} else if (localStorage.getItem('arstousd') == null) {
			localStorage.setItem('arstousd', JSON.stringify(storeARStoUSD));
		}
	}

	function saveUSDtoARS() {
		storeUSDtoARS.push([
			monto.toLocaleString('es-AR', {
				maximumFractionDigits: 2
			}),
			montoCorregido
		]);

		let populateStorage: any = [];

		if (localStorage.getItem('usdtoars') != null) {
			populateStorage = JSON.parse(localStorage.getItem('usdtoars'));

			//console.log(populateStorage);
			populateStorage.push([
				monto.toLocaleString('es-AR', {
					maximumFractionDigits: 2
				}),
				montoCorregido
			]);

			localStorage.setItem('usdtoars', JSON.stringify(populateStorage));
		} else if (localStorage.getItem('usdtoars') == null) {
			localStorage.setItem('usdtoars', JSON.stringify(storeUSDtoARS));
		}
	}
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
				vibrateARS();
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
				vibrateARS();
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
				vibrateUSD();
			} catch (e) {
				console.log(e);
			}
		}
	}
</script>

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

{#if offline == true}
	<div class="text-center">
		<h1 class="text-1xl font-bold">Último precio de la cotización:</h1>
		<p class="text-white font-thin text-center">{theDate.toLocaleString()}</p>
	</div>
{:else}
	<p class="text-white font-thin text-center">La cotización del momento, provista por Yadio</p>
{/if}

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
