Captain, all seven sources were fully reread through the read tool, including their endings. Long files were read in consecutive chunks of at most 150 lines; initially elided frontend output was reread using raw chunks. Fresh SHA-256 computation then succeeded for every source.

No files were changed. No external inbox, product code, tests, pipelines, agents, databases, or infrastructure were accessed.

## Source paths and fresh hashes

All paths below are relative to this exact root:
```text
/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-omp-recovery/pool/.treehouse/frontend-0b3a95/1/frontend/
```

| Source path | Fresh SHA-256 |
|---|---|
| `CLAUDE.md` | `aa59124396ea2fac91efc636fe185932fe27f63284960f6f27233beeb0e0cf7d` |
| `AGENTS.md` | `3b853ab9ad6f0d8244146b53a849c4a8d3adce59c7639a310076b536a23dff39` |
| `validation-sources/rialto-backend/CLAUDE.md` | `c8e1706e7be57beaa16424b2d1c980787da85b9f7c604d69fb1fe45fc8c46922` |
| `validation-sources/rialto-backend/AGENTS.md` | `79014b8a2c13b7ce5ef5142a4cc8936507616f3bf3cdbdca9b9650c2cbc9d6e3` |
| `validation-sources/rialto-frontend/CLAUDE.md` | `aa59124396ea2fac91efc636fe185932fe27f63284960f6f27233beeb0e0cf7d` |
| `validation-sources/rialto-frontend/AGENTS.md` | `8c135e463237e05bf577df161b242df3279c3816678c3e083219d22a535f90fe` |
| `validation-sources/AGENTS.md` | `8e751a4077315abd35e420083a9d87bd8d3490103a63b9c8b0e443bcf5492ca9` |

Computed after full reading with read-only `shasum -a 256`, exit status 0.

## Markers discovered from current disk contents

Both `AGENTS.md` and `validation-sources/rialto-backend/CLAUDE.md` contain:
```text
OMP_RECOVERY_5ecf480c332246a387e81a34b5943689
```

No recovery validation marker appeared in the other five fully read sources.

## Mandatory rules recovered

- **Backend:** Python managed exclusively with `uv`; FastAPI/Uvicorn, Pydantic, async SQLAlchemy/asyncpg, Alembic, pytest and Ruff. No TypeScript/Node backend or product UI in the backend repository.
- **Frontend:** Vite, React, TypeScript, pnpm, Tailwind/shadcn and TanStack Query. No direct datastore access or pricing, matching or RFQ business logic. Structured values come from REST/artifact schemas, never parsed chat prose.
- **Ownership and transactions:** Shared business logic and database access belong in `app/core/`. User-owned services require `user_id` and enforce ownership before reads or mutations; foreign ownership returns not-found. RLS configuration alone is not proof of enforcement. Core services and job handlers do not commit; the owning request, audited-tool or worker boundary commits. `run_logged_tool` owns MCP business-write transactions and tool-call audit records.
- **Typed MCP and REST:** Agents receive named tools with typed schemas and precise descriptions, never raw SQL/ORM access. Maintain one registry and shared core behavior. Read `CONTRACT.md` before changing API consumers; correct stale contracts before types and consumers. Missing endpoints must be reported, not replaced with invented data or workarounds.
- **Queues and evidence:** Queue long work with explicit retry/failure states and bounded, duplicate-safe recovery. Preserve successful stages, originals, quantities, units, price provenance and citations. Never fabricate prices or claim durable success prematurely. Source text is citable; contextual retrieval prefixes are not quotations.
- **Isolation and retention:** Shared/production databases remain read-only. Separately authorized development must verify affected database, worker, ingestion and agent flows against isolated resources; pytest alone is insufficient integration proof. Retain test databases, projects and storage until Tomasz explicitly approves deletion of the exact resources.
- **Human gates:** Preserve hooks, protected paths, contract review and approval requirements. Development requires Gauntlet fast during work and survivor before acceptance—not during this read-only probe. RFQ sending requires applicable approval; reusable price-book promotion requires explicit intent. Current safety and UX rules override historical instructions, including old migration or cleanup notes.

RECOVERY_COMPLETE
