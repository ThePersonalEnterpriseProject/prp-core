import { env } from '$env/dynamic/private';
import { PUBLIC_BACKEND_URL } from '$env/static/public';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch }) => {
    const baseUrl = env.INTERNAL_BACKEND_URL || PUBLIC_BACKEND_URL;
    console.log(`Fetching goals from: ${baseUrl}/api/v1/planning/goals/`);

    try {
        const res = await fetch(`${baseUrl}/api/v1/planning/goals/`);
        if (!res.ok) {
            console.error(`Failed to fetch goals: ${res.status} ${res.statusText}`);
            return { goals: [] };
        }
        const goals = await res.json();
        return { goals };
    } catch (e) {
        console.error('Error fetching goals:', e);
        return { goals: [] };
    }
};
