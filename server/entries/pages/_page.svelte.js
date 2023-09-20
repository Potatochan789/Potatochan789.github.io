import { c as create_ssr_component, d as add_attribute, i as is_promise, n as noop, f as each, e as escape } from "../../chunks/ssr.js";
const _page_svelte_svelte_type_style_lang = "";
const css = {
  code: ".svelte-brtn5w{box-sizing:border-box;font-family:'Mooli', sans-serif}.header.svelte-brtn5w{background-color:#3b77f8;display:flex;flex-direction:row;align-items:left;padding:0 1rem;position:fixed;left:0;top:0;height:4rem;width:100%;color:#fff;& .search {\n			width: 15rem;\n			display: flex;\n			flex-direction: row;\n			align-items: center;\n			padding: 0 1rem;\n			gap: 1rem;\n		};& h1 {\n			font-size: 1.3rem;\n		};& input {\n			width: 7rem;\n			height: 1.75rem;\n		};& .link-bar {\n			display: flex;\n			gap: 1rem;\n\n			list-style-type: none;\n\n			& a {\n				background-color: rgba(255, 255, 255, 0.1);\n				border: 1px rgba(255, 255, 255, 0.3) solid;\n				color: #fff;\n				text-decoration: none;\n				padding: 0.5rem 1rem;\n				border-radius: 3px;\n				transition: background 0.1s ease-out, border 0.1s ease-out, transform 0.1s ease-out;\n\n				&:hover {\n					background-color: rgba(255, 255, 255, 0.2);\n					border: 1px rgba(255, 255, 255, 0.5) solid;\n					transform: translateY(-2px);\n				}\n			}\n		}}.team.svelte-brtn5w:nth-child(odd){background-color:#eee}.teams.svelte-brtn5w{margin-top:7rem;margin-left:3rem}.team.svelte-brtn5w{display:flex;justify-content:space-between;width:90%;max-width:25rem;border-bottom:1px solid rgba(0, 0, 0, 0.2)}",
  map: null
};
async function load() {
  return await (await fetch("/test.json")).json();
}
function getUrl(pokemon) {
  pokemon = pokemon.toLowerCase();
  pokemon = pokemon.split(",")[0];
  pokemon = pokemon.replaceAll(" ", "-");
  const pokemonImage = document.createElement("img");
  pokemonImage.title = pokemon;
  return `https://www.smogon.com/forums//media/minisprites/${pokemon}.png`;
}
function containsPokemon(team, name) {
  return team.filter((elem) => elem.toLowerCase().includes(name.toLowerCase())).length > 0;
}
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let player = "";
  let pokemonSearch = "";
  const data = load();
  $$result.css.add(css);
  return `${$$result.head += `<!-- HEAD_svelte-fqsu9v_START --><meta charset="UTF-8" class="svelte-brtn5w"><meta http-equiv="X-UA-Compatible" content="IE=edge" class="svelte-brtn5w"><meta name="viewport" content="width=device-width, initial-scale=1.0" class="svelte-brtn5w">${$$result.title = `<title>Document</title>`, ""}<link rel="preconnect" href="https://fonts.googleapis.com" class="svelte-brtn5w"><link rel="preconnect" href="https://fonts.gstatic.com" class="svelte-brtn5w"><link href="https://fonts.googleapis.com/css2?family=Mooli&display=swap" rel="stylesheet" class="svelte-brtn5w"><!-- HEAD_svelte-fqsu9v_END -->`, ""}  <header class="header svelte-brtn5w"><div class="search svelte-brtn5w"><h1 class="svelte-brtn5w" data-svelte-h="svelte-1r9prsx">Player:</h1> <input class="svelte-brtn5w"${add_attribute("value", player, 0)}></div> <div class="search svelte-brtn5w"><h1 class="svelte-brtn5w" data-svelte-h="svelte-3k2cax">Pokemon:</h1> <input class="svelte-brtn5w"${add_attribute("value", pokemonSearch, 0)}></div></header> ${function(__value) {
    if (is_promise(__value)) {
      __value.then(null, noop);
      return ` <span class="svelte-brtn5w" data-svelte-h="svelte-1e3c296">LOADING</span> `;
    }
    return function(data2) {
      return ` <div id="teams" class="teams svelte-brtn5w">${each(data2, (entry) => {
        return `${each(Object.entries(entry.teams), ([, teamData]) => {
          return `${(player.length === 0 || teamData.name.includes(player)) && (pokemonSearch.length === 0 || containsPokemon(teamData.team, pokemonSearch)) ? `<div class="team svelte-brtn5w"><span class="svelte-brtn5w">${escape(teamData.name)}</span> <a class="pokemon-list svelte-brtn5w"${add_attribute("href", entry.link, 0)} target="_BLANK">${each(teamData.team, (pokemon) => {
            return `<img${add_attribute("src", getUrl(pokemon), 0)} alt="" class="svelte-brtn5w">`;
          })}</a> </div>` : ``}`;
        })}`;
      })}</div> `;
    }(__value);
  }(data)}`;
});
export {
  Page as default
};
