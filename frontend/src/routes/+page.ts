import { browser } from '$app/environment';
import { PUBLIC_BACKEND_URL } from '$env/static/public';
import type { PageLoad } from './$types';

const backendHost = browser ? PUBLIC_BACKEND_URL : 'http://backend:8000';

export const load: PageLoad = async ({ fetch }) => {
	try {
		const res = await fetch(`${backendHost}/api/v1/accounts/`);
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