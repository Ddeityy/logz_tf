<script>
	let logo = 'logo-top.png';
	let steamButton = 'steam_small.png';
</script>

<div class="topbar">
	<div class="navbar container">
		<div class="logo">
			<img src={logo} alt="" />
		</div>
		<div class="navbar-search">
			<form action="">
				<input
					id="player-search"
					type="text"
					name="s"
					placeholder="Player name or SteamID…"
					maxlength="60"
				/>
			</form>
		</div>
		<div class="steam-login"><img src={steamButton} alt="" /></div>
	</div>
</div>

<style lang="scss">
	.topbar {
		background: #444;
		border-bottom: 4px solid #333;
		margin-bottom: 15px;
		min-width: 980px;
		border-radius: 5px;
	}
	.navbar-search {
		flex: 1;
		margin: 0 60px;
	}

	.navbar-search form {
		margin: 0;
		display: inline-block;
		width: 100%;
	}

	.navbar-search input {
		margin: 0;
		padding: 7px;
		width: 100%;
		border: 0;
		border-top: 1px solid rgba(0, 0, 0, 0.1);
		background: #333;
		color: #fff;
	}
	.container {
		margin-right: auto;
		margin-left: auto;
		box-sizing: border-box;
		width: 980px !important;
	}

	.navbar {
		position: relative;
		padding: 8px 0;
		display: flex;
		align-items: center;
		justify-items: center;
		align-content: space-between;
	}

	.logo {
		font-family: Arial, sans-serif;
		font-size: 14px;
		line-height: 20px;
		color: #444;
		margin-left: 10px;
		img {
			width: 114.3px;
			height: 34px;
		}
	}
	.steam-login {
		margin-top: 5px;
		margin-right: 10px;
	}
</style>
