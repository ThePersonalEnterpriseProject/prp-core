<script lang="ts">
  import type { PageData } from './$types';
  import { invalidateAll } from '$app/navigation';
  import { PUBLIC_BACKEND_URL } from '$env/static/public';
  import Card from '$lib/components/ui/Card.svelte';
  import Button from '$lib/components/ui/Button.svelte';
  import Input from '$lib/components/ui/Input.svelte';

  let { data }: { data: PageData } = $props();

  let name = $state('');
  let target_amount = $state('');
  let deadline = $state('');
  let error: string | null = $state(null);
  let isAdding = $state(false);

  let goals = $derived(data.goals);

  async function createGoal() {
    error = null;
    const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/planning/goals/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name,
        target_amount: parseFloat(target_amount),
        deadline: deadline ? new Date(deadline).toISOString() : null
      })
    });

    if (res.ok) {
      name = '';
      target_amount = '';
      deadline = '';
      isAdding = false;
      await invalidateAll();
    } else {
      const err = await res.json();
      error = err.detail || 'Failed to create goal.';
    }
  }

  async function deleteGoal(id: string) {
    if (!confirm('Are you sure you want to delete this goal?')) return;

    const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/planning/goals/${id}`, {
      method: 'DELETE'
    });

    if (res.ok) {
      await invalidateAll();
    } else {
      alert('Failed to delete goal');
    }
  }
</script>

<div class="space-y-8">
  <div class="flex items-center justify-between">
    <div>
      <h1 class="text-3xl font-bold text-gray-900 dark:text-white">Financial Goals</h1>
      <p class="mt-1 text-gray-500 dark:text-gray-400">Track your savings targets.</p>
    </div>
  </div>

  {#if isAdding}
    <Card class="p-6 border-indigo-100 ring-4 ring-indigo-50 dark:ring-indigo-900/20">
      <div class="flex items-center justify-between mb-4">
        <h2 class="text-lg font-semibold text-gray-900 dark:text-white">Add New Goal</h2>
        <button onclick={() => isAdding = false} class="text-gray-400 hover:text-gray-500">
          <span class="sr-only">Close</span>
          <svg class="w-5 h-5" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
          </svg>
        </button>
      </div>
      {#if error}
        <div class="p-3 mb-4 text-sm text-red-700 rounded-md bg-red-50">{error}</div>
      {/if}
      <form onsubmit={(e) => { e.preventDefault(); createGoal(); }} class="grid grid-cols-1 gap-4 md:grid-cols-3 items-end">
        <div>
          <label for="name" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Goal Name</label>
          <Input id="name" bind:value={name} placeholder="e.g. Emergency Fund" required />
        </div>
        <div>
          <label for="amount" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Target Amount</label>
          <Input id="amount" type="number" step="0.01" bind:value={target_amount} placeholder="10000.00" required />
        </div>
        <div>
          <label for="deadline" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Deadline (Optional)</label>
          <Input id="deadline" type="date" bind:value={deadline} />
        </div>
        <div class="md:col-span-3 flex justify-end">
          <Button type="submit">Create Goal</Button>
        </div>
      </form>
    </Card>
  {:else}
    <div class="flex justify-end">
      <Button onclick={() => isAdding = true}>
        <svg class="w-5 h-5 mr-2 -ml-1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
        </svg>
        Add Goal
      </Button>
    </div>
  {/if}

  <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
    {#each goals as goal}
      <Card class="flex flex-col justify-between p-6">
        <div>
          <div class="flex items-start justify-between">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">{goal.name}</h3>
            <button 
              onclick={() => deleteGoal(goal.id)} 
              class="text-gray-400 transition-colors hover:text-red-600"
            >
              <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
            </button>
          </div>
          <div class="mt-4">
            <p class="text-sm text-gray-500 dark:text-gray-400">Target</p>
            <p class="text-2xl font-bold text-indigo-600 dark:text-indigo-400">${goal.target_amount.toLocaleString()}</p>
          </div>
          <div class="mt-4">
            <p class="text-sm text-gray-500 dark:text-gray-400">Current Progress</p>
            <div class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700 mt-1">
              <div class="bg-indigo-600 h-2.5 rounded-full" style="width: {Math.min((goal.current_amount / goal.target_amount) * 100, 100)}%"></div>
            </div>
            <p class="text-xs text-right mt-1 text-gray-500">{((goal.current_amount / goal.target_amount) * 100).toFixed(1)}%</p>
          </div>
          {#if goal.deadline}
            <div class="mt-4 text-sm text-gray-500">
              Deadline: {new Date(goal.deadline).toLocaleDateString()}
            </div>
          {/if}
        </div>
      </Card>
    {:else}
      <div class="col-span-full py-12 text-center bg-gray-50 border border-gray-300 border-dashed rounded-lg dark:bg-gray-800 dark:border-gray-700">
        <p class="text-gray-500 dark:text-gray-400">No goals found. Create one to get started!</p>
      </div>
    {/each}
  </div>
</div>
