<script lang="ts">
	import Table from './Table.svelte';
	import Header from './Header.svelte';
	import Blur from './Blur.svelte';
	import Footer from './Footer.svelte';
</script>

<body>
	<Header />
	<Blur />
	<div class="container main">
		<Table />
		<Footer />
	</div>
</body>

<style lang="scss">
	.container {
		align-items: center;
		max-width: 980px !important;
		border-bottom-left-radius: 5px;
		border-bottom-right-radius: 5px;
	}
	.container::before {
		display: table;
		content: '';
		line-height: 0;
	}
	.container::after {
		clear: both;
	}
	.main {
		position: relative;
		align-items: center;
		background: #fff;
		min-height: 100%;
		padding: 0 30px 0 30px;
		flex-grow: 1;
	}
	body {
		position: absolute;
		top: 50%;
		left: 50%;
		min-height: 100vh;
		margin-right: -50%;
		transform: translate(-50%, -50%);
		margin: 0;
		background: #272822;
		font-family: Arial, sans-serif;
		font-size: 14px;
		line-height: 20px;
		color: #444;
		flex-direction: column;
		display: flex;
		height: 100%;
	}
</style>
