<script>
	let logo = 'logo-top.png';
	let steamButton = 'steam_small.png';
</script>

<div class="topbar">
	<div class="navbar container">
		<div class="logo">
			<img src={logo} alt="" />
		</div>
		<div class="search-box"><input type="text" placeholder="Logs..." /></div>
		<div class="steam-login"><img src={steamButton} alt="" /></div>
	</div>
</div>

<style>
	.topbar {
		background: #444;
		border-bottom: 4px solid #333;
		margin-bottom: 15px;
		min-width: 980px;
	}

	.container {
		margin-right: auto;
		margin-left: auto;
		*zoom: 1;
		box-sizing: border-box;
		width: 980px !important;
	}

	.navbar {
		position: relative;
		padding: 8px 0;
		display: flex;
		align-items: center;
	}

	.logo {
		font-family: Arial, sans-serif;
		font-size: 14px;
		line-height: 20px;
		color: #444;
	}

	img {
		width: 120px;
		height: 40px;
	}
</style>
