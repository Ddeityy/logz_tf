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

<table class="table loglist">
	<thead>
		<tr>
			<th style="text-align: left;">Title</th>
			<th style="text-align: left;">Map</th>
			<th style="text-align: left;">Format</th>
			<th style="text-align: left;">Views</th>
			<th style="text-align: left;">Date</th>
		</tr>
	</thead>
	<tbody>
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
				<td style="text-align: center;">{log.player_count}</td>
				<td style="text-align: center;">{log.views}</td>
				<td>{convertDate(log.date)}</td>
			</tr>
		{/each}
	</tbody>
</table>

<style lang="scss">
	.loglist tbody > tr:nth-child(2n + 1) {
		background: #f9f9f9;
	}
	.table {
		width: 100%;
		margin-bottom: 10px;
		background: none;

		td {
			padding: 8px;
			line-height: 20px;
			text-align: left;
			vertical-align: middle;
			border-right: 1px solidrgba(0, 0, 0, 0.07);
		}
		a {
			color: #dd4814;
			text-decoration: none;
		}
		th {
			padding: 8px;
			line-height: 20px;
			text-align: left;
			vertical-align: middle;
			border-right: 1px solidrgba(0, 0, 0, 0.07);
		}
	}
	table {
		max-width: 100%;
		background-color: transparent;
		border-collapse: collapse;
		border-spacing: 0;
	}
</style>
