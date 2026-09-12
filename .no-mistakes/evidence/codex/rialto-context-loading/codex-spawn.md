CONTEXT_DELIVERY_COMPLETE

Standards received:

- Backend: Python with `uv` (`uv add`/`uv remove`; never pip/Poetry/Conda), FastAPI/Uvicorn, Pydantic, async SQLAlchemy/asyncpg, Alembic, pytest and Ruff. No TypeScript/Node backend or product UI in the backend repository.
- Business logic and database access belong in `app/core/`. REST and MCP handlers share that logic. Request/audit/worker boundaries own commits; core services and job handlers do not.
- Product agents use named, typed MCP tools with precise descriptions, never raw SQL/ORM. Queue long work with explicit retries/failures; preserve price sources and evidence; avoid duplicate registries and logic.
- Frontend: Vite + React + TypeScript, pnpm, Tailwind/shadcn and TanStack Query. No direct datastore access or pricing/matching/RFQ logic. Structured data comes from REST/artifact schemas, never chat prose.
- Read `CONTRACT.md` before API-consumer changes; update stale contracts first, flag missing endpoints and preserve human review gates.
- Verify affected flows against proven isolated resources; pytest alone is not integration proof. Development requires Gauntlet fast and survivor stages without bypassing hooks, protected paths or human gates.
- Shared/production databases remain read-only. Retain test databases, projects and storage until Tomasz confirms exact-resource deletion. Current safety and UX rules override historical notes.
- Preserve originals, scoped caches and drafts; keep navigation and reading available during processing; distinguish saved/viewable/searchable/accepted states; require durable confirmation before reporting success.

Supplied source paths and SHA-256 values, reported without independent filesystem verification:

| Source path | SHA-256 |
|---|---|
| `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-context-test/pool/.treehouse/backend-e79957/2/backend/CLAUDE.md` | `c016b8ae5f571f3af922fd972fdbe2090353ed7b20fce2e67f5c6e614f670bb0` |
| `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-context-test/pool/.treehouse/backend-e79957/2/backend/AGENTS.md` | `79014b8a2c13b7ce5ef5142a4cc8936507616f3bf3cdbdca9b9650c2cbc9d6e3` |
| `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/rialto-backend/CLAUDE.md` | `c016b8ae5f571f3af922fd972fdbe2090353ed7b20fce2e67f5c6e614f670bb0` |
| `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/rialto-backend/AGENTS.md` | `79014b8a2c13b7ce5ef5142a4cc8936507616f3bf3cdbdca9b9650c2cbc9d6e3` |
| `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/rialto-frontend/CLAUDE.md` | `aa59124396ea2fac91efc636fe185932fe27f63284960f6f27233beeb0e0cf7d` |
| `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/rialto-frontend/AGENTS.md` | `8c135e463237e05bf577df161b242df3279c3816678c3e083219d22a535f90fe` |
| `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/AGENTS.md` | `8e751a4077315abd35e420083a9d87bd8d3490103a63b9c8b0e443bcf5492ca9` |

No tools run, files edited, infrastructure contacted, agents launched, pushes made or PRs opened. Historical instructions were not executed.