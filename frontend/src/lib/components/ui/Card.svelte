<script lang="ts">
	import { type Snippet } from 'svelte';

	interface Props {
		class?: string;
		title?: string;
		children: Snippet;
	}

	let { class: className = '', title, children }: Props = $props();
</script>

<div class="bg-white rounded-xl shadow-sm border border-gray-100 {className}">
	{#if title}
		<div class="px-6 py-4 border-b border-gray-100">
			<h3 class="text-lg font-semibold text-gray-900">{title}</h3>
		</div>
	{/if}
	<div class="p-6">
		{@render children()}
	</div>
</div>
