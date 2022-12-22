<script>
	import '../app.postcss';
	import './styles.css';
</script>

<nav class="text-center">
	<a class="text-center font-bold navText" href="/">HOME</a>
	<a class="text-center font-bold navText" href="/about">ABOUT</a>
</nav>

<slot />

<footer>
	<div class="signature">
		<p>Hecho con &#128150; por BLOCK33</p>
	</div>
</footer>

<style>
	.signature {
		text-align: center;
		justify-items: center;
		position: relative;
		top: 0;
		left: 0;
		margin-top: 5%;
	}
	.navText {
		margin: 2em;
	}
	.navText:hover {
		color: rgb(240, 46, 170);
		transition: 0.2s;
	}
</style>
