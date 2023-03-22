<script lang="ts">
	import { onMount } from 'svelte';
	import Header from './Header.svelte';

	let logs: ArrayLike<any> = [];
	let currentPage: number = 0;
	let offset: number = currentPage * 25;

	onMount(async () => {
		const res = await fetch(`http://localhost:8003/logs/?offset=${offset}`);
		logs = await res.json();
		console.log(logs);
	});
	const options: Object = {
		year: 'numeric',
		month: 'short',
		day: 'numeric',
		timeZone: 'CET',
		hour: '2-digit',
		minute: '2-digit',
		hour12: true
	};
	const convertDate = (date: any) => {
		let result = new Date(Number(date * 1000));
		return result.toLocaleString('en-GB', options);
	};
</script>

<body>
	<Header />
	<table>
		<tr>
			<th style="text-align: left;">Title</th>
			<th style="text-align: left;">Map</th>
			<th style="text-align: center;">Format</th>
			<th style="text-align: center;">Views</th>
			<th style="text-align: left;">Date</th>
		</tr>
		{#each logs as log}
			<tr>
				<td>
					<label for={''}>
						<a href="/logs/{log.log_id}">
							{log.title}
						</a>
					</label></td
				>
				<td>{log.map}</td>
				<td>{log.player_count}</td>
				<td>{log.views}</td>
				<td>{convertDate(log.date)}</td>
			</tr>
		{/each}
	</table>
</body>

<style>
	body {
		margin: 0;
		background: #272822;
		font-family: Arial, sans-serif;
		font-size: 14px;
		line-height: 20px;
		color: #444;
		height: 100%;
	}
</style>
