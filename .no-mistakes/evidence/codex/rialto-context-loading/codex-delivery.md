Captain, this report uses only the supplied instruction text. No tools, files, agents, or external systems were used. Current safety and UX instructions override conflicting historical notes.

- **Backend stack:** Python managed with `uv` (`uv add`/`uv remove`; never pip, Poetry, or Conda), FastAPI/Uvicorn, Pydantic/pydantic-settings, PostgreSQL through async SQLAlchemy/asyncpg, Alembic, pytest, and Ruff. Use the official Python MCP SDK/FastMCP. No TypeScript/Node backend or product UI in the backend repository; do not restore MDB/ACCDB support.
- **Frontend stack:** Vite + React + TypeScript SPA, pnpm, Tailwind CSS/shadcn/ui, and TanStack Query for backend state. No direct datastore access or frontend pricing, matching, or RFQ business logic. Backend-authorized presigned R2 uploads are the explicit storage-transfer exception; credentials remain server-side.
- **Transaction ownership:** Business logic and database access belong in `app/core/`, shared by thin REST routes and MCP handlers. Core services and job handlers never commit. The owning request, audit, or worker boundary commits or rolls back. MCP `run_logged_tool` commits successful business writes with their audit row; failures roll back business writes and record a separate failure. User-owned services require and enforce `user_id`.
- **MCP design:** Specific named tools, typed schemas, and precise, disambiguating descriptions; never raw SQL/ORM access. One registry serves product chat and external MCP clients, with FastMCP mounted at `/mcp` inside FastAPI. Do not duplicate registries or business logic. Historical catalogs do not establish callable tools. Long work uses queues with explicit retries and failure states. Preserve price provenance and evidence; never invent prices. Reusable price-book promotion requires explicit intent, and RFQ drafting/sending requires explicit user request with applicable send approval.
- **Database isolation and retention:** Production/shared databases remain read-only, including rollback-only write probes, migrations, stamps, seeds, backfills, and mutating test flows. Database-backed work requires a verified disposable Neon child branch or another isolated non-production database. Prove provider, project, branch ID, endpoint, database identity, and all backend/worker/control-plane/preview/eval bindings; names or Railway provenance alone prove nothing. Verified isolated resources have standing mutation authorization, but **retain test databases, projects, and storage until Tomasz explicitly confirms deletion of the exact resources**. Historical cleanup or shared-database migration notes grant no authority.
- **API contract:** Read frontend `CONTRACT.md` before changing consumers. Follow documented paths, methods, schemas, and enums exactly; update stale contracts before types and consumers. Flag missing or MCP-only endpoints rather than inventing data or workarounds. Structured UI data comes from REST/artifact schemas, never chat-prose parsing; chat side effects trigger query invalidation/refetch.
- **Human gates and evidence:** Contract, permission, dependency, CI, secret, and deployment changes require human review. Shared infrastructure operations require explicit authorization and confirmation of resolved targets. Never repair production migration history through manual `alembic_version` edits, stamping, or unmerged migrations; production recovery requires reviewed code merged to `main` and a named human release owner. Preserve Gauntlet hooks, protected paths, isolation, and human gates; fast checks during development and survivor before acceptance remain required for implementation work. Real isolated database/worker/ingestion/agent flows provide integration evidence; pytest, mocks, skipped tests, and fixture-only browser tests do not establish it. No checks were executed for this text-only verification.

The five distinct supplied sources follow. Hashes are reproduced as supplied, not independently computed; repeated backend sources count once.

1. `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/rialto-backend/CLAUDE.md`  
   SHA-256: `c016b8ae5f571f3af922fd972fdbe2090353ed7b20fce2e67f5c6e614f670bb0`

2. `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/rialto-backend/AGENTS.md`  
   SHA-256: `79014b8a2c13b7ce5ef5142a4cc8936507616f3bf3cdbdca9b9650c2cbc9d6e3`

3. `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/rialto-frontend/CLAUDE.md`  
   SHA-256: `aa59124396ea2fac91efc636fe185932fe27f63284960f6f27233beeb0e0cf7d`

4. `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/rialto-frontend/AGENTS.md`  
   SHA-256: `8c135e463237e05bf577df161b242df3279c3816678c3e083219d22a535f90fe`

5. `/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/AGENTS.md`  
   SHA-256: `8e751a4077315abd35e420083a9d87bd8d3490103a63b9c8b0e443bcf5492ca9`

Preserve these requirements and exact source paths in every handoff and compaction summary. After compaction or switching checkout, reload the applicable full sources before dependent work.

CONTEXT_DELIVERY_COMPLETE