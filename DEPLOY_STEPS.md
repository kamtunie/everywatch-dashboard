# Ultra Step-by-Step — Put Your Dashboard Live (No Compromises)

## Option A — Render.com (recommended)

1. Go to GitHub → New repository → **everywatch-dashboard** (Public).
2. Upload the **contents of `/everywatch_app`** (4 files + `Everywatch_CEO_Dashboard_RELEASE.html`).
3. Go to **render.com** → New → Web Service → connect your repo.
4. Render will read `render.yaml` automatically. If not:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Click **Create Web Service**. After it turns **Live**, open the URL.
6. Health check (optional): add `/health` to the URL → should return `ok`.

## Option B — 100% static hosting

### GitHub Pages
- Create repo `everywatch-dashboard-site`
- Rename `Everywatch_CEO_Dashboard_RELEASE.html` to **`index.html`** and upload it
- Repo → Settings → Pages → Source: `main` / root → **Save**
- Use the URL GitHub provides

### Netlify
- Go to netlify.com → Add new site → **Deploy manually**
- Drag a folder containing `index.html` (rename first)
- Use the public URL Netlify gives you

**Prepared by:** Kamil Tuniewicz — Sep 30, 2025