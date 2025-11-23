<script lang="ts">
	import type { PageData } from './$types';
	import { invalidateAll, goto } from '$app/navigation';
	import { PUBLIC_BACKEND_URL } from '$env/static/public';
	import Card from '$lib/components/ui/Card.svelte';
	import Button from '$lib/components/ui/Button.svelte';
	import Input from '$lib/components/ui/Input.svelte';

	let { data }: { data: PageData } = $props();

	let name = $state('');
	let account_type = $state('Asset');
	let error: string | null = $state(null);

	async function createAccount() {
		error = null;
		const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/accounts/`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				name,
				account_type
			})
		});

		if (res.ok) {
			name = '';
			account_type = 'Asset';
			await invalidateAll();
		} else {
			const err = await res.json();
			error = err.detail || 'Failed to create account.';
		}
	}
</script>

<div class="space-y-8">
	<!-- Header -->
	<div class="flex items-center justify-between">
		<div>
			<h1 class="text-3xl font-bold text-gray-900">Dashboard</h1>
			<p class="text-gray-500 mt-1">Overview of your personal enterprise.</p>
		</div>
		<div class="text-right">
			<p class="text-sm text-gray-500">Net Worth</p>
			<p class="text-3xl font-bold text-indigo-600">${data.netWorth.toFixed(2)}</p>
		</div>
	</div>

	<div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
		<!-- Create Account Form -->
		<div class="lg:col-span-1">
			<Card class="p-6">
				<h2 class="text-lg font-semibold text-gray-900 mb-4">Add Account</h2>
				{#if error}
					<div class="bg-red-50 text-red-700 p-3 rounded-md text-sm mb-4 flex items-start gap-2">
						<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
							<path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
						</svg>
						<span>{error}</span>
					</div>
				{/if}
				<form onsubmit={(e) => { e.preventDefault(); createAccount(); }} class="space-y-4">
					<div>
						<label for="name" class="block text-sm font-medium text-gray-700 mb-1">Account Name</label>
						<Input id="name" bind:value={name} placeholder="e.g. Chase Checking" required />
					</div>
					<div>
						<label for="type" class="block text-sm font-medium text-gray-700 mb-1">Type</label>
						<select
							id="type"
							bind:value={account_type}
							class="flex h-10 w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
						>
							<option>Asset</option>
							<option>Liability</option>
						</select>
					</div>
					<Button type="submit" class="w-full">Create Account</Button>
				</form>
			</Card>
		</div>

		<!-- Accounts List -->
		<div class="lg:col-span-2">
			<Card>
				<div class="px-6 py-4 border-b border-gray-100">
					<h2 class="text-lg font-semibold text-gray-900">Accounts</h2>
				</div>
				<div class="overflow-x-auto">
					<table class="w-full text-left text-sm">
						<thead class="bg-gray-50 text-gray-500">
							<tr>
								<th class="px-6 py-3 font-medium">Name</th>
								<th class="px-6 py-3 font-medium">Type</th>
								<th class="px-6 py-3 font-medium text-right">Balance</th>
							</tr>
						</thead>
						<tbody class="divide-y divide-gray-100">
							{#each data.accounts as account}
								<tr 
									onclick={() => goto(`/transactions?account=${account.id}`)}
									class="hover:bg-gray-50 transition-colors cursor-pointer"
								>
									<td class="px-6 py-4 font-medium text-gray-900">{account.name}</td>
									<td class="px-6 py-4">
										<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium
											{account.account_type === 'Asset' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}">
											{account.account_type}
										</span>
									</td>
									<td class="px-6 py-4 text-right font-medium text-gray-900">
										${account.balance.toFixed(2)}
									</td>
								</tr>
							{:else}
								<tr>
									<td colspan="3" class="px-6 py-8 text-center text-gray-500">
										No accounts yet. Create one to get started!
									</td>
								</tr>
							{/each}
						</tbody>
					</table>
				</div>
			</Card>
		</div>
	</div>
</div>
