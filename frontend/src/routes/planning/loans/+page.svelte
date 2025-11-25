<script lang="ts">
  import type { PageData } from './$types';
  import { invalidateAll } from '$app/navigation';
  import { PUBLIC_BACKEND_URL } from '$env/static/public';
  import Card from '$lib/components/ui/Card.svelte';
  import Button from '$lib/components/ui/Button.svelte';
  import Input from '$lib/components/ui/Input.svelte';

  let { data }: { data: PageData } = $props();

  let name = $state('');
  let principal = $state('');
  let interest_rate = $state('');
  let term_years = $state('');
  let down_payment = $state('');
  let extra_monthly_payment = $state('');
  
  let error: string | null = $state(null);
  let isAdding = $state(false);
  
  let scenarios = $derived(data.scenarios);
  let selectedScenarioIds: string[] = $state([]);
  let comparisonResults: any[] = $state([]);
  let isLoadingComparison = $state(false);

  async function createScenario() {
    error = null;
    const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/planning/loans/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name,
        principal: parseFloat(principal),
        interest_rate: parseFloat(interest_rate) / 100,
        term_years: parseInt(term_years),
        down_payment: parseFloat(down_payment || '0'),
        extra_monthly_payment: parseFloat(extra_monthly_payment || '0')
      })
    });

    if (res.ok) {
      name = '';
      principal = '';
      interest_rate = '';
      term_years = '';
      down_payment = '';
      extra_monthly_payment = '';
      isAdding = false;
      await invalidateAll();
    } else {
      const err = await res.json();
      error = err.detail || 'Failed to create scenario.';
    }
  }

  function toggleSelection(id: string) {
    if (selectedScenarioIds.includes(id)) {
        selectedScenarioIds = selectedScenarioIds.filter(s => s !== id);
    } else {
        selectedScenarioIds = [...selectedScenarioIds, id];
    }
  }

  async function compareLoans() {
    if (selectedScenarioIds.length === 0) return;
    
    isLoadingComparison = true;
    comparisonResults = [];
    try {
        const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/planning/loans/compare`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(selectedScenarioIds)
        });
        if (res.ok) {
            comparisonResults = await res.json();
        } else {
            alert('Failed to compare loans');
        }
    } catch (e) {
        console.error(e);
        alert('Error comparing loans');
    } finally {
        isLoadingComparison = false;
    }
  }
</script>

<div class="space-y-8">
  <div class="flex items-center justify-between">
    <div>
      <h1 class="text-3xl font-bold text-gray-900 dark:text-white">Loan Comparison</h1>
      <p class="mt-1 text-gray-500 dark:text-gray-400">Compare mortgage and loan options.</p>
    </div>
  </div>

  {#if isAdding}
    <Card class="p-6 border-indigo-100 ring-4 ring-indigo-50 dark:ring-indigo-900/20">
      <div class="flex items-center justify-between mb-4">
        <h2 class="text-lg font-semibold text-gray-900 dark:text-white">Add New Scenario</h2>
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
      <form onsubmit={(e) => { e.preventDefault(); createScenario(); }} class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3 items-end">
        <div class="lg:col-span-3">
          <label for="name" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Scenario Name</label>
          <Input id="name" bind:value={name} placeholder="e.g. 30-Year Fixed" required />
        </div>
        
        <div>
          <label for="principal" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Principal Amount</label>
          <Input id="principal" type="number" step="100" bind:value={principal} placeholder="300000" required />
        </div>
        <div>
          <label for="rate" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Interest Rate (%)</label>
          <Input id="rate" type="number" step="0.01" bind:value={interest_rate} placeholder="6.5" required />
        </div>
        <div>
          <label for="term" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Term (Years)</label>
          <Input id="term" type="number" bind:value={term_years} placeholder="30" required />
        </div>
        
        <div>
          <label for="down_payment" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Down Payment (Optional)</label>
          <Input id="down_payment" type="number" step="100" bind:value={down_payment} placeholder="60000" />
        </div>
        <div>
          <label for="extra" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Extra Monthly Payment (Optional)</label>
          <Input id="extra" type="number" step="10" bind:value={extra_monthly_payment} placeholder="100" />
        </div>

        <div class="lg:col-span-3 flex justify-end">
          <Button type="submit">Create Scenario</Button>
        </div>
      </form>
    </Card>
  {:else}
    <div class="flex justify-end">
      <Button onclick={() => isAdding = true}>
        <svg class="w-5 h-5 mr-2 -ml-1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
        </svg>
        Add Scenario
      </Button>
    </div>
  {/if}

  <div class="grid grid-cols-1 gap-6 lg:grid-cols-3">
    <!-- Scenarios List -->
    <div class="space-y-4">
        <div class="flex items-center justify-between">
            <h2 class="text-lg font-semibold text-gray-900 dark:text-white">Saved Scenarios</h2>
            {#if selectedScenarioIds.length > 0}
                <Button size="sm" variant="primary" onclick={compareLoans}>Compare ({selectedScenarioIds.length})</Button>
            {/if}
        </div>
        {#each scenarios as scenario}
            <div 
                class="relative p-4 bg-white border rounded-lg shadow-sm cursor-pointer transition-all hover:shadow-md dark:bg-gray-800 dark:border-gray-700"
                class:ring-2={selectedScenarioIds.includes(scenario.id)}
                class:ring-indigo-500={selectedScenarioIds.includes(scenario.id)}
                onclick={() => toggleSelection(scenario.id)}
            >
                <div class="flex justify-between items-start">
                    <div>
                        <h3 class="font-medium text-gray-900 dark:text-white">{scenario.name}</h3>
                        <p class="text-sm text-gray-500">${scenario.principal.toLocaleString()} @ {(scenario.interest_rate * 100).toFixed(2)}%</p>
                    </div>
                    <span class="text-xs bg-gray-100 text-gray-800 px-2 py-1 rounded-full dark:bg-gray-700 dark:text-gray-300">{scenario.term_years} Years</span>
                </div>
                <!-- Checkbox indicator -->
                <div class="absolute top-4 right-4">
                    {#if selectedScenarioIds.includes(scenario.id)}
                        <svg class="w-5 h-5 text-indigo-600" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                    {:else}
                        <div class="w-5 h-5 border-2 border-gray-300 rounded-full"></div>
                    {/if}
                </div>
            </div>
        {:else}
            <p class="text-gray-500 text-sm">No loan scenarios created yet.</p>
        {/each}
    </div>

    <!-- Results Area -->
    <div class="lg:col-span-2">
        {#if isLoadingComparison}
            <div class="flex justify-center items-center h-64 bg-gray-50 rounded-lg border border-gray-200">
                <p class="text-gray-500">Comparing scenarios...</p>
            </div>
        {:else if comparisonResults.length > 0}
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                {#each comparisonResults as result}
                    {@const scenario = scenarios.find(s => s.id === result.scenario_id)}
                    <Card class="p-6 border-t-4 border-indigo-500">
                        <h3 class="text-lg font-bold text-gray-900 mb-4">{scenario?.name}</h3>
                        
                        <div class="space-y-4">
                            <div>
                                <p class="text-sm text-gray-500">Monthly Payment</p>
                                <p class="text-2xl font-bold text-gray-900">${result.monthly_payment.toLocaleString()}</p>
                            </div>
                            
                            <div class="pt-4 border-t border-gray-100">
                                <div class="flex justify-between mb-2">
                                    <span class="text-sm text-gray-600">Total Interest</span>
                                    <span class="text-sm font-medium text-red-600">${result.total_interest_paid.toLocaleString()}</span>
                                </div>
                                <div class="flex justify-between mb-2">
                                    <span class="text-sm text-gray-600">Total Cost</span>
                                    <span class="text-sm font-medium text-gray-900">${result.total_cost.toLocaleString()}</span>
                                </div>
                                <div class="flex justify-between">
                                    <span class="text-sm text-gray-600">Payoff Date</span>
                                    <span class="text-sm font-medium text-gray-900">{new Date(result.payoff_date).toLocaleDateString()}</span>
                                </div>
                            </div>
                        </div>
                    </Card>
                {/each}
            </div>
        {:else}
            <div class="flex justify-center items-center h-64 bg-gray-50 rounded-lg border border-dashed border-gray-300">
                <p class="text-gray-500">Select scenarios and click "Compare" to view results.</p>
            </div>
        {/if}
    </div>
  </div>
</div>
