<script lang="ts">
  import Card from "$lib/components/ui/Card.svelte";
  import Button from "$lib/components/ui/Button.svelte";
  import type { PageData } from './$types';

  export let data: PageData;
  $: budgets = data.budgets;
</script>

<div class="space-y-6">
  <div class="flex items-center justify-between">
    <h1 class="text-3xl font-bold text-gray-900 dark:text-white">Budgets</h1>
    <Button variant="primary">Add Budget</Button>
  </div>

  <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
    {#each budgets as budget}
      <Card title={budget.category}>
        <div class="space-y-2">
          <div class="flex justify-between text-sm">
            <span class="text-gray-500">Limit</span>
            <span class="font-medium">${budget.limit_amount.toLocaleString()}</span>
          </div>
          <div class="flex justify-between text-sm">
            <span class="text-gray-500">Period</span>
            <span class="font-medium capitalize">{budget.period}</span>
          </div>
        </div>
        <div class="mt-4 flex justify-end">
            <Button variant="ghost" size="sm">Edit</Button>
        </div>
      </Card>
    {/each}
    
    {#if budgets.length === 0}
        <div class="col-span-full text-center py-12 bg-gray-50 rounded-lg border-2 border-dashed border-gray-200">
            <p class="text-gray-500">No budgets found. Create one to get started!</p>
        </div>
    {/if}
  </div>
</div>
