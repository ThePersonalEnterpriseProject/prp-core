import { env } from '$env/dynamic/private';
import { PUBLIC_BACKEND_URL } from '$env/static/public';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch }) => {
    const baseUrl = env.INTERNAL_BACKEND_URL || PUBLIC_BACKEND_URL;

    try {
        const res = await fetch(`${baseUrl}/api/v1/planning/forecasts/`);
        if (!res.ok) {
            console.error(`Failed to fetch forecasts: ${res.status} ${res.statusText}`);
            return { scenarios: [] };
        }
        const scenarios = await res.json();
        return { scenarios };
    } catch (e) {
        console.error('Error fetching forecasts:', e);
        return { scenarios: [] };
    }
};
