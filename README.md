# Interview starter

FastAPI backend + React/Vite/TypeScript frontend.

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/). It downloads Python 3.12 for you if you don't have it.
  - macOS: `brew install uv`
  - Windows (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"` or `winget install --id=astral-sh.uv -e`
  - Then open a new terminal so `uv` is on your PATH.
- [Node.js](https://nodejs.org/) 20.19+ or 22.12+ (includes npm)

## Setup (once)

```sh
cd backend && uv sync && cd ..        # creates backend/.venv and installs Python deps
cd frontend && npm install && cd ..   # installs JS deps into frontend/node_modules
```

## Run

Use two terminals, both starting from the repo root.

```sh
# Terminal 1: backend on http://127.0.0.1:8000 (API docs at /docs)
cd backend && uv run uvicorn app.main:app --reload --port 8000
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



Build a 4×4 2048 game with a frontend and a backend API.

Start from a blank project directory. Set up the frontend and backend,
install dependencies, and configure local browser-to-server communication.
You may choose your stack and use standard framework generators and documentation.
Do not use an existing game implementation or prebuilt game engine.

Implement New Game:
- Keep the board on the backend; in-memory storage for one game is enough.
- Use 0 for empty cells.
- Initialize two tiles of value 2 in distinct random cells.
- Call the API from the frontend and display the returned board.

A simple grid with visible numbers is enough. Choose your own endpoint names.
Persistence, authentication, multiplayer, animations, and deployment are not required.


Add left, right, up, and down controls using buttons or arrow keys.

Send the direction to the backend. The backend must:
- Slide tiles as far as possible toward the selected edge.
- Merge only equal-valued tiles that become adjacent after sliding, processing from that edge.
- Do not merge across an intervening tile or diagonally.
- Allow each tile to participate in at most one merge per move.
- Add one tile of value 2 in a random empty cell only if the board changed.
- Return the resulting board so the frontend can update.
- Reject missing or invalid directions with an error response without changing state.

For this exercise, every spawned tile is 2.

Left-move examples, before spawning:
[0, 2, 0, 2] -> [4, 0, 0, 0]
[2, 2, 2, 0] -> [4, 2, 0, 0]
[2, 2, 2, 2] -> [4, 4, 0, 0]
[2, 2, 4, 0] -> [4, 4, 0, 0]
[4, 2, 0, 0] -> unchanged; no new tile