<script>
	import '../app.postcss';
	import './styles.css';
</script>

<nav class="text-center">
	<a class="text-center font-bold navText" href="/">HOME</a>
	<a class="text-center font-bold navText" href="/about">ABOUT</a>
</nav>

<body>
	<slot />
</body>

<footer>
	<div class="signature">
		<p>Hecho con &#128150; por BLOCK33</p>
	</div>
</footer>

<style>
	.signature {
		position: fixed;
		left: 0;
		bottom: 0;
		width: 100%;
		background-image: linear-gradient(rgba(255, 0, 179, 0.05), rgba(0, 255, 242, 0.062));
		color: white;
		text-align: center;
	}
	.navText {
		margin: 2em;
	}
	.navText:hover {
		color: rgb(240, 46, 170);
		transition: 0.2s;
	}
</style>
