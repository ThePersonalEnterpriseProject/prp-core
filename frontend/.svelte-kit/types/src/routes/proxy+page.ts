// @ts-nocheck
import type { PageLoad } from './$types';

export const load = async ({ fetch }: Parameters<PageLoad>[0]) => {
	try {
		const res = await fetch('http://localhost:8000/api/v1/accounts');
		if (!res.ok) {
			console.error('Failed to fetch accounts:', res.status, res.statusText);
			return {
				accounts: [],
				netWorth: 0,
				error: 'Failed to load accounts. Is the backend running?'
			};
		}
		const accounts = await res.json();

		const assets = accounts.filter((acc: any) => acc.account_type === 'Asset');
		const liabilities = accounts.filter((acc: any) => acc.account_type === 'Liability');

		const totalAssets = assets.reduce((sum: number, acc: any) => sum + acc.balance, 0);
		const totalLiabilities = liabilities.reduce((sum: number, acc: any) => sum + acc.balance, 0);

		const netWorth = totalAssets - totalLiabilities;

		return {
			accounts,
			netWorth
		};
	} catch (e) {
		console.error('Error fetching accounts:', e);
		return {
			accounts: [],
			netWorth: 0,
			error: 'Failed to connect to the backend.'
		};
	}
};