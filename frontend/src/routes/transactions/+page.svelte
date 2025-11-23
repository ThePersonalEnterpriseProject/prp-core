<script lang="ts">
	import type { PageData } from './$types';
	import { invalidateAll } from '$app/navigation';
	import { PUBLIC_BACKEND_URL } from '$env/static/public';
	import Card from '$lib/components/ui/Card.svelte';
	import Button from '$lib/components/ui/Button.svelte';
	import Input from '$lib/components/ui/Input.svelte';

	import { page } from '$app/stores';
	import { onMount } from 'svelte';

	let { data }: { data: PageData } = $props();

	let description = $state('');
	let amount = $state('');
	let account_id = $state('');
	let error: string | null = $state(null);
	let isAdding = $state(false);
	let selectedAccountFilter = $state('');

	// Initialize filter from URL
	onMount(() => {
		const accountParam = $page.url.searchParams.get('account');
		if (accountParam) {
			selectedAccountFilter = accountParam;
		}
	});

	// Derived state
	let filteredTransactions = $derived(
		data.transactions.filter((t: any) => 
			selectedAccountFilter ? t.account_id === selectedAccountFilter : true
		)
	);

	// Sort transactions by date (newest first)
	let sortedTransactions = $derived([...filteredTransactions].sort((a: any, b: any) => 
		new Date(b.date).getTime() - new Date(a.date).getTime()
	));

	async function createTransaction() {
		error = null;
		if (!account_id) {
			error = 'Please select an account.';
			return;
		}

		const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/transactions/`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				description,
				amount: parseFloat(amount),
				account_id
			})
		});

		if (res.ok) {
			description = '';
			amount = '';
			account_id = '';
			isAdding = false;
			await invalidateAll();
		} else {
			const err = await res.json();
			error = err.detail || 'Failed to create transaction.';
		}
	}

	async function deleteTransaction(id: string) {
		if (!confirm('Are you sure you want to delete this transaction?')) return;
		
		const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/transactions/${id}`, {
			method: 'DELETE'
		});

		if (res.ok) {
			await invalidateAll();
		} else {
			alert('Failed to delete transaction');
		}
	}

	function formatDate(dateString: string) {
		return new Date(dateString).toLocaleDateString('en-US', {
			year: 'numeric',
			month: 'short',
			day: 'numeric'
		});
	}
</script>

<div class="space-y-8">
	<!-- Header -->
	<div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
		<div>
			<h1 class="text-3xl font-bold text-gray-900">Transactions</h1>
			<p class="text-gray-500 mt-1">View and categorize your financial activity.</p>
		</div>
		<div class="flex gap-4">
			<select
				bind:value={selectedAccountFilter}
				class="rounded-md border border-gray-300 bg-white px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
			>
				<option value="">All Accounts</option>
				{#each data.accounts as account}
					<option value={account.id}>{account.name}</option>
				{/each}
			</select>
			{#if !isAdding}
				<Button onclick={() => isAdding = true}>
					<svg class="-ml-1 mr-2 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
						<path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
					</svg>
					Add Transaction
				</Button>
			{/if}
		</div>
	</div>

	<!-- Add Transaction Form -->
	{#if isAdding}
		<Card class="p-6 border-indigo-100 ring-4 ring-indigo-50">
			<div class="flex justify-between items-center mb-4">
				<h2 class="text-lg font-semibold text-gray-900">Add New Transaction</h2>
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
			<form onsubmit={(e) => { e.preventDefault(); createTransaction(); }} class="grid grid-cols-1 md:grid-cols-4 gap-4 items-end">
				<div class="md:col-span-2">
					<label for="description" class="block text-sm font-medium text-gray-700 mb-1">Description</label>
					<Input id="description" bind:value={description} placeholder="e.g. Grocery Store" required />
				</div>
				<div>
					<label for="amount" class="block text-sm font-medium text-gray-700 mb-1">Amount</label>
					<Input id="amount" type="number" step="0.01" bind:value={amount} placeholder="0.00" required />
				</div>
				<div>
					<label for="account" class="block text-sm font-medium text-gray-700 mb-1">Account</label>
					<select
						id="account"
						bind:value={account_id}
						class="flex h-10 w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
						required
					>
						<option value="" disabled selected>Select Account</option>
						{#each data.accounts as account}
							<option value={account.id}>{account.name}</option>
						{/each}
					</select>
				</div>
				<div class="md:col-span-4 flex justify-end mt-2">
					<Button type="submit">Save Transaction</Button>
				</div>
			</form>
		</Card>
	{/if}

	<!-- Transactions Table -->
	<Card class="overflow-hidden">
		<div class="overflow-x-auto">
			<table class="w-full text-left text-sm">
				<thead class="bg-gray-50 text-gray-500 border-b border-gray-100">
					<tr>
						<th class="px-6 py-3 font-medium">Date</th>
						<th class="px-6 py-3 font-medium">Description</th>
						<th class="px-6 py-3 font-medium">Account</th>
						<th class="px-6 py-3 font-medium text-right">Amount</th>
						<th class="px-6 py-3 font-medium text-right">Actions</th>
					</tr>
				</thead>
				<tbody class="divide-y divide-gray-100">
					{#each sortedTransactions as transaction}
						<tr class="hover:bg-gray-50 transition-colors">
							<td class="px-6 py-4 text-gray-500 whitespace-nowrap">{formatDate(transaction.date)}</td>
							<td class="px-6 py-4 font-medium text-gray-900">{transaction.description}</td>
							<td class="px-6 py-4 text-gray-500">{transaction.account_name}</td>
							<td class="px-6 py-4 text-right font-medium {transaction.amount > 0 ? 'text-green-600' : 'text-gray-900'}">
								${transaction.amount.toFixed(2)}
							</td>
							<td class="px-6 py-4 text-right">
								<button onclick={() => deleteTransaction(transaction.id)} class="text-gray-400 hover:text-red-600 transition-colors">
									<svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
										<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
									</svg>
								</button>
							</td>
						</tr>
					{:else}
						<tr>
							<td colspan="5" class="px-6 py-12 text-center text-gray-500">
								No transactions found. Add one to get started!
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</Card>
</div>
