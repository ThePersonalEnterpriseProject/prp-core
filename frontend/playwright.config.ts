import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
    webServer: {
        command: 'npm run build && npm run preview',
        port: 4173,
        reuseExistingServer: !process.env.CI
    },
    testDir: 'tests/e2e',
    testMatch: /(.+\.)?(test|spec)\.[jt]s/,
    outputDir: 'test-results',
    use: {
        baseURL: process.env.PUBLIC_BACKEND_URL || 'http://frontend:5173',
        screenshot: 'on',
        trace: 'retain-on-failure',
    },
    projects: [
        {
            name: 'chromium',
            use: { ...devices['Desktop Chrome'] },
        },
    ],
});
