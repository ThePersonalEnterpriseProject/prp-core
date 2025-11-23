<script lang="ts">
	import type { PageData } from './$types';
	import { invalidateAll } from '$app/navigation';
	import { PUBLIC_BACKEND_URL } from '$env/static/public';
	import Card from '$lib/components/ui/Card.svelte';
	import Button from '$lib/components/ui/Button.svelte';
	import Input from '$lib/components/ui/Input.svelte';

	let { data }: { data: PageData } = $props();

	let name = $state('');
	let account_type = $state('Asset');
	let error: string | null = $state(null);
	let isAdding = $state(false);

	// Derived state
	let assets = $derived(data.accounts.filter((a: any) => a.account_type === 'Asset'));
	let liabilities = $derived(data.accounts.filter((a: any) => a.account_type === 'Liability'));
	
	let totalAssets = $derived(assets.reduce((sum: number, a: any) => sum + a.balance, 0));
	let totalLiabilities = $derived(liabilities.reduce((sum: number, a: any) => sum + a.balance, 0));
	let netWorth = $derived(totalAssets - totalLiabilities);

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
			isAdding = false;
			await invalidateAll();
		} else {
			const err = await res.json();
			error = err.detail || 'Failed to create account.';
		}
	}

	async function deleteAccount(id: string) {
		if (!confirm('Are you sure you want to delete this account?')) return;
		
		const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/accounts/${id}`, {
			method: 'DELETE'
		});

		if (res.ok) {
			await invalidateAll();
		} else {
			alert('Failed to delete account');
		}
	}
</script>

<div class="space-y-8">
	<!-- Header & Stats -->
	<div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
		<div>
			<h1 class="text-3xl font-bold text-gray-900">Accounts</h1>
			<p class="text-gray-500 mt-1">Manage your assets and liabilities.</p>
		</div>
		<div class="flex gap-6 text-right">
			<div>
				<p class="text-xs text-gray-500 uppercase tracking-wider">Assets</p>
				<p class="text-xl font-semibold text-green-600">${totalAssets.toFixed(2)}</p>
			</div>
			<div>
				<p class="text-xs text-gray-500 uppercase tracking-wider">Liabilities</p>
				<p class="text-xl font-semibold text-red-600">${totalLiabilities.toFixed(2)}</p>
			</div>
			<div class="border-l pl-6 border-gray-200">
				<p class="text-xs text-gray-500 uppercase tracking-wider">Net Worth</p>
				<p class="text-2xl font-bold text-indigo-600">${netWorth.toFixed(2)}</p>
			</div>
		</div>
	</div>

	<!-- Add Account Section -->
	{#if isAdding}
		<Card class="p-6 border-indigo-100 ring-4 ring-indigo-50">
			<div class="flex justify-between items-center mb-4">
				<h2 class="text-lg font-semibold text-gray-900">Add New Account</h2>
				<button onclick={() => isAdding = false} class="text-gray-400 hover:text-gray-500">
					<span class="sr-only">Close</span>
					<svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
						<path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
					</svg>
				</button>
			</div>
			{#if error}
				<div class="bg-red-50 text-red-700 p-3 rounded-md text-sm mb-4">{error}</div>
			{/if}
			<form onsubmit={(e) => { e.preventDefault(); createAccount(); }} class="flex flex-col md:flex-row gap-4 items-end">
				<div class="w-full md:w-1/2">
					<label for="name" class="block text-sm font-medium text-gray-700 mb-1">Account Name</label>
					<Input id="name" bind:value={name} placeholder="e.g. Chase Checking" required />
				</div>
				<div class="w-full md:w-1/3">
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
				<div class="w-full md:w-auto">
					<Button type="submit">Create Account</Button>
				</div>
			</form>
		</Card>
	{:else}
		<div class="flex justify-end">
			<Button onclick={() => isAdding = true}>
				<svg class="-ml-1 mr-2 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
					<path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
				</svg>
				Add Account
			</Button>
		</div>
	{/if}

	<div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
		<!-- Assets Column -->
		<div class="space-y-4">
			<h2 class="text-lg font-semibold text-gray-900 flex items-center">
				<span class="bg-green-100 text-green-800 p-1 rounded mr-2">
					<svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
					</svg>
				</span>
				Assets
			</h2>
			{#each assets as account}
				<a href="/transactions?account={account.id}" class="block group">
					<Card class="p-4 flex justify-between items-center hover:shadow-md transition-shadow group-hover:border-indigo-200">
						<div>
							<h3 class="font-medium text-gray-900 group-hover:text-indigo-600 transition-colors">{account.name}</h3>
							<p class="text-2xl font-bold text-gray-900 mt-1">${account.balance.toFixed(2)}</p>
						</div>
						<button 
							onclick={(e) => { e.preventDefault(); e.stopPropagation(); deleteAccount(account.id); }} 
							class="text-gray-400 hover:text-red-600 transition-colors p-2"
						>
							<svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
							</svg>
						</button>
					</Card>
				</a>
			{:else}
				<div class="text-center py-8 bg-gray-50 rounded-lg border border-dashed border-gray-300">
					<p class="text-gray-500">No assets found.</p>
				</div>
			{/each}
		</div>

		<!-- Liabilities Column -->
		<div class="space-y-4">
			<h2 class="text-lg font-semibold text-gray-900 flex items-center">
				<span class="bg-red-100 text-red-800 p-1 rounded mr-2">
					<svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
					</svg>
				</span>
				Liabilities
			</h2>
			{#each liabilities as account}
				<a href="/transactions?account={account.id}" class="block group">
					<Card class="p-4 flex justify-between items-center hover:shadow-md transition-shadow group-hover:border-indigo-200">
						<div>
							<h3 class="font-medium text-gray-900 group-hover:text-indigo-600 transition-colors">{account.name}</h3>
							<p class="text-2xl font-bold text-gray-900 mt-1">${account.balance.toFixed(2)}</p>
						</div>
						<button 
							onclick={(e) => { e.preventDefault(); e.stopPropagation(); deleteAccount(account.id); }} 
							class="text-gray-400 hover:text-red-600 transition-colors p-2"
						>
							<svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
							</svg>
						</button>
					</Card>
				</a>
			{:else}
				<div class="text-center py-8 bg-gray-50 rounded-lg border border-dashed border-gray-300">
					<p class="text-gray-500">No liabilities found.</p>
				</div>
			{/each}
		</div>
	</div>
</div>
