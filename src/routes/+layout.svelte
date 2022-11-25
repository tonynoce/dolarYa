<script>
	import '../app.postcss';
</script>

<nav class="text-center font-bold">
	<a href="/">Home</a>
	<a href="/about">About</a>
</nav>

<slot />

<div class="signature">
	<p>Hecho con &#128150; por BLOCK33</p>
</div>

<style>
	.signature {
		text-align: center;
		position: fixed;
		bottom: 25px;
		left: 0;
		right: 0;
	}
</style>
