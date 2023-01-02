<script lang="ts">
	/**
	 * lo de abajo se creo solo
	 */
	/* 	import type { PageData } from './$types';

	export let data: PageData; */
</script>

<main>
	<div class="mainText">
		<h1 class="text-5xl text-white text-center font-bold">ABOUT</h1>
		<br />
		<p>
			El precio es fetcheado desde la api de Yadio. <br />
			Un sitio donde están las cotizaciones del llamado dolar crypto, que suele fluctuar también los
			fines de semana y/o días feriados.
		</p>
		<br />
		<p>
			Esto le da una ventaja sobre el dolar blue, que posee un volumen menor y no responde a los
			movimientos hechos por el retail.
		</p>
	</div>
</main>

<style>
	main {
		background-color: rgb(27, 33, 39);
		color: white;
		margin-top: 5vh;
	}
	.mainText {
		display: grid;
		grid-template-columns: 100%;
		justify-items: center;
		grid-column-start: 1;
		margin: 5vw;
	}
</style>
