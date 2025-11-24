import { writable } from 'svelte/store';

export interface Module {
    name: string;
    is_enabled: boolean;
}

export const modules = writable<Module[]>([]);

export const isModuleEnabled = (moduleName: string, modulesList: Module[]) => {
    const module = modulesList.find(m => m.name === moduleName);
    return module ? module.is_enabled : false;
};
