<script lang="ts">
	import { onMount } from 'svelte';
	import { PUBLIC_BACKEND_URL } from '$env/static/public';
	import Card from '$lib/components/ui/Card.svelte';
	import Button from '$lib/components/ui/Button.svelte';
	import Input from '$lib/components/ui/Input.svelte';

	interface Asset {
		id: string;
		name: string;
		description: string | null;
		type: string;
		value: number;
		location: string | null;
		purchase_date: string | null;
		created_at: string;
	}

	let assets = $state<Asset[]>([]);
	let loading = $state(true);
	let showForm = $state(false);
	let error = $state<string | null>(null);

	// Form state
	let newAsset = $state({
		name: '',
		description: '',
		type: 'General',
		value: 0,
		location: ''
	});

	async function fetchAssets() {
		try {
			const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/assets/`);
			if (res.ok) {
				assets = await res.json();
			} else {
				error = 'Failed to load assets';
			}
		} catch (e) {
			error = 'Network error';
		} finally {
			loading = false;
		}
	}

	async function handleSubmit(e: Event) {
		e.preventDefault();
		try {
			const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/assets/`, {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify(newAsset)
			});

			if (res.ok) {
				const created = await res.json();
				assets = [created, ...assets];
				showForm = false;
				// Reset form
				newAsset = { name: '', description: '', type: 'General', value: 0, location: '' };
			} else {
				alert('Failed to create asset');
			}
		} catch (e) {
			alert('Error creating asset');
		}
	}

	onMount(fetchAssets);
</script>

<div class="space-y-6">
	<div class="flex justify-between items-center">
		<div>
			<h1 class="text-3xl font-bold text-gray-900">Assets</h1>
			<p class="text-gray-500 mt-1">Track your physical assets and inventory.</p>
		</div>
		<Button onclick={() => showForm = !showForm}>
			{showForm ? 'Cancel' : 'Add Asset'}
		</Button>
	</div>

	{#if showForm}
		<Card class="p-6">
			<h2 class="text-lg font-semibold mb-4">New Asset</h2>
			<form onsubmit={handleSubmit} class="space-y-4">
				<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
					<Input label="Name" bind:value={newAsset.name} required placeholder="e.g. Ford F-150" />
					<Input label="Type" bind:value={newAsset.type} required placeholder="e.g. Vehicle" />
					<Input label="Value ($)" type="number" bind:value={newAsset.value} required min="0" step="0.01" />
					<Input label="Location" bind:value={newAsset.location} placeholder="e.g. Garage" />
					<div class="md:col-span-2">
						<Input label="Description" bind:value={newAsset.description} placeholder="Optional details..." />
					</div>
				</div>
				<div class="flex justify-end">
					<Button type="submit">Save Asset</Button>
				</div>
			</form>
		</Card>
	{/if}

	{#if loading}
		<div class="text-center py-12">
			<div class="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600 mx-auto"></div>
			<p class="mt-4 text-gray-500">Loading assets...</p>
		</div>
	{:else if error}
		<div class="bg-red-50 text-red-700 p-4 rounded-lg">
			{error}
		</div>
	{:else if assets.length === 0}
		<div class="text-center py-12 bg-gray-50 rounded-lg border-2 border-dashed border-gray-200">
			<p class="text-gray-500">No assets found. Add one to get started!</p>
		</div>
	{:else}
		<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
			{#each assets as asset}
				<Card class="p-6 hover:shadow-md transition-shadow">
					<div class="flex justify-between items-start mb-4">
						<div>
							<h3 class="font-semibold text-lg text-gray-900">{asset.name}</h3>
							<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-indigo-100 text-indigo-800">
								{asset.type}
							</span>
						</div>
						<div class="text-lg font-bold text-gray-900">
							${asset.value.toLocaleString()}
						</div>
					</div>
					
					{#if asset.description}
						<p class="text-gray-600 text-sm mb-4">{asset.description}</p>
					{/if}

					<div class="flex items-center text-sm text-gray-500 gap-4">
						{#if asset.location}
							<div class="flex items-center gap-1">
								<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
									<path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" />
								</svg>
								{asset.location}
							</div>
						{/if}
					</div>
				</Card>
			{/each}
		</div>
	{/if}
</div>
