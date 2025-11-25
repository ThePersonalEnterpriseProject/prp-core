<script lang="ts">
	import { type Snippet } from 'svelte';

	interface Props {
		type?: 'button' | 'submit' | 'reset';
		variant?: 'primary' | 'secondary' | 'ghost' | 'danger';
		class?: string;
		children: Snippet;
		onclick?: () => void;
		href?: string;
		fullWidth?: boolean;
		size?: 'sm' | 'md' | 'lg';
	}

	let {
		type = 'button',
		variant = 'primary',
		class: className = '',
		children,
		onclick,
		disabled = false,
		href,
		fullWidth = false,
		size = 'md'
	}: Props = $props();

	const baseStyles =
		'inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:opacity-50 disabled:pointer-events-none ring-offset-white';
	
	const variants = {
		primary: 'bg-indigo-600 text-white hover:bg-indigo-700 focus-visible:ring-indigo-500',
		secondary: 'bg-white text-gray-900 border border-gray-300 hover:bg-gray-50 focus-visible:ring-indigo-500',
		ghost: 'hover:bg-gray-100 hover:text-gray-900 focus-visible:ring-gray-500',
		danger: 'bg-red-600 text-white hover:bg-red-700 focus-visible:ring-red-500'
	};

	const sizes = {
		sm: 'h-8 px-3 text-xs',
		md: 'h-10 py-2 px-4 text-sm',
		lg: 'h-12 px-8 text-base'
	};
</script>

{#if href}
	<a
		{href}
		class="{baseStyles} {variants[variant]} {sizes[size]} {className} {fullWidth ? 'w-full' : ''}"
		onclick={onclick}
	>
		{@render children()}
	</a>
{:else}
	<button
		{type}
		class="{baseStyles} {variants[variant]} {sizes[size]} {className} {fullWidth ? 'w-full' : ''}"
		{onclick}
		{disabled}
	>
		{@render children()}
	</button>
{/if}
