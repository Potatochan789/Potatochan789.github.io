

export const index = 0;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/fallbacks/layout.svelte.js')).default;
export const imports = ["_app/immutable/nodes/0.61dbbcdc.js","_app/immutable/chunks/scheduler.8746962a.js","_app/immutable/chunks/index.914b573a.js"];
export const stylesheets = [];
export const fonts = [];
