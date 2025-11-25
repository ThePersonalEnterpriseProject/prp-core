import { test, expect } from '@playwright/test';

test.describe('README Screenshots', () => {
    test('capture screenshots', async ({ page }) => {
        // Dashboard
        await page.goto('/');
        await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
        await page.screenshot({ path: '/screenshots/dashboard.png', fullPage: true });

        // Accounts
        await page.goto('/accounts');
        await expect(page.getByRole('heading', { name: 'Accounts' })).toBeVisible();
        await page.screenshot({ path: '/screenshots/accounts.png', fullPage: true });

        // Transactions
        await page.goto('/transactions');
        await expect(page.getByRole('heading', { name: 'Transactions' })).toBeVisible();
        await page.screenshot({ path: '/screenshots/transactions.png', fullPage: true });

        // Assets
        await page.goto('/assets');
        await expect(page.getByRole('heading', { name: 'Assets' })).toBeVisible();
        await page.screenshot({ path: '/screenshots/assets.png', fullPage: true });

        // Planning Dashboard
        await page.goto('/planning');
        await expect(page.getByRole('heading', { name: 'Financial Planning' })).toBeVisible();
        await page.screenshot({ path: '/screenshots/planning_dashboard.png', fullPage: true });

        // Planning - Goals
        await page.goto('/planning/goals');
        await expect(page.getByRole('heading', { name: 'Goals' })).toBeVisible();
        await page.screenshot({ path: '/screenshots/planning_goals.png', fullPage: true });

        // Planning - Budgets
        await page.goto('/planning/budgets');
        await expect(page.getByRole('heading', { name: 'Budgets' })).toBeVisible();
        await page.screenshot({ path: '/screenshots/planning_budgets.png', fullPage: true });

        // Planning - Forecasting
        await page.goto('/planning/forecasting');
        await expect(page.getByRole('heading', { name: 'Forecasting' })).toBeVisible();
        await page.screenshot({ path: '/screenshots/planning_forecasting.png', fullPage: true });

        // Planning - Retirement
        await page.goto('/planning/retirement');
        await expect(page.getByRole('heading', { name: 'Retirement Planning' })).toBeVisible();
        await page.screenshot({ path: '/screenshots/planning_retirement.png', fullPage: true });

        // Planning - Loans
        await page.goto('/planning/loans');
        await expect(page.getByRole('heading', { name: 'Loan Comparison' })).toBeVisible();
        await page.screenshot({ path: '/screenshots/planning_loans.png', fullPage: true });
    });
});
