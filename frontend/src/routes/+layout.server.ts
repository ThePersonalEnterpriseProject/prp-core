import { env } from '$env/dynamic/private';

export const load = async ({ fetch }: { fetch: typeof globalThis.fetch }) => {
    const backendUrl = env.INTERNAL_BACKEND_URL || 'http://backend:8000';

    try {
        const response = await fetch(`${backendUrl}/api/v1/modules/`);
        if (response.ok) {
            const modules = await response.json();
            return {
                modules
            };
        }
    } catch (error) {
        console.error('Failed to fetch modules:', error);
    }

    return {
        modules: []
    };
};
