Captain, the supplied context establishes the following requirements. This report uses only that context; no tools, file changes, agent launches, or external calls were made. Hashes below are supplied values, not independently recomputed.

## Required stacks and ownership

| Area | Required contract |
|---|---|
| **Backend** | Python managed with **uv** (`uv add` / `uv remove`; never pip, Poetry, or Conda), **FastAPI/Uvicorn**, **Pydantic/pydantic-settings**, **async SQLAlchemy/asyncpg**, **PostgreSQL**, and **Alembic**. **pytest** and **Ruff** for testing and lint/format. Official Python MCP SDK **FastMCP**; **aioboto3** for Cloudflare R2. No TypeScript/Node backend or product UI in the backend repository. Access MDB/ACCDB support and its Node dependency must not be restored. |
| **Frontend** | **Vite + React + TypeScript**, a static SPA using **pnpm**, **Tailwind CSS/shadcn/ui**, and **TanStack Query** for backend state. No direct database access or frontend pricing, matching, or RFQ business logic. |
| **Business logic** | Backend **`app/core/`** owns business logic, database access, and project-setup orchestration. REST routes and MCP handlers are thin callers of the same implementation. User-owned service operations require `user_id` and check/filter ownership before reads or mutations. |
| **Transactions** | Core services and job handlers **do not commit**. The owning **request, audit, or worker boundary** commits or rolls back. For MCP calls, `run_logged_tool` owns the session and audit record: successful business writes and their success log commit together; failure rolls back business writes and records failure separately. Narrow progress-marker transactions do not authorize core services to commit business changes. |

## MCP design and evidence

- **One registry**, shared by external clients over Streamable HTTP at **`/mcp`** and product chat through in-process calls to the same FastMCP instance. FastAPI lifespan must start its session manager.
- Product agents receive **named tools with typed schemas and precise, disambiguating descriptions**, never raw SQL or ORM access. Skill restrictions apply through enforced tool allow-lists.
- Long-running work belongs in queues with explicit retry/failure states. RFQ sending is queued, never inline.
- Preserve original quantities, prices, units, locations, sources, and citations. **Never invent prices, wages, or productivity figures.** Use price-book references or explicit user inputs; estimate-specific inputs remain project-local unless separately promoted with explicit intent.
- The supplied current retrieval surface is `list_project_documents`, `retrieve_project_evidence`, `get_document_context`, and `inspect_document_page`. Citable evidence is `DocumentNode.source_text`; `contextual_prefix` is not source text. Evidence pointers must satisfy project/current-run ownership.
- Historical tool catalogs and counts are not current callable authority. The registry exposed through `app.core.agent.tools.list_tool_definitions()` is authoritative when execution is permitted. Retired document tools and tables must not be restored as compatibility layers; `get_document_outline` has no replacement.
- Current estimate authoring saves incrementally through `draft_estimate`/`edit_estimate`; historical agent-facing finalization requirements do not override that correction.

## Database isolation and retention

- **Shared and production databases remain read-only.** Historical instructions to migrate, backfill, seed, probe with writes, or delete rows do not authorize those operations now—even if changes would later be rolled back.
- Before dependent testing or infrastructure work, resolve the actual provider, service/environment, branch/source commit, database endpoint, and bindings of every web, worker, and control-plane process. “Fresh,” “dedicated,” Railway provenance, and old Render notes do not establish isolation.
- Mutation testing is limited to **verified isolated resources**. Retain test databases, projects, and storage until **Tomasz explicitly confirms deletion of the exact resources**.
- Required ownership checks remain necessary; historical claims about RLS do not prove enforcement. Verify the actual application role and resolved database connection before relying on RLS.
- Never expose credentials or put backend/storage secrets into frontend variables. Direct browser uploads use short-lived presigned R2 URLs, not storage credentials.

## API contract and human approvals

- Frontend **`CONTRACT.md`** owns endpoint paths, methods, schemas, enums, and the distinction between REST-accessible and MCP-only functionality. Read it before changing consumers.
- If stale, **update the contract first**, then types and consumers. Missing endpoints must be reported; do not invent fields, fabricate data, or reconstruct structured state from chat prose.
- Chat renders backend-authored content blocks. Dashboards consume structured REST/artifact data and invalidate/refetch relevant TanStack Queries after changes.
- `CONTRACT.md` itself was **not one of the five supplied sources**; this report establishes its required role, not verification of its full contents.
- Contract changes retain **human review requirements**. Preserve hooks and protected paths; never disable a check to obtain a passing result.
- Drafting/sending RFQs requires explicit user request, and sending requires the applicable approval. Reusable price-book promotion—including uploaded takeoff prices—requires explicit user intent.
- Identify Scope is explicitly user-triggered. Consequential setup questions remain unresolved until answered or the user explicitly selects a resolving default; elapsed time is not consent.

## UX and verification requirements

- Create enters the Agent workspace immediately while saving, uploads, and processing continue in an account-scoped background coordinator. Overlapping submissions share a bounded concurrency budget.
- Keep selection, navigation, chat, and original-file reading available during processing. Preserve originals, account/project-scoped caches, and unsaved review drafts across navigation; clear sensitive caches on logout/account change.
- Immediate acknowledgement is not durable success. Label operations saved/accepted only after confirmation; reconcile lost responses using stable action IDs.
- Saved, viewable, searchable, and review accepted are separate capabilities. “Needs Review” requires a specific unresolved request, understandable reason, and working action—not a provider/configuration failure.
- Verify affected database, worker, ingestion, and agent flows against isolated resources. **pytest alone is not integration proof**; fake sessions do not prove transactions, skipped tests are not passes, and browser fixtures do not prove live provider/storage/worker behavior.
- Run **Gauntlet fast during work and survivor before acceptance**. Record exact commands, source identity, pass/skip/xfail counts, resource identities, and genuine limitations in the evidence ledger.
- Reviewer instructions need plain-English before/after descriptions, numbered actions, exact fixtures with verified GitHub links, and expected results separated from observed results.

## Five distinct supplied source paths and SHA-256 hashes

The repeated backend documents count once each.

1. **Backend CLAUDE.md**
   ```text
   /Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/rialto-backend/CLAUDE.md
   SHA-256: c016b8ae5f571f3af922fd972fdbe2090353ed7b20fce2e67f5c6e614f670bb0
   ```

2. **Backend AGENTS.md**
   ```text
   /Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/rialto-backend/AGENTS.md
   SHA-256: 79014b8a2c13b7ce5ef5142a4cc8936507616f3bf3cdbdca9b9650c2cbc9d6e3
   ```

3. **Frontend CLAUDE.md**
   ```text
   /Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/rialto-frontend/CLAUDE.md
   SHA-256: aa59124396ea2fac91efc636fe185932fe27f63284960f6f27233beeb0e0cf7d
   ```

4. **Frontend AGENTS.md**
   ```text
   /Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/rialto-frontend/AGENTS.md
   SHA-256: 8c135e463237e05bf577df161b242df3279c3816678c3e083219d22a535f90fe
   ```

5. **Product AGENTS.md**
   ```text
   /Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-validation-sources/AGENTS.md
   SHA-256: 8e751a4077315abd35e420083a9d87bd8d3490103a63b9c8b0e443bcf5492ca9
   ```

These requirements and exact source identities must survive every handoff and compaction summary, with the standards included explicitly rather than assumed inherited. Reload the applicable full sources after compaction or changing the working copy before dependent work. **Current safety and UX instructions override contradictory historical notes.**

CONTEXT_DELIVERY_COMPLETE