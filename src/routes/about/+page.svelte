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
		<img src="DolarYaIcon.png" alt="Dollar ya" />
		<br />
		<p>
			El precio es fetcheado desde la api de Yadio. <br />
			Un sitio donde están las cotizaciones del llamado dolar crypto, que suele fluctuar también los
			fines de semana y/o días feriados.
		</p>
		<p>
			Esto le da una ventaja sobre el dolar blue, que posee un volumen menor y no responde a los
			movimientos hechos por el retail.
		</p>
	</div>
</main>

<style>
	img {
		width: 50%;
		max-width: 200px;
		border-radius: 100%;
		animation-name: shadow;
		animation-duration: 2.5s;
		animation-iteration-count: infinite;
		animation-direction: alternate;
		animation-timing-function: ease-in-out;
	}

	@keyframes shadow {
		from {
			box-shadow: 0px 0px 50px rgb(41, 207, 97, 1);
		}
		to {
			box-shadow: 0px 0px 20px rgb(196, 207, 41, 0.25);
		}
	}

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

	h1 {
		margin: 0px 0px 10% 0px;
	}
</style>
