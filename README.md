# Interview starter

FastAPI backend + React/Vite/TypeScript frontend.

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) (`brew install uv` on macOS). It downloads Python 3.12 for you if you don't have it.
- [Node.js](https://nodejs.org/) 20.19+ or 22.12+ (includes npm)

## Setup (once)

```sh
git clone <repo-url>
cd <repo-folder>

cd backend && uv sync && cd ..        # creates backend/.venv and installs Python deps
cd frontend && npm install && cd ..   # installs JS deps into frontend/node_modules
```

## Run

Use two terminals, both starting from the repo root.

```sh
# Terminal 1: backend on http://127.0.0.1:8000 (API docs at /docs)
cd backend && uv run fastapi dev app/main.py
```

```sh
# Terminal 2: frontend on http://localhost:5173
cd frontend && npm run dev
```

Open http://localhost:5173. The frontend proxies `/api/*` to the backend, so start both.

## Project layout

```
backend/
  app/main.py            FastAPI app; registers routers
  app/routers/health.py  example endpoints: GET /api/health, GET /api/hello, POST /api/echo
frontend/
  src/api.ts             fetch wrapper used for every backend call
  src/App.tsx            example page calling the backend
  vite.config.ts         dev server + /api proxy to port 8000
```

To add an endpoint, create a router in `backend/app/routers/` and register it in `app/main.py` with `app.include_router(...)`.
