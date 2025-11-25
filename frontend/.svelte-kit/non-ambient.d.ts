
// this file is generated — do not edit it


declare module "svelte/elements" {
	export interface HTMLAttributes<T> {
		'data-sveltekit-keepfocus'?: true | '' | 'off' | undefined | null;
		'data-sveltekit-noscroll'?: true | '' | 'off' | undefined | null;
		'data-sveltekit-preload-code'?:
			| true
			| ''
			| 'eager'
			| 'viewport'
			| 'hover'
			| 'tap'
			| 'off'
			| undefined
			| null;
		'data-sveltekit-preload-data'?: true | '' | 'hover' | 'tap' | 'off' | undefined | null;
		'data-sveltekit-reload'?: true | '' | 'off' | undefined | null;
		'data-sveltekit-replacestate'?: true | '' | 'off' | undefined | null;
	}
}

export {};


declare module "$app/types" {
	export interface AppTypes {
		RouteId(): "/" | "/accounts" | "/assets" | "/planning" | "/planning/budgets" | "/planning/forecasting" | "/planning/goals" | "/planning/loans" | "/planning/retirement" | "/settings" | "/transactions";
		RouteParams(): {
			
		};
		LayoutParams(): {
			"/": Record<string, never>;
			"/accounts": Record<string, never>;
			"/assets": Record<string, never>;
			"/planning": Record<string, never>;
			"/planning/budgets": Record<string, never>;
			"/planning/forecasting": Record<string, never>;
			"/planning/goals": Record<string, never>;
			"/planning/loans": Record<string, never>;
			"/planning/retirement": Record<string, never>;
			"/settings": Record<string, never>;
			"/transactions": Record<string, never>
		};
		Pathname(): "/" | "/accounts" | "/accounts/" | "/assets" | "/assets/" | "/planning" | "/planning/" | "/planning/budgets" | "/planning/budgets/" | "/planning/forecasting" | "/planning/forecasting/" | "/planning/goals" | "/planning/goals/" | "/planning/loans" | "/planning/loans/" | "/planning/retirement" | "/planning/retirement/" | "/settings" | "/settings/" | "/transactions" | "/transactions/";
		ResolvedPathname(): `${"" | `/${string}`}${ReturnType<AppTypes['Pathname']>}`;
		Asset(): "/robots.txt" | string & {};
	}
}