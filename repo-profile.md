# Repo profile: api-vtv-argentina

## GitHub creation settings

- Owner: patente-ar
- Repository name: api-vtv-argentina
- Visibility: Public
- Add README: yes
- .gitignore: Node
- License: MIT License
- Homepage: https://patente.ar/api-vtv
- Description: Ejemplos de integracion para consultar estado y vencimiento de VTV por patente con la API de patente.ar.

## Topics

api, argentina, vtv, verificacion-tecnica, patentes, webhooks, openapi

## SEO positioning

- Primary keyword: API VTV Argentina
- Secondary keywords: API de VTV en Argentina, vtv, API vehicular Argentina, API patente argentina
- Canonical commercial page: https://patente.ar/api-vtv
- Public informational page: https://patente.ar/verificacion-vtv
- Brand/entity link: https://patente.ar

## Repository features

- Enable Issues for integration questions.
- Enable Discussions only if there is time to moderate.
- Enable GitHub Pages from the `docs/` folder on `main`.
- Pin this repo on the GitHub profile after the README is published.
- Keep default branch as `main`.

## GitHub API metadata command

```bash
GH_TOKEN="$(security find-generic-password -a patente-ar -s codex-github:doc-apis-github -w)"
gh repo edit patente-ar/api-vtv-argentina \
  --description "Ejemplos de integracion para consultar estado y vencimiento de VTV por patente con la API de patente.ar." \
  --homepage "https://patente.ar/api-vtv" \
  --enable-issues=true
gh repo edit patente-ar/api-vtv-argentina --add-topic "api,argentina,vtv,verificacion-tecnica,patentes,webhooks,openapi"
```
