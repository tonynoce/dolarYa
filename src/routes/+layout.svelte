<script>
	import '../app.postcss';
</script>

<nav class="text-center">
	<a class="text-center font-bold navText" href="/">HOME</a>
	<a class="text-center font-bold navText" href="/about">ABOUT</a>
</nav>

<slot />

<div class="signature">
	<p>Hecho con &#128150; por BLOCK33</p>
</div>

<style>
	.signature {
		text-align: center;
		position: relative;
		top: 150px;
		left: 0;
		right: 0;
	}
	.navText {
		margin: 2em;
	}
	.navText:hover {
		color: rgb(240, 46, 170);
		transition: 0.2s;
	}
</style>
