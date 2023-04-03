<script lang="ts">
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import { steamID } from '../stores';

	onMount(() => {
		let url = $page.url;
		steamID.set(url.searchParams.get('openid.claimed_id')?.slice(37)!);
		window.location.replace(`http://localhost:5174/`);
	});
</script>
