<script lang="ts">
	import { onMount } from 'svelte';
	import Pagination from './Pagination.svelte';

	let currentPage: number = 1;
	let logs: ArrayLike<any> = [];
	let offset: number = 0;

	$: fetchData(offset);

	const fetchData = async (offset: number) => {
		const res = await fetch(`http://localhost:8003/logs/?offset=${offset}&limit=20`);
		logs = await res.json();
		console.log(logs);
	};

	onMount(() => fetchData(0));

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

<div>
	<table class="table loglist">
		<thead>
			<tr>
				<th style="text-align: left;">Title</th>
				<th style="text-align: left;">Map</th>
				<th style="text-align: center;">Format</th>
				<th style="text-align: center;">Views</th>
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
					<td style="text-align: left;">{convertDate(log.date)}</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
<Pagination
	{currentPage}
	on:message={(e) => {
		currentPage = e.detail.text;
		offset = currentPage * 20;
	}}
/>

<style lang="scss">
	.loglist tbody > tr:nth-child(2n + 1) {
		background: #f9f9f9;
	}
	.table {
		width: 100%;
		margin-bottom: 10px;
		background: none;
		font-size: medium;
		margin-top: 20px;

		td {
			padding: 8px;
			line-height: 20px;
			text-align: left;
			vertical-align: middle;
			border-right: 1px solid rgba(128, 128, 128, 0.17);
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
			border-right: 1px solid rgba(128, 128, 128, 0.17);
		}
	}
	table {
		max-width: 100%;
		background-color: transparent;
		border-collapse: collapse;
		border-spacing: 0;
	}
</style>
