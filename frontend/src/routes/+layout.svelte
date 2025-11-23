<script lang="ts">
	import '../app.css';
	import Sidebar from '$lib/components/layout/Sidebar.svelte';
	import { type Snippet } from 'svelte';

	let { children }: { children: Snippet } = $props();
</script>

<div class="flex h-full">
	<Sidebar />
	<main class="flex-1 overflow-auto p-8">
		<div class="max-w-5xl mx-auto">
			{@render children()}
		</div>
	</main>
</div>
