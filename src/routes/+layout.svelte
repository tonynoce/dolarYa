<script>
	import '../app.postcss';
	import './styles.css';
</script>

<nav class="text-center">
	<a class="text-center font-bold navText" href="/">HOME</a>
	<a class="text-center font-bold navText" href="/historial">HISTORIAL</a>
	<a class="text-center font-bold navText" href="/about">ABOUT</a>
</nav>

<body>
	<slot />
</body>

<footer>
	<div class="footer">
		<p class="signature">Hecho con &#128150; por BLOCK33</p>
	</div>
</footer>

<style>
	nav {
		display: grid;
		grid-template-columns: repeat(3, auto);
	}

	.footer {
		position: fixed;
		left: 0;
		bottom: 0;
		width: 100%;
		background-image: linear-gradient(rgb(27, 33, 39), rgb(10, 48, 66));
		/* background-image: linear-gradient(rgba(255, 0, 179, 0.05), rgba(0, 255, 242, 0.062)); */
		color: white;
		text-align: center;
		opacity: 1;
	}

	.signature {
		margin-bottom: 7px;
	}

	.navText {
		margin: 2em;
	}
	.navText:hover {
		color: rgb(240, 46, 170);
		transition: 0.2s;
	}
</style>
