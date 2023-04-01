<script lang="ts">
	import { page } from '$app/stores';
	import { onMount } from 'svelte';

	onMount(() => {
		let url = $page.url;
		window.location.replace(
			`http://localhost:5174/?steamid=${url.searchParams.get('openid.claimed_id')?.slice(37)}`
		);
	});
</script>
