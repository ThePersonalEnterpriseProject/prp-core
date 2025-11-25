<script lang="ts">
  import Card from "$lib/components/ui/Card.svelte";
  import Button from "$lib/components/ui/Button.svelte";
</script>

<div class="space-y-6">
  <div class="flex items-center justify-between">
    <h1 class="text-3xl font-bold text-gray-900 dark:text-white">Financial Planning</h1>
  </div>

  <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
    <!-- Goals -->
    <Card title="Goals">
      <p class="mb-4 text-gray-600 dark:text-gray-400">
        Track your savings targets and financial objectives.
      </p>
      <Button href="/planning/goals" variant="primary" fullWidth>Manage Goals</Button>
    </Card>

    <!-- Budgets -->
    <Card title="Budgets">
      <p class="mb-4 text-gray-600 dark:text-gray-400">
        Set spending limits and monitor your expenses.
      </p>
      <Button href="/planning/budgets" variant="primary" fullWidth>Manage Budgets</Button>
    </Card>

    <!-- Forecasting -->
    <Card title="Forecasting">
      <p class="mb-4 text-gray-600 dark:text-gray-400">
        Project your net worth growth over time.
      </p>
      <Button href="/planning/forecasting" variant="secondary" fullWidth>Run Forecast</Button>
    </Card>

    <!-- Retirement -->
    <Card title="Retirement">
      <p class="mb-4 text-gray-600 dark:text-gray-400">
        Analyze your retirement readiness and savings needs.
      </p>
      <Button href="/planning/retirement" variant="secondary" fullWidth>Plan Retirement</Button>
    </Card>

    <!-- Loans -->
    <Card title="Loan Comparison">
      <p class="mb-4 text-gray-600 dark:text-gray-400">
        Compare mortgage and loan scenarios side-by-side.
      </p>
      <Button href="/planning/loans" variant="secondary" fullWidth>Compare Loans</Button>
    </Card>
  </div>
</div>
