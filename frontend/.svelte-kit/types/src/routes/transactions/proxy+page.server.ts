// @ts-nocheck
import { env } from '$env/dynamic/private';
import { PUBLIC_BACKEND_URL } from '$env/static/public';
import type { PageServerLoad } from './$types';

export const load = async ({ fetch }: Parameters<PageServerLoad>[0]) => {
    const baseUrl = env.INTERNAL_BACKEND_URL || PUBLIC_BACKEND_URL;

    try {
        const [transactionsRes, accountsRes] = await Promise.all([
            fetch(`${baseUrl}/api/v1/transactions/`),
            fetch(`${baseUrl}/api/v1/accounts/`)
        ]);

        if (!transactionsRes.ok || !accountsRes.ok) {
            console.error('Failed to fetch data');
            return { transactions: [], accounts: [] };
        }

        const transactions = await transactionsRes.json();
        const accounts = await accountsRes.json();

        // Enrich transactions with account names
        const enrichedTransactions = transactions.map((t: any) => {
            const account = accounts.find((a: any) => a.id === t.account_id);
            return {
                ...t,
                account_name: account ? account.name : 'Unknown Account'
            };
        });

        return {
            transactions: enrichedTransactions,
            accounts
        };
    } catch (e) {
        console.error('Error fetching data:', e);
        return { transactions: [], accounts: [] };
    }
};
