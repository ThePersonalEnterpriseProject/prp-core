<script lang="ts">
	import { page } from '$app/stores';

	import { modules, isModuleEnabled } from '$lib/stores/modules';

	const baseLinks = [
		{ href: '/', label: 'Dashboard', icon: 'Home' },
		{ href: '/accounts', label: 'Accounts', icon: 'Wallet', module: 'finance' },
		{ href: '/transactions', label: 'Transactions', icon: 'List', module: 'finance' },
		{ href: '/assets', label: 'Assets', icon: 'Box', module: 'assets' },
		{ href: '/settings', label: 'Settings', icon: 'Settings' }
	];

	let links = $derived(baseLinks.filter(link => 
		!link.module || isModuleEnabled(link.module, $modules)
	));
</script>

<aside class="w-64 bg-white border-r border-gray-200 flex flex-col h-full">
	<div class="p-6 border-b border-gray-100">
		<h1 class="text-xl font-bold text-indigo-600 flex items-center gap-2">
			<span class="text-2xl">⚡</span> PRP Core
		</h1>
	</div>

	<nav class="flex-1 p-4 space-y-1">
		{#each links as link}
			<a
				href={link.href}
				class="flex items-center gap-3 px-4 py-3 text-sm font-medium rounded-lg transition-colors
        {$page.url.pathname === link.href
					? 'bg-indigo-50 text-indigo-700'
					: 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'}"
			>
				<!-- Simple icon placeholders -->
				{#if link.icon === 'Home'}
					<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
				{:else if link.icon === 'Wallet'}
					<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12V7H5a2 2 0 0 1 0-4h14v4"/><path d="M3 5v14a2 2 0 0 0 2 2h16v-5"/><path d="M18 12a2 2 0 0 0 0 4h4v-4Z"/></svg>
				{:else if link.icon === 'List'}
					<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>
				{:else if link.icon === 'Box'}
					<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>
				{:else if link.icon === 'Settings'}
					<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.1a2 2 0 0 1-1-1.74v-.47a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/></svg>
				{/if}
				{link.label}
			</a>
		{/each}
	</nav>

	<div class="p-4 border-t border-gray-100">
		<div class="flex items-center gap-3 px-4 py-3 text-sm text-gray-600">
			<div class="w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center font-bold text-gray-500">
				U
			</div>
			<div>
				<p class="font-medium text-gray-900">User</p>
				<p class="text-xs">user@example.com</p>
			</div>
		</div>
	</div>
</aside>
