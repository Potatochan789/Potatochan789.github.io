export const manifest = (() => {
function __memo(fn) {
	let value;
	return () => value ??= (value = fn());
}

return {
	appDir: "_app",
	appPath: "_app",
	assets: new Set(["favicon.png","test.json"]),
	mimeTypes: {".png":"image/png",".json":"application/json"},
	_: {
		client: {"start":"_app/immutable/entry/start.f4b11e8a.js","app":"_app/immutable/entry/app.63c278aa.js","imports":["_app/immutable/entry/start.f4b11e8a.js","_app/immutable/chunks/scheduler.8746962a.js","_app/immutable/chunks/singletons.6a0b5e08.js","_app/immutable/entry/app.63c278aa.js","_app/immutable/chunks/scheduler.8746962a.js","_app/immutable/chunks/index.914b573a.js"],"stylesheets":[],"fonts":[]},
		nodes: [
			__memo(() => import('./nodes/0.js')),
			__memo(() => import('./nodes/1.js')),
			__memo(() => import('./nodes/2.js'))
		],
		routes: [
			{
				id: "/",
				pattern: /^\/$/,
				params: [],
				page: { layouts: [0,], errors: [1,], leaf: 2 },
				endpoint: null
			}
		],
		matchers: async () => {
			
			return {  };
		}
	}
}
})();
