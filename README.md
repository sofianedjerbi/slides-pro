# Présentation : la template ADR (Slidev)

Showcase de la template ADR de LionX (MADR, Astro Starlight, diagrammes Mermaid avec icônes
AWS, déploiement GitHub Pages). Court et droit au but : ce que fait la template, démo live.
Pour Pictet Technologies.

## Lancer

```bash
npm install      # une seule fois
npm run dev      # http://localhost:3030
```

Auto-hébergé sur un VPS + domaine (HTTPS auto via Caddy) :

```bash
DOMAIN=slides.tondomaine.com docker compose up -d
```

## Pendant la présentation

* `f` : plein écran
* `Espace` : avancer (les révélations au clic font le rythme)
* `o` : vue d'ensemble des slides
* **Mode présentateur** (notes d'orateur en français) : http://localhost:3030/presenter

## Le déroulé (8 slides)

1. Cover
2. « Tu écris ça. Tu obtiens ça. » : markdown MADR à gauche, site généré à droite + **démo live**
3. « Les sections d'un ADR » : toutes les sections MADR, requis / optionnel (et pourquoi optionnel)
4. « Le diagramme d'archi, c'est du texte » : source Mermaid `architecture-beta` + rendu côte à côte, icônes AWS
5. « Et Claude l'écrit pour toi » : prompt en langage naturel → diff mermaid/ADR, relu en PR
6. « Tu merges. C'est en ligne. » : ce que ça apporte + la page publiée
7. « Sous le capot » : la stack (MADR, Astro Starlight, Mermaid, GitHub Pages, Docker/Caddy)
8. « À vous » : CTA

Droit au but, 100 % template. Pas de slide sur le concept d'ADR (l'audience connaît).

## À préparer avant de monter sur scène

* Ouvrir le **site ADR déployé** dans un onglet (la démo live de la slide 2).
* Vérifier le mode présentateur et les notes.
* Poster les liens (dépôt + site) dans le canal Teams juste après.

## Export PDF (plan B projecteur)

```bash
npm run export   # produit slides-export.pdf
```

## Structure

* `slides.md` : la présentation + notes d'orateur
* `styles/index.css` : charte Pictet (rouge `--pictet-red`, filets de titre)
* `global-bottom.vue` : logo Pictet en bas à droite
* `setup/shiki.ts` : thème de coloration (github-light)
* `setup/mermaid.ts` : pack d'icônes AWS pour `architecture-beta`
* `public/` : captures du site + logo
* `scripts/shoot.mjs` et `scripts/crop-top.mjs` : régénérer / recadrer les captures
* `docker-compose.yml` + `Caddyfile` : auto-hébergement HTTPS

> Pour régénérer des captures : utiliser le **build de prod** du site ADR (`npm run preview`),
> pas le dev server, sinon la toolbar Astro apparaît dans l'image.
