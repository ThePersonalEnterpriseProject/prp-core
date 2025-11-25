<script lang="ts">
  import type { PageData } from './$types';
  import { invalidateAll } from '$app/navigation';
  import { PUBLIC_BACKEND_URL } from '$env/static/public';
  import Card from '$lib/components/ui/Card.svelte';
  import Button from '$lib/components/ui/Button.svelte';
  import Input from '$lib/components/ui/Input.svelte';

  let { data }: { data: PageData } = $props();

  let name = $state('');
  let annual_growth_rate = $state('');
  let inflation_rate = $state('');
  let years_to_project = $state('');
  let error: string | null = $state(null);
  let isAdding = $state(false);
  
  let scenarios = $derived(data.scenarios);
  let forecastResult: any = $state(null);
  let isLoadingForecast = $state(false);

  async function createScenario() {
    error = null;
    const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/planning/forecasts/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name,
        annual_growth_rate: parseFloat(annual_growth_rate) / 100, // Convert % to decimal
        inflation_rate: parseFloat(inflation_rate) / 100, // Convert % to decimal
        years_to_project: parseInt(years_to_project)
      })
    });

    if (res.ok) {
      name = '';
      annual_growth_rate = '';
      inflation_rate = '';
      years_to_project = '';
      isAdding = false;
      await invalidateAll();
    } else {
      const err = await res.json();
      error = err.detail || 'Failed to create scenario.';
    }
  }

  async function runForecast(id: string) {
    isLoadingForecast = true;
    forecastResult = null;
    try {
        const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/planning/forecasts/${id}/run`, {
            method: 'POST'
        });
        if (res.ok) {
            forecastResult = await res.json();
        } else {
            alert('Failed to run forecast');
        }
    } catch (e) {
        console.error(e);
        alert('Error running forecast');
    } finally {
        isLoadingForecast = false;
    }
  }
</script>

<div class="space-y-8">
  <div class="flex items-center justify-between">
    <div>
      <h1 class="text-3xl font-bold text-gray-900 dark:text-white">Net Worth Forecasting</h1>
      <p class="mt-1 text-gray-500 dark:text-gray-400">Project your financial future based on growth assumptions.</p>
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
      <form onsubmit={(e) => { e.preventDefault(); createScenario(); }} class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-4 items-end">
        <div class="lg:col-span-2">
          <label for="name" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Scenario Name</label>
          <Input id="name" bind:value={name} placeholder="e.g. Aggressive Growth" required />
        </div>
        <div>
          <label for="growth" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Annual Growth (%)</label>
          <Input id="growth" type="number" step="0.1" bind:value={annual_growth_rate} placeholder="7.0" required />
        </div>
        <div>
          <label for="inflation" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Inflation (%)</label>
          <Input id="inflation" type="number" step="0.1" bind:value={inflation_rate} placeholder="3.0" required />
        </div>
        <div>
          <label for="years" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Years to Project</label>
          <Input id="years" type="number" bind:value={years_to_project} placeholder="10" required />
        </div>
        <div class="lg:col-span-4 flex justify-end">
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
        <h2 class="text-lg font-semibold text-gray-900 dark:text-white">Saved Scenarios</h2>
        {#each scenarios as scenario}
            <Card class="p-4 hover:shadow-md transition-shadow cursor-pointer" onclick={() => runForecast(scenario.id)}>
                <div class="flex justify-between items-center">
                    <h3 class="font-medium text-gray-900 dark:text-white">{scenario.name}</h3>
                    <span class="text-xs bg-indigo-100 text-indigo-800 px-2 py-1 rounded-full">{scenario.years_to_project} Years</span>
                </div>
                <div class="mt-2 text-sm text-gray-500 space-y-1">
                    <p>Growth: {(scenario.annual_growth_rate * 100).toFixed(1)}%</p>
                    <p>Inflation: {(scenario.inflation_rate * 100).toFixed(1)}%</p>
                </div>
                <div class="mt-3">
                    <Button size="sm" variant="secondary" fullWidth onclick={() => runForecast(scenario.id)}>Run Forecast</Button>
                </div>
            </Card>
        {:else}
            <p class="text-gray-500 text-sm">No scenarios created yet.</p>
        {/each}
    </div>

    <!-- Results Area -->
    <div class="lg:col-span-2">
        {#if isLoadingForecast}
            <div class="flex justify-center items-center h-64 bg-gray-50 rounded-lg border border-gray-200">
                <p class="text-gray-500">Calculating projection...</p>
            </div>
        {:else if forecastResult}
            <Card class="p-6">
                <h3 class="text-xl font-bold text-gray-900 mb-4">Forecast Results</h3>
                <div class="overflow-x-auto">
                    <table class="min-w-full divide-y divide-gray-200">
                        <thead class="bg-gray-50">
                            <tr>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Year</th>
                                <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Projected Net Worth</th>
                                <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Inflation Adjusted</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white divide-y divide-gray-200">
                            {#each forecastResult.data as point}
                                <tr>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">Year {point.year}</td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-right font-medium text-green-600">${point.projected_net_worth.toLocaleString()}</td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-right text-gray-500">${point.inflation_adjusted_net_worth.toLocaleString()}</td>
                                </tr>
                            {/each}
                        </tbody>
                    </table>
                </div>
            </Card>
        {:else}
            <div class="flex justify-center items-center h-64 bg-gray-50 rounded-lg border border-dashed border-gray-300">
                <p class="text-gray-500">Select a scenario to view forecast results.</p>
            </div>
        {/if}
    </div>
  </div>
</div>
