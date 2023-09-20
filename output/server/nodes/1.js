

export const index = 1;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/fallbacks/error.svelte.js')).default;
export const imports = ["_app/immutable/nodes/1.df8560f6.js","_app/immutable/chunks/scheduler.8746962a.js","_app/immutable/chunks/index.914b573a.js","_app/immutable/chunks/singletons.6a0b5e08.js"];
export const stylesheets = [];
export const fonts = [];
