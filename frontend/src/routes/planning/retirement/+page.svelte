<script lang="ts">
  import type { PageData } from './$types';
  import { invalidateAll } from '$app/navigation';
  import { PUBLIC_BACKEND_URL } from '$env/static/public';
  import Card from '$lib/components/ui/Card.svelte';
  import Button from '$lib/components/ui/Button.svelte';
  import Input from '$lib/components/ui/Input.svelte';

  let { data }: { data: PageData } = $props();

  let name = $state('');
  let current_age = $state('');
  let retirement_age = $state('');
  let life_expectancy = $state('');
  let desired_annual_income = $state('');
  let expected_return_rate = $state('');
  let current_savings = $state('');
  let annual_contribution = $state('');
  
  let error: string | null = $state(null);
  let isAdding = $state(false);
  
  let plans = $derived(data.plans);
  let analysisResult: any = $state(null);
  let isLoadingAnalysis = $state(false);

  async function createPlan() {
    error = null;
    const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/planning/retirement/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name,
        current_age: parseInt(current_age),
        retirement_age: parseInt(retirement_age),
        life_expectancy: parseInt(life_expectancy),
        desired_annual_income: parseFloat(desired_annual_income),
        expected_return_rate: parseFloat(expected_return_rate) / 100,
        current_savings: parseFloat(current_savings),
        annual_contribution: parseFloat(annual_contribution)
      })
    });

    if (res.ok) {
      name = '';
      current_age = '';
      retirement_age = '';
      life_expectancy = '';
      desired_annual_income = '';
      expected_return_rate = '';
      current_savings = '';
      annual_contribution = '';
      isAdding = false;
      await invalidateAll();
    } else {
      const err = await res.json();
      error = err.detail || 'Failed to create plan.';
    }
  }

  async function analyzePlan(id: string) {
    isLoadingAnalysis = true;
    analysisResult = null;
    try {
        const res = await fetch(`${PUBLIC_BACKEND_URL}/api/v1/planning/retirement/${id}/analyze`, {
            method: 'POST'
        });
        if (res.ok) {
            analysisResult = await res.json();
        } else {
            alert('Failed to analyze plan');
        }
    } catch (e) {
        console.error(e);
        alert('Error analyzing plan');
    } finally {
        isLoadingAnalysis = false;
    }
  }
</script>

<div class="space-y-8">
  <div class="flex items-center justify-between">
    <div>
      <h1 class="text-3xl font-bold text-gray-900 dark:text-white">Retirement Planning</h1>
      <p class="mt-1 text-gray-500 dark:text-gray-400">Analyze your readiness for retirement.</p>
    </div>
  </div>

  {#if isAdding}
    <Card class="p-6 border-indigo-100 ring-4 ring-indigo-50 dark:ring-indigo-900/20">
      <div class="flex items-center justify-between mb-4">
        <h2 class="text-lg font-semibold text-gray-900 dark:text-white">Add New Plan</h2>
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
      <form onsubmit={(e) => { e.preventDefault(); createPlan(); }} class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-4 items-end">
        <div class="lg:col-span-4">
          <label for="name" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Plan Name</label>
          <Input id="name" bind:value={name} placeholder="e.g. Early Retirement" required />
        </div>
        
        <!-- Age & Timeline -->
        <div>
          <label for="current_age" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Current Age</label>
          <Input id="current_age" type="number" bind:value={current_age} placeholder="30" required />
        </div>
        <div>
          <label for="retirement_age" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Retirement Age</label>
          <Input id="retirement_age" type="number" bind:value={retirement_age} placeholder="65" required />
        </div>
        <div>
          <label for="life_expectancy" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Life Expectancy</label>
          <Input id="life_expectancy" type="number" bind:value={life_expectancy} placeholder="90" required />
        </div>
        <div>
          <label for="return_rate" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Exp. Return (%)</label>
          <Input id="return_rate" type="number" step="0.1" bind:value={expected_return_rate} placeholder="5.0" required />
        </div>

        <!-- Financials -->
        <div>
          <label for="current_savings" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Current Savings</label>
          <Input id="current_savings" type="number" step="100" bind:value={current_savings} placeholder="50000" required />
        </div>
        <div>
          <label for="annual_contribution" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Annual Contribution</label>
          <Input id="annual_contribution" type="number" step="100" bind:value={annual_contribution} placeholder="10000" required />
        </div>
        <div class="lg:col-span-2">
          <label for="desired_income" class="block mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">Desired Annual Income (Retirement)</label>
          <Input id="desired_income" type="number" step="100" bind:value={desired_annual_income} placeholder="60000" required />
        </div>

        <div class="lg:col-span-4 flex justify-end">
          <Button type="submit">Create Plan</Button>
        </div>
      </form>
    </Card>
  {:else}
    <div class="flex justify-end">
      <Button onclick={() => isAdding = true}>
        <svg class="w-5 h-5 mr-2 -ml-1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
        </svg>
        Add Plan
      </Button>
    </div>
  {/if}

  <div class="grid grid-cols-1 gap-6 lg:grid-cols-3">
    <!-- Plans List -->
    <div class="space-y-4">
        <h2 class="text-lg font-semibold text-gray-900 dark:text-white">Saved Plans</h2>
        {#each plans as plan}
            <Card class="p-4 hover:shadow-md transition-shadow cursor-pointer" onclick={() => analyzePlan(plan.id)}>
                <div class="flex justify-between items-center">
                    <h3 class="font-medium text-gray-900 dark:text-white">{plan.name}</h3>
                    <span class="text-xs bg-indigo-100 text-indigo-800 px-2 py-1 rounded-full">Age {plan.current_age} -> {plan.retirement_age}</span>
                </div>
                <div class="mt-3">
                    <Button size="sm" variant="secondary" fullWidth onclick={() => analyzePlan(plan.id)}>Analyze</Button>
                </div>
            </Card>
        {:else}
            <p class="text-gray-500 text-sm">No retirement plans created yet.</p>
        {/each}
    </div>

    <!-- Results Area -->
    <div class="lg:col-span-2">
        {#if isLoadingAnalysis}
            <div class="flex justify-center items-center h-64 bg-gray-50 rounded-lg border border-gray-200">
                <p class="text-gray-500">Analyzing plan...</p>
            </div>
        {:else if analysisResult}
            <Card class="p-6">
                <div class="flex items-center justify-between mb-6">
                    <h3 class="text-xl font-bold text-gray-900">Analysis Results</h3>
                    {#if analysisResult.is_on_track}
                        <span class="px-3 py-1 text-sm font-semibold text-green-800 bg-green-100 rounded-full">On Track</span>
                    {:else}
                        <span class="px-3 py-1 text-sm font-semibold text-red-800 bg-red-100 rounded-full">Action Needed</span>
                    {/if}
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="p-4 bg-gray-50 rounded-lg">
                        <p class="text-sm text-gray-500">Projected Savings at Retirement</p>
                        <p class="text-2xl font-bold text-indigo-600">${analysisResult.projected_savings_at_retirement.toLocaleString()}</p>
                    </div>
                    <div class="p-4 bg-gray-50 rounded-lg">
                        <p class="text-sm text-gray-500">Required Savings (4% Rule)</p>
                        <p class="text-2xl font-bold text-gray-900">${analysisResult.required_savings_at_retirement.toLocaleString()}</p>
                    </div>
                </div>

                <div class="mt-6">
                    <p class="text-sm text-gray-500">Surplus / Shortfall</p>
                    <p class="text-3xl font-bold mt-1" class:text-green-600={analysisResult.shortfall_surplus >= 0} class:text-red-600={analysisResult.shortfall_surplus < 0}>
                        {analysisResult.shortfall_surplus >= 0 ? '+' : ''}${analysisResult.shortfall_surplus.toLocaleString()}
                    </p>
                    <p class="text-sm text-gray-500 mt-2">
                        {analysisResult.shortfall_surplus >= 0 
                            ? "Great job! You are projected to have more than enough to cover your desired income." 
                            : "You may need to increase your contributions, retire later, or adjust your expected returns."}
                    </p>
                </div>
            </Card>
        {:else}
            <div class="flex justify-center items-center h-64 bg-gray-50 rounded-lg border border-dashed border-gray-300">
                <p class="text-gray-500">Select a plan to view analysis.</p>
            </div>
        {/if}
    </div>
  </div>
</div>
