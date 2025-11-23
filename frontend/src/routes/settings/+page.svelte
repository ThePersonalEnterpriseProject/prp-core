<script lang="ts">
	import Card from '$lib/components/ui/Card.svelte';
	import Button from '$lib/components/ui/Button.svelte';
	import { PUBLIC_BACKEND_URL } from '$env/static/public';
	import { invalidateAll } from '$app/navigation';

	let loading = $state(false);
	let message = $state<string | null>(null);
	let error = $state<string | null>(null);

	async function seedData(scenario: string) {
		if (!confirm('WARNING: This will wipe all existing data! Are you sure?')) return;

		loading = true;
		message = null;
		error = null;

		try {
			const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/debug/seed?scenario=${scenario}`, {
				method: 'POST'
			});

			if (res.ok) {
				message = `Successfully seeded ${scenario} data!`;
				await invalidateAll();
			} else {
				const err = await res.json();
				error = err.detail || 'Failed to seed data';
			}
		} catch (e) {
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
</div>
