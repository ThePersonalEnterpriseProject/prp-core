// @ts-nocheck
import { env } from '$env/dynamic/private';
import { PUBLIC_BACKEND_URL } from '$env/static/public';
import type { PageServerLoad } from './$types';

export const load = async ({ fetch }: Parameters<PageServerLoad>[0]) => {
    const baseUrl = env.INTERNAL_BACKEND_URL || PUBLIC_BACKEND_URL;
    console.log(`Fetching accounts from: ${baseUrl}/api/v1/accounts/`);

    try {
        const res = await fetch(`${baseUrl}/api/v1/accounts/`);
        if (!res.ok) {
            console.error(`Failed to fetch accounts: ${res.status} ${res.statusText}`);
            return { accounts: [] };
        }
        const accounts = await res.json();
        return { accounts };
    } catch (e) {
        console.error('Error fetching accounts:', e);
        return { accounts: [] };
    }
};
