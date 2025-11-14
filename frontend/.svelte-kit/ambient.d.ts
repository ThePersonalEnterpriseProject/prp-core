
// this file is generated — do not edit it


/// <reference types="@sveltejs/kit" />

/**
 * Environment variables [loaded by Vite](https://vitejs.dev/guide/env-and-mode.html#env-files) from `.env` files and `process.env`. Like [`$env/dynamic/private`](https://svelte.dev/docs/kit/$env-dynamic-private), this module cannot be imported into client-side code. This module only includes variables that _do not_ begin with [`config.kit.env.publicPrefix`](https://svelte.dev/docs/kit/configuration#env) _and do_ start with [`config.kit.env.privatePrefix`](https://svelte.dev/docs/kit/configuration#env) (if configured).
 * 
 * _Unlike_ [`$env/dynamic/private`](https://svelte.dev/docs/kit/$env-dynamic-private), the values exported from this module are statically injected into your bundle at build time, enabling optimisations like dead code elimination.
 * 
 * ```ts
 * import { API_KEY } from '$env/static/private';
 * ```
 * 
 * Note that all environment variables referenced in your code should be declared (for example in an `.env` file), even if they don't have a value until the app is deployed:
 * 
 * ```
 * MY_FEATURE_FLAG=""
 * ```
 * 
 * You can override `.env` values from the command line like so:
 * 
 * ```sh
 * MY_FEATURE_FLAG="enabled" npm run dev
 * ```
 */
declare module '$env/static/private' {
	export const SHELL: string;
	export const npm_command: string;
	export const COLORTERM: string;
	export const GTK_THEME: string;
	export const PYENV_SHELL: string;
	export const CSF_MDTVTexturesDirectory: string;
	export const HYPRLAND_CMD: string;
	export const XDG_CONFIG_DIRS: string;
	export const npm_config_cache: string;
	export const XDG_SESSION_PATH: string;
	export const NVM_INC: string;
	export const XDG_MENU_PREFIX: string;
	export const XDG_BACKEND: string;
	export const CSF_DrawPluginDefaults: string;
	export const QT_WAYLAND_DISABLE_WINDOWDECORATION: string;
	export const NODE: string;
	export const LC_ADDRESS: string;
	export const CSF_LANGUAGE: string;
	export const XDG_BIN_HOME: string;
	export const LC_NAME: string;
	export const SSH_AUTH_SOCK: string;
	export const CSF_MIGRATION_TYPES: string;
	export const XDG_DATA_HOME: string;
	export const GRADLE_HOME: string;
	export const XDG_CONFIG_HOME: string;
	export const __ABBR_TIPS_VALUES: string;
	export const MEMORY_PRESSURE_WRITE: string;
	export const FFMPEG_DATADIR: string;
	export const RIPGREP_CONFIG_PATH: string;
	export const COLOR: string;
	export const npm_config_local_prefix: string;
	export const DESKTOP_SESSION: string;
	export const STARSHIP_LOG: string;
	export const LC_MONETARY: string;
	export const __ETC_PROFILE_NIX_SOURCED: string;
	export const KITTY_PID: string;
	export const CSF_OCCTResourcePath: string;
	export const HL_INITIAL_WORKSPACE_TOKEN: string;
	export const _ZO_FZF_OPTS: string;
	export const npm_config_globalconfig: string;
	export const XCURSOR_SIZE: string;
	export const CSF_STEPDefaults: string;
	export const GPG_TTY: string;
	export const CONAN_USER_HOME: string;
	export const EDITOR: string;
	export const GTK_MODULES: string;
	export const XDG_SEAT: string;
	export const PWD: string;
	export const NIX_PROFILES: string;
	export const DOTNET_CLI_HOME: string;
	export const LOGNAME: string;
	export const XDG_SESSION_DESKTOP: string;
	export const QT_QPA_PLATFORMTHEME: string;
	export const XDG_SESSION_TYPE: string;
	export const DRAWHOME: string;
	export const NIX_PATH: string;
	export const PNPM_HOME: string;
	export const npm_config_init_module: string;
	export const SYSTEMD_EXEC_PID: string;
	export const npm_config_tmp: string;
	export const OMF_PATH: string;
	export const CSF_StandardLiteDefaults: string;
	export const KITTY_PUBLIC_KEY: string;
	export const FZF_DEFAULT_COMMAND: string;
	export const XDG_GREETER_DATA_DIR: string;
	export const ABBR_TIPS_PROMPT: string;
	export const QT_STYLE_OVERRIDE: string;
	export const MOTD_SHOWN: string;
	export const GTK2_RC_FILES: string;
	export const __ABBR_TIPS_KEYS: string;
	export const ANSIBLE_HOME: string;
	export const HOME: string;
	export const XSERVERRC: string;
	export const LC_PAPER: string;
	export const LANG: string;
	export const WINEPREFIX: string;
	export const HISTFILE: string;
	export const LS_COLORS: string;
	export const _JAVA_AWT_WM_NONREPARENTING: string;
	export const XDG_CURRENT_DESKTOP: string;
	export const CARGO_HOME: string;
	export const npm_package_version: string;
	export const MEMORY_PRESSURE_WATCH: string;
	export const STARSHIP_SHELL: string;
	export const WAYLAND_DISPLAY: string;
	export const STARSHIP_CONFIG: string;
	export const NIX_SSL_CERT_FILE: string;
	export const KITTY_WINDOW_ID: string;
	export const XDG_SEAT_PATH: string;
	export const INVOCATION_ID: string;
	export const MANAGERPID: string;
	export const GOMODCACHE: string;
	export const INIT_CWD: string;
	export const CSF_ShadersDirectory: string;
	export const CSF_EXCEPTION_PROMPT: string;
	export const STARSHIP_SESSION_KEY: string;
	export const CSF_XmlOcafResource: string;
	export const UWSM_WAIT_VARNAMES: string;
	export const QT_QPA_PLATFORM: string;
	export const XDG_CACHE_HOME: string;
	export const npm_lifecycle_script: string;
	export const NVM_DIR: string;
	export const W3M_DIR: string;
	export const WORKON_HOME: string;
	export const CSF_SHMessage: string;
	export const GRADLE_USER_HOME: string;
	export const npm_config_npm_version: string;
	export const XDG_SESSION_CLASS: string;
	export const TERM: string;
	export const TERMINFO: string;
	export const LC_IDENTIFICATION: string;
	export const npm_package_name: string;
	export const ZSH: string;
	export const RUSTUP_HOME: string;
	export const npm_config_prefix: string;
	export const XDG_SCRIPT_HOME: string;
	export const fzf_preview_dir_cmd: string;
	export const USER: string;
	export const MYSQL_HISTFILE: string;
	export const SUDO_EDITOR: string;
	export const CSF_StandardDefaults: string;
	export const CSF_IGESDefaults: string;
	export const HYPRLAND_INSTANCE_SIGNATURE: string;
	export const NPM_CONFIG_USERCONFIG: string;
	export const XINITRC: string;
	export const VISUAL: string;
	export const NOTIFY_SOCKET: string;
	export const DISPLAY: string;
	export const CSF_XCAFDefaults: string;
	export const npm_lifecycle_event: string;
	export const SHLVL: string;
	export const NVM_CD_FLAGS: string;
	export const MOZ_ENABLE_WAYLAND: string;
	export const LC_TELEPHONE: string;
	export const LC_MEASUREMENT: string;
	export const XDG_VTNR: string;
	export const ANDROID_USER_HOME: string;
	export const CSF_PluginDefaults: string;
	export const CSF_TObjMessage: string;
	export const XDG_SESSION_ID: string;
	export const npm_config_user_agent: string;
	export const CASROOT: string;
	export const NUGET_PACKAGES: string;
	export const WLR_DRM_NO_ATOMIC: string;
	export const XDG_STATE_HOME: string;
	export const npm_execpath: string;
	export const XDG_RUNTIME_DIR: string;
	export const KITTY_LISTEN_ON: string;
	export const fish_key_bindings: string;
	export const PYENV_ROOT: string;
	export const DEBUGINFOD_URLS: string;
	export const npm_package_json: string;
	export const LC_TIME: string;
	export const HYPRCURSOR_THEME: string;
	export const fzf_fd_opts: string;
	export const QT_AUTO_SCREEN_SCALE_FACTOR: string;
	export const JOURNAL_STREAM: string;
	export const NODE_REPL_HISTORY: string;
	export const CSF_XSMessage: string;
	export const XCURSOR_THEME: string;
	export const MMGT_CLEAR: string;
	export const GTK3_MODULES: string;
	export const LEIN_HOME: string;
	export const XDG_DATA_DIRS: string;
	export const SQLITE_HISTORY: string;
	export const npm_config_noproxy: string;
	export const BROWSER: string;
	export const PATH: string;
	export const CSF_TObjDefaults: string;
	export const GDK_SCALE: string;
	export const npm_config_node_gyp: string;
	export const DOCKER_CONFIG: string;
	export const GDMSESSION: string;
	export const DBUS_SESSION_BUS_ADDRESS: string;
	export const OMNISHARPHOME: string;
	export const FZF_DEFAULT_OPTS: string;
	export const npm_config_global_prefix: string;
	export const NVM_BIN: string;
	export const MAIL: string;
	export const UWSM_FINALIZE_VARNAMES: string;
	export const ABBR_TIPS_REGEXES: string;
	export const QT_SCALE_FACTOR: string;
	export const DRAWDEFAULT: string;
	export const OMF_CONFIG: string;
	export const KITTY_INSTALLATION_DIR: string;
	export const npm_node_execpath: string;
	export const LC_NUMERIC: string;
	export const GOPATH: string;
	export const HYPRCURSOR_SIZE: string;
	export const _: string;
	export const NODE_ENV: string;
}

/**
 * Similar to [`$env/static/private`](https://svelte.dev/docs/kit/$env-static-private), except that it only includes environment variables that begin with [`config.kit.env.publicPrefix`](https://svelte.dev/docs/kit/configuration#env) (which defaults to `PUBLIC_`), and can therefore safely be exposed to client-side code.
 * 
 * Values are replaced statically at build time.
 * 
 * ```ts
 * import { PUBLIC_BASE_URL } from '$env/static/public';
 * ```
 */
declare module '$env/static/public' {
	
}

/**
 * This module provides access to runtime environment variables, as defined by the platform you're running on. For example if you're using [`adapter-node`](https://github.com/sveltejs/kit/tree/main/packages/adapter-node) (or running [`vite preview`](https://svelte.dev/docs/kit/cli)), this is equivalent to `process.env`. This module only includes variables that _do not_ begin with [`config.kit.env.publicPrefix`](https://svelte.dev/docs/kit/configuration#env) _and do_ start with [`config.kit.env.privatePrefix`](https://svelte.dev/docs/kit/configuration#env) (if configured).
 * 
 * This module cannot be imported into client-side code.
 * 
 * ```ts
 * import { env } from '$env/dynamic/private';
 * console.log(env.DEPLOYMENT_SPECIFIC_VARIABLE);
 * ```
 * 
 * > [!NOTE] In `dev`, `$env/dynamic` always includes environment variables from `.env`. In `prod`, this behavior will depend on your adapter.
 */
declare module '$env/dynamic/private' {
	export const env: {
		SHELL: string;
		npm_command: string;
		COLORTERM: string;
		GTK_THEME: string;
		PYENV_SHELL: string;
		CSF_MDTVTexturesDirectory: string;
		HYPRLAND_CMD: string;
		XDG_CONFIG_DIRS: string;
		npm_config_cache: string;
		XDG_SESSION_PATH: string;
		NVM_INC: string;
		XDG_MENU_PREFIX: string;
		XDG_BACKEND: string;
		CSF_DrawPluginDefaults: string;
		QT_WAYLAND_DISABLE_WINDOWDECORATION: string;
		NODE: string;
		LC_ADDRESS: string;
		CSF_LANGUAGE: string;
		XDG_BIN_HOME: string;
		LC_NAME: string;
		SSH_AUTH_SOCK: string;
		CSF_MIGRATION_TYPES: string;
		XDG_DATA_HOME: string;
		GRADLE_HOME: string;
		XDG_CONFIG_HOME: string;
		__ABBR_TIPS_VALUES: string;
		MEMORY_PRESSURE_WRITE: string;
		FFMPEG_DATADIR: string;
		RIPGREP_CONFIG_PATH: string;
		COLOR: string;
		npm_config_local_prefix: string;
		DESKTOP_SESSION: string;
		STARSHIP_LOG: string;
		LC_MONETARY: string;
		__ETC_PROFILE_NIX_SOURCED: string;
		KITTY_PID: string;
		CSF_OCCTResourcePath: string;
		HL_INITIAL_WORKSPACE_TOKEN: string;
		_ZO_FZF_OPTS: string;
		npm_config_globalconfig: string;
		XCURSOR_SIZE: string;
		CSF_STEPDefaults: string;
		GPG_TTY: string;
		CONAN_USER_HOME: string;
		EDITOR: string;
		GTK_MODULES: string;
		XDG_SEAT: string;
		PWD: string;
		NIX_PROFILES: string;
		DOTNET_CLI_HOME: string;
		LOGNAME: string;
		XDG_SESSION_DESKTOP: string;
		QT_QPA_PLATFORMTHEME: string;
		XDG_SESSION_TYPE: string;
		DRAWHOME: string;
		NIX_PATH: string;
		PNPM_HOME: string;
		npm_config_init_module: string;
		SYSTEMD_EXEC_PID: string;
		npm_config_tmp: string;
		OMF_PATH: string;
		CSF_StandardLiteDefaults: string;
		KITTY_PUBLIC_KEY: string;
		FZF_DEFAULT_COMMAND: string;
		XDG_GREETER_DATA_DIR: string;
		ABBR_TIPS_PROMPT: string;
		QT_STYLE_OVERRIDE: string;
		MOTD_SHOWN: string;
		GTK2_RC_FILES: string;
		__ABBR_TIPS_KEYS: string;
		ANSIBLE_HOME: string;
		HOME: string;
		XSERVERRC: string;
		LC_PAPER: string;
		LANG: string;
		WINEPREFIX: string;
		HISTFILE: string;
		LS_COLORS: string;
		_JAVA_AWT_WM_NONREPARENTING: string;
		XDG_CURRENT_DESKTOP: string;
		CARGO_HOME: string;
		npm_package_version: string;
		MEMORY_PRESSURE_WATCH: string;
		STARSHIP_SHELL: string;
		WAYLAND_DISPLAY: string;
		STARSHIP_CONFIG: string;
		NIX_SSL_CERT_FILE: string;
		KITTY_WINDOW_ID: string;
		XDG_SEAT_PATH: string;
		INVOCATION_ID: string;
		MANAGERPID: string;
		GOMODCACHE: string;
		INIT_CWD: string;
		CSF_ShadersDirectory: string;
		CSF_EXCEPTION_PROMPT: string;
		STARSHIP_SESSION_KEY: string;
		CSF_XmlOcafResource: string;
		UWSM_WAIT_VARNAMES: string;
		QT_QPA_PLATFORM: string;
		XDG_CACHE_HOME: string;
		npm_lifecycle_script: string;
		NVM_DIR: string;
		W3M_DIR: string;
		WORKON_HOME: string;
		CSF_SHMessage: string;
		GRADLE_USER_HOME: string;
		npm_config_npm_version: string;
		XDG_SESSION_CLASS: string;
		TERM: string;
		TERMINFO: string;
		LC_IDENTIFICATION: string;
		npm_package_name: string;
		ZSH: string;
		RUSTUP_HOME: string;
		npm_config_prefix: string;
		XDG_SCRIPT_HOME: string;
		fzf_preview_dir_cmd: string;
		USER: string;
		MYSQL_HISTFILE: string;
		SUDO_EDITOR: string;
		CSF_StandardDefaults: string;
		CSF_IGESDefaults: string;
		HYPRLAND_INSTANCE_SIGNATURE: string;
		NPM_CONFIG_USERCONFIG: string;
		XINITRC: string;
		VISUAL: string;
		NOTIFY_SOCKET: string;
		DISPLAY: string;
		CSF_XCAFDefaults: string;
		npm_lifecycle_event: string;
		SHLVL: string;
		NVM_CD_FLAGS: string;
		MOZ_ENABLE_WAYLAND: string;
		LC_TELEPHONE: string;
		LC_MEASUREMENT: string;
		XDG_VTNR: string;
		ANDROID_USER_HOME: string;
		CSF_PluginDefaults: string;
		CSF_TObjMessage: string;
		XDG_SESSION_ID: string;
		npm_config_user_agent: string;
		CASROOT: string;
		NUGET_PACKAGES: string;
		WLR_DRM_NO_ATOMIC: string;
		XDG_STATE_HOME: string;
		npm_execpath: string;
		XDG_RUNTIME_DIR: string;
		KITTY_LISTEN_ON: string;
		fish_key_bindings: string;
		PYENV_ROOT: string;
		DEBUGINFOD_URLS: string;
		npm_package_json: string;
		LC_TIME: string;
		HYPRCURSOR_THEME: string;
		fzf_fd_opts: string;
		QT_AUTO_SCREEN_SCALE_FACTOR: string;
		JOURNAL_STREAM: string;
		NODE_REPL_HISTORY: string;
		CSF_XSMessage: string;
		XCURSOR_THEME: string;
		MMGT_CLEAR: string;
		GTK3_MODULES: string;
		LEIN_HOME: string;
		XDG_DATA_DIRS: string;
		SQLITE_HISTORY: string;
		npm_config_noproxy: string;
		BROWSER: string;
		PATH: string;
		CSF_TObjDefaults: string;
		GDK_SCALE: string;
		npm_config_node_gyp: string;
		DOCKER_CONFIG: string;
		GDMSESSION: string;
		DBUS_SESSION_BUS_ADDRESS: string;
		OMNISHARPHOME: string;
		FZF_DEFAULT_OPTS: string;
		npm_config_global_prefix: string;
		NVM_BIN: string;
		MAIL: string;
		UWSM_FINALIZE_VARNAMES: string;
		ABBR_TIPS_REGEXES: string;
		QT_SCALE_FACTOR: string;
		DRAWDEFAULT: string;
		OMF_CONFIG: string;
		KITTY_INSTALLATION_DIR: string;
		npm_node_execpath: string;
		LC_NUMERIC: string;
		GOPATH: string;
		HYPRCURSOR_SIZE: string;
		_: string;
		NODE_ENV: string;
		[key: `PUBLIC_${string}`]: undefined;
		[key: `${string}`]: string | undefined;
	}
}

/**
 * Similar to [`$env/dynamic/private`](https://svelte.dev/docs/kit/$env-dynamic-private), but only includes variables that begin with [`config.kit.env.publicPrefix`](https://svelte.dev/docs/kit/configuration#env) (which defaults to `PUBLIC_`), and can therefore safely be exposed to client-side code.
 * 
 * Note that public dynamic environment variables must all be sent from the server to the client, causing larger network requests — when possible, use `$env/static/public` instead.
 * 
 * ```ts
 * import { env } from '$env/dynamic/public';
 * console.log(env.PUBLIC_DEPLOYMENT_SPECIFIC_VARIABLE);
 * ```
 */
declare module '$env/dynamic/public' {
	export const env: {
		[key: `PUBLIC_${string}`]: string | undefined;
	}
}
