import { env } from '$env/dynamic/private';
import { PUBLIC_BACKEND_URL } from '$env/static/public';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch }) => {
    const baseUrl = env.INTERNAL_BACKEND_URL || PUBLIC_BACKEND_URL;

    try {
        const res = await fetch(`${baseUrl}/api/v1/planning/retirement/`);
        if (!res.ok) {
            console.error(`Failed to fetch retirement plans: ${res.status} ${res.statusText}`);
            return { plans: [] };
        }
        const plans = await res.json();
        return { plans };
    } catch (e) {
        console.error('Error fetching retirement plans:', e);
        return { plans: [] };
    }
};
