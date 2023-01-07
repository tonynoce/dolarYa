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
		<!-- <img src="DolarYaIcon.png" alt="Dollar ya" /> -->
		<div class="pictureWrapper">
			<picture>
				<source type="image/webp" srcset="DolarYaIcon.webp" />
				<img src="DolarYaIcon.png" alt="Picture of a dolar coin made by an AI" />
			</picture>
		</div>
		<br />
		<!-- 		<p>
			El precio es fetcheado desde la api de Yadio. <br />
			Un sitio donde están las cotizaciones del llamado dolar crypto, que suele fluctuar también los
			fines de semana y/o días feriados.
		</p>
		<p>
			Esto le da una ventaja sobre el dolar blue, que posee un volumen menor y no responde a los
			movimientos hechos por el retail.
		</p> -->
		<h1 class="text-2xl text-white text-center font-bold">Usamos el dolar crypto!</h1>
		<p>
			El precio que se utiliza de referencia es un promedio de todas las ofertas de compra-venta del
			mercado p2p crypto.
		</p>
		<p>
			De esta forma podemos tener una mejor referencia de la fluctuación con respecto a la
			cotización del dolar blue.
		</p>
	</div>
</main>

<style>
	main {
		background-color: rgb(27, 33, 39);
		color: white;
		margin-top: 5vh;
		margin-bottom: 18pt;
	}
	h1 {
		margin: 0px 0px 10% 0px;
	}

	.mainText {
		display: grid;
		/* grid-template-columns: 3fr; */
		justify-items: center;
		grid-column-start: 1;
		margin: 0 5vw 0 5vw;
	}

	.pictureWrapper {
		width: 50%;
		max-width: 200px;
		border-radius: 100%;
		animation-name: shadow;
		animation-duration: 6s;
		animation-iteration-count: infinite;
		animation-direction: alternate;
		animation-timing-function: ease-in-out;
		margin-bottom: 15px;
	}

	@keyframes shadow {
		0% {
			transform: rotate3d(0, 1, 0, 360deg);
			box-shadow: 0px 0px 20px rgb(196, 207, 41, 0.25);
		}
		50% {
			transform: rotate3d(0, 1, 0, 0deg);
			box-shadow: 0px 0px 50px rgb(41, 207, 97, 1);
		}
		100% {
			transform: rotate3d(1, 0, 0, 360deg);
			box-shadow: 0px 0px 20px rgb(196, 207, 41, 0.25);
		}
	}
</style>
