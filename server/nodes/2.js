

export const index = 2;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/2.71100863.js","_app/immutable/chunks/scheduler.8746962a.js","_app/immutable/chunks/index.914b573a.js"];
export const stylesheets = ["_app/immutable/assets/2.8c1c24f1.css"];
export const fonts = [];
