import { env } from '$env/dynamic/private';
import { PUBLIC_BACKEND_URL } from '$env/static/public';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch }) => {
    const baseUrl = env.INTERNAL_BACKEND_URL || PUBLIC_BACKEND_URL;
    console.log(`Fetching budgets from: ${baseUrl}/api/v1/planning/budgets/`);

    try {
        const res = await fetch(`${baseUrl}/api/v1/planning/budgets/`);
        if (!res.ok) {
            console.error(`Failed to fetch budgets: ${res.status} ${res.statusText}`);
            return { budgets: [] };
        }
        const budgets = await res.json();
        return { budgets };
    } catch (e) {
        console.error('Error fetching budgets:', e);
        return { budgets: [] };
    }
};
