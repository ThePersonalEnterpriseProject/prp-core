<script lang="ts">
	import type { PageData } from './$types';
	import { invalidateAll } from '$app/navigation';
	import { PUBLIC_BACKEND_URL } from '$env/static/public';

	export let data: PageData;

	let name = '';
	let account_type = 'Asset';
	let error: string | null = null;

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

<div class="container mx-auto p-8">
	{#if data.error}
		<div class="alert alert-error shadow-lg">
			<div>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					class="stroke-current flex-shrink-0 h-6 w-6"
					fill="none"
					viewBox="0 0 24 24"
					><path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
					/></svg
				>
				<span>{data.error}</span>
			</div>
		</div>
	{:else}
		<h1 class="text-4xl font-bold mb-8">Net Worth: ${data.netWorth.toFixed(2)}</h1>

		<div class="mb-8">
			<h2 class="text-2xl font-bold mb-4">Create Account</h2>
			{#if error}
				<div class="alert alert-warning shadow-lg mb-4">
					<div>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="stroke-current flex-shrink-0 h-6 w-6"
							fill="none"
							viewBox="0 0 24 24"
							><path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
							/></svg
						>
						<span>{error}</span>
					</div>
				</div>
			{/if}
			<form on:submit|preventDefault={createAccount} class="flex gap-4">
				<input
					type="text"
					bind:value={name}
					placeholder="Account Name"
					class="input input-bordered w-full max-w-xs"
				/>
				<select bind:value={account_type} class="select select-bordered">
					<option>Asset</option>
					<option>Liability</option>
				</select>
				<button type="submit" class="btn btn-primary">Create</button>
			</form>
		</div>

		<div>
			<h2 class="text-2xl font-bold mb-4">Accounts</h2>
			<div class="overflow-x-auto">
				<table class="table w-full">
					<thead>
						<tr>
							<th>Name</th>
							<th>Type</th>
							<th>Balance</th>
						</tr>
					</thead>
					<tbody>
						{#each data.accounts as account}
							<tr>
								<td>{account.name}</td>
								<td>{account.account_type}</td>
								<td>${account.balance.toFixed(2)}</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		</div>
	{/if}
</div>
