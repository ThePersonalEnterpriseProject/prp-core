<script lang="ts">
	import { type Snippet } from 'svelte';

	interface Props {
		class?: string;
		children: Snippet;
	}

	let { class: className = '', children }: Props = $props();
</script>

<div class="bg-white rounded-xl shadow-sm border border-gray-100 {className}">
	{@render children()}
</div>
