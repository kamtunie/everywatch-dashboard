# Everywatch — CEO Dashboard App (Flask)

**Prepared by:** Kamil Tuniewicz • **Date:** Sep 30, 2025

This app serves a single static HTML dashboard (Plotly + vanilla JS). No transformations, 1:1 with the signed-off file.

## Local run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python app.py  # open http://localhost:8000
```

## Deploy to Render.com
- Create a new **Web Service** from this folder (GitHub repo)
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Or use the provided `render.yaml` for auto-config