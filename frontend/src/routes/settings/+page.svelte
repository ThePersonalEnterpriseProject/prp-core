<script lang="ts">
	import Card from '$lib/components/ui/Card.svelte';
	import Button from '$lib/components/ui/Button.svelte';
	import { PUBLIC_BACKEND_URL } from '$env/static/public';
	import { invalidateAll } from '$app/navigation';
	import { modules } from '$lib/stores/modules';
	import type { Module } from '$lib/stores/modules';

	let loading = $state(false);
	let message = $state<string | null>(null);
	let error = $state<string | null>(null);

	async function seedData(scenario: string) {
		console.log('seedData called with:', scenario);
		// if (!confirm('WARNING: This will wipe all existing data! Are you sure?')) {
		// 	console.log('User cancelled seedData');
		// 	return;
		// }

		console.log('User confirmed seedData');
		loading = true;
		message = null;
		error = null;

		try {
			console.log('Fetching:', `${PUBLIC_BACKEND_URL}/api/v1/debug/seed?scenario=${scenario}`);
			const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/debug/seed?scenario=${scenario}`, {
				method: 'POST'
			});
			console.log('Fetch response status:', res.status);

			if (res.ok) {
				message = `Successfully seeded ${scenario} data!`;
				await invalidateAll();
			} else {
				const err = await res.json();
				console.error('Seed error:', err);
				error = err.detail || 'Failed to seed data';
			}
		} catch (e) {
			console.error('Network error in seedData:', e);
			error = 'Network error occurred';
		} finally {
			loading = false;
		}
	}
</script>

<div class="space-y-8">
	<div>
		<h1 class="text-3xl font-bold text-gray-900">Settings</h1>
		<p class="text-gray-500 mt-1">Configure your personal enterprise preferences.</p>
	</div>

	<Card class="p-6">
		<h2 class="text-lg font-semibold text-gray-900 mb-4">Developer Tools</h2>
		<div class="bg-yellow-50 border border-yellow-200 rounded-md p-4 mb-6">
			<div class="flex">
				<div class="flex-shrink-0">
					<svg class="h-5 w-5 text-yellow-400" viewBox="0 0 20 20" fill="currentColor">
						<path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
					</svg>
				</div>
				<div class="ml-3">
					<h3 class="text-sm font-medium text-yellow-800">Fake Data Generator</h3>
					<div class="mt-2 text-sm text-yellow-700">
						<p>Use these buttons to populate the database with sample data. <strong>This will wipe all existing data.</strong></p>
					</div>
				</div>
			</div>
		</div>

		{#if message}
			<div class="bg-green-50 text-green-700 p-3 rounded-md mb-4">{message}</div>
		{/if}
		{#if error}
			<div class="bg-red-50 text-red-700 p-3 rounded-md mb-4">{error}</div>
		{/if}

		<div class="grid grid-cols-1 md:grid-cols-3 gap-4">
			<div class="border border-gray-200 rounded-lg p-4 hover:border-indigo-200 transition-colors">
				<h3 class="font-medium text-gray-900 mb-2">Young Professional</h3>
				<p class="text-sm text-gray-500 mb-4">Simple setup with checking, savings, credit card, and student loans.</p>
				<Button variant="secondary" class="w-full" onclick={() => seedData('young_professional')} disabled={loading}>
					Load Scenario
				</Button>
			</div>

			<div class="border border-gray-200 rounded-lg p-4 hover:border-indigo-200 transition-colors">
				<h3 class="font-medium text-gray-900 mb-2">Family</h3>
				<p class="text-sm text-gray-500 mb-4">Complex setup with joint accounts, mortgage, car loans, and retirement.</p>
				<Button variant="secondary" class="w-full" onclick={() => seedData('family')} disabled={loading}>
					Load Scenario
				</Button>
			</div>

			<div class="border border-gray-200 rounded-lg p-4 hover:border-indigo-200 transition-colors">
				<h3 class="font-medium text-gray-900 mb-2">Small Business</h3>
				<p class="text-sm text-gray-500 mb-4">Mixed personal and business accounts with inventory loans.</p>
				<Button variant="secondary" class="w-full" onclick={() => seedData('small_business')} disabled={loading}>
					Load Scenario
				</Button>
			</div>
		</div>
	</Card>

	<Card class="p-6">
		<h2 class="text-lg font-semibold text-gray-900 mb-4">Modules</h2>
		<p class="text-gray-500 mb-6">Enable or disable features to customize your experience.</p>

		<div class="space-y-4">
			{#each $modules as module}
				<div class="flex items-center justify-between p-4 border border-gray-200 rounded-lg">
					<div>
						<h3 class="font-medium text-gray-900 capitalize">{module.name}</h3>
						<p class="text-sm text-gray-500">
							{module.name === 'finance' ? 'Accounts, transactions, and financial tracking.' : 'Module feature.'}
						</p>
					</div>
					<label class="relative inline-flex items-center cursor-pointer">
						<input 
							type="checkbox" 
							class="sr-only peer" 
							checked={module.is_enabled}
							onchange={async (e) => {
								const enabled = e.currentTarget.checked;
								try {
									const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/modules/${module.name}`, {
										method: 'PUT',
										headers: { 'Content-Type': 'application/json' },
										body: JSON.stringify({ is_enabled: enabled })
									});
									if (res.ok) {
										// Update local store
										modules.update((ms: Module[]) => ms.map((m: Module) => 
											m.name === module.name ? { ...m, is_enabled: enabled } : m
										));
										await invalidateAll(); // Refresh layout to update sidebar
									}
								} catch (err) {
									console.error('Failed to toggle module', err);
									// Revert checkbox if failed (optional, but good UX)
									e.currentTarget.checked = !enabled;
								}
							}}
						>
						<div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-indigo-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-indigo-600"></div>
					</label>
				</div>
			{/each}
		</div>
	</Card>
</div>
