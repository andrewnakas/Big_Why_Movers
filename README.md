# Big Why Movers — Static Website

A fun, single-folder static site for a Montana moving company serving Bozeman, Livingston, Big Sky, and the surrounding Big Sky Country.

## Run locally

- Option 1: Open `index.html` in your browser.
- Option 2: Serve locally from this folder:
  - Python: `python3 -m http.server 8000` and open `http://localhost:8000/`

## Structure

- `index.html` — Landing page
- `about.html` — About Big Why Movers
- `services.html` — Services overview
- `contact.html` — Contact + simple client-side form handling
- `tips.html` — Moving best practices for Big Sky Country
- `gallery.html` — Photo gallery (Imgur album embed)
- `assets/css/style.css` — Shared styles, playful Big Sky theme
- `assets/js/main.js` — Small interactions (mobile nav, form toast)
- `assets/img/` — SVGs used in the site

## Tests

Run a quick smoke test to verify key content and navigation integrity:

```
python3 scripts/test_site.py
```

## Notes

- Certified U‑Haul Moving Help partner: https://www.uhaul.com/MovingHelp/Bozeman-MT-59715/1/Xip-Moving-Pros/?id=8E0B44F119FE42
- Primary contact: Sam Harlan — +1 (406) 589‑4641
- Gallery album: https://imgur.com/a/L8eFhdV

## Deploy options

- GitHub Pages (recommended for quick share):
  1) Push this repo to GitHub.
  2) In your repo, Settings → Pages → Set "Source" to "GitHub Actions".
  3) Push to `main` (or `master`); the workflow in `.github/workflows/deploy-pages.yml` deploys `big-why-movers-site/`.
  The URL will appear in the Actions summary and under Settings → Pages.

- Netlify (drag‑and‑drop):
  1) Zip the `big-why-movers-site` folder or select it directly.
  2) Go to https://app.netlify.com/drop and drop the folder to deploy.
  3) Optional: if connecting a repo, set the site root to `big-why-movers-site/`. `netlify.toml` is provided.

- Vercel (CLI or dashboard):
  1) `cd big-why-movers-site`
  2) Run `vercel` (requires Vercel CLI and login) and accept defaults to deploy.
  3) `vercel --prod` to promote to production. `vercel.json` is provided.
