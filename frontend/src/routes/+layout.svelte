<script lang="ts">
	import '../app.css';
	import Sidebar from '$lib/components/layout/Sidebar.svelte';
	import { type Snippet } from 'svelte';

	import { modules } from '$lib/stores/modules';
	import type { Module } from '$lib/stores/modules';

	let { children, data }: { children: Snippet, data: { modules: Module[] } } = $props();

	$effect(() => {
		if (data.modules) {
			modules.set(data.modules);
		}
	});
</script>

<div class="flex h-full">
	<Sidebar />
	<main class="flex-1 overflow-auto p-8">
		<div class="max-w-5xl mx-auto">
			{@render children()}
		</div>
	</main>
</div>
