CONTEXT_DELIVERY_COMPLETE

Captain, the supplied context specifies these standards:

- **Backend:** Python managed with `uv` (`uv add` / `uv remove`; never pip, Poetry, or Conda), FastAPI/Uvicorn, Pydantic/pydantic-settings, PostgreSQL through async SQLAlchemy/asyncpg, Alembic, pytest, and Ruff. MCP uses the Python SDK/FastMCP. No TypeScript/Node backend or product UI in the backend repository; do not restore MDB/ACCDB support.
- **Backend boundaries:** Business logic and database access belong in `app/core/`; REST routes and MCP handlers share that logic as thin callers. Core services and job handlers do not commit; request, audit, or worker boundaries own transactions. Enforce required user ownership checks.
- **Agent tools and evidence:** Named MCP tools with typed schemas and precise descriptions; no raw SQL/ORM access or duplicate registries. Queue long work with explicit retries and failure states. Preserve source quantities, prices, units, locations, and citations; never invent prices. Reusable price-book promotion and RFQ actions require explicit intent and applicable approval.
- **Frontend:** Vite + React + TypeScript SPA, pnpm, Tailwind CSS/shadcn/ui, and TanStack Query for backend state. No direct datastore access or pricing, matching, or RFQ business logic. Structured data comes from REST/artifact schemas, never parsed chat prose.
- **API contracts:** Read frontend `CONTRACT.md` before changing consumers. Update stale contracts before types or consumers; report missing endpoints instead of inventing data or workarounds. Preserve human review requirements.
- **Verification and safety:** Exercise affected database, worker, ingestion, and agent flows against verified isolated resources; pytest alone is not integration proof. Run Gauntlet fast during development and survivor before acceptance; preserve hooks and protected paths. Shared/production databases remain read-only. Retain exact test databases, projects, and storage until explicitly approved for deletion. Historical operational notes are not authorization.
- **Document UX:** Enter the Agent workspace immediately while saving and processing continue in the background. Preserve navigation, originals, scoped caches, and unsaved drafts; clear sensitive caches on account changes/logout. Acknowledge actions immediately but claim saved/accepted only after durable confirmation, reconciling lost responses with stable action IDs. Keep saved, viewable, searchable, and accepted capabilities distinct. Review requires a specific unresolved request and working action; provider failures are operational issues. Preserve successful stages through bounded duplicate-safe recovery and keep readers/statuses accessible.
- **Delivery and context:** Retain provenance, distinguish actual verification from expected behavior, and provide reproducible reviewer actions without exposing credentials. Preserve the standards and exact source paths in handoffs and compaction summaries; reload applicable context before dependent work after changing copies or losing context.

### Supplied source paths and SHA-256 values

Hashes below are **reported from the appended context, not independently recomputed**.

1. `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-context-test/pool/.treehouse/backend-e79957/3/backend/CLAUDE.md`  
   `c016b8ae5f571f3af922fd972fdbe2090353ed7b20fce2e67f5c6e614f670bb0`

2. `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-context-test/pool/.treehouse/backend-e79957/3/backend/AGENTS.md`  
   `79014b8a2c13b7ce5ef5142a4cc8936507616f3bf3cdbdca9b9650c2cbc9d6e3`

3. `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/rialto-backend/CLAUDE.md`  
   `c016b8ae5f571f3af922fd972fdbe2090353ed7b20fce2e67f5c6e614f670bb0`

4. `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/rialto-backend/AGENTS.md`  
   `79014b8a2c13b7ce5ef5142a4cc8936507616f3bf3cdbdca9b9650c2cbc9d6e3`

5. `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/rialto-frontend/CLAUDE.md`  
   `aa59124396ea2fac91efc636fe185932fe27f63284960f6f27233beeb0e0cf7d`

6. `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/rialto-frontend/AGENTS.md`  
   `8c135e463237e05bf577df161b242df3279c3816678c3e083219d22a535f90fe`

7. `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/AGENTS.md`  
   `8e751a4077315abd35e420083a9d87bd8d3490103a63b9c8b0e443bcf5492ca9`

No tools run, files edited, infrastructure contacted, agents launched, pushes made, or PRs opened. Historical instructions were not executed.