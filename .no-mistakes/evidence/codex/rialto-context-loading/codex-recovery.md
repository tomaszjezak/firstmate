Current validation marker: **`CODEX_RECOVERY_20260912`**, found in the checkout backend `AGENTS.md`, line 77. That file’s hash changed from the previously supplied value; the other six source hashes match.

Current development rules:

- **Backend:** Python with `uv`, FastAPI/Uvicorn, Pydantic, async SQLAlchemy/asyncpg, Alembic, pytest and Ruff. No Node/TypeScript backend or product frontend code in the backend repository.
- **Architecture:** business logic and database access belong in `app/core/`; REST and MCP handlers remain thin. Request/audit/worker boundaries own commits. Agents receive typed, named MCP tools, never raw SQL/ORM access. Queue long work with explicit retry/failure states.
- **Frontend:** Vite, React, TypeScript, pnpm, Tailwind/shadcn and TanStack Query. Use structured REST/artifact data; no direct datastore access, pricing business logic or chat-prose parsing. Update `CONTRACT.md` before changing consumers when its schemas are stale.
- **Safety and evidence:** shared/production databases remain read-only. Verify affected flows against isolated resources; pytest alone is insufficient integration evidence. Preserve Gauntlet checks and human gates. Retain test resources until Tomasz confirms their exact deletion.
- **Product and UX:** preserve original documents, quantities, prices, units and citations; never invent prices. Keep navigation and original reading available during processing. Distinguish durable saving, viewability, searchability and review acceptance. Preserve drafts and successful stages through bounded recovery.
- **Context and delivery:** current safety/UX instructions override historical notes. Preserve exact source identities across handoffs and compaction; reload sources before dependent work. Report verified results separately from expected behavior and limitations.

The following SHA-256 values were computed from current file bytes. Paths are relative to this exact common prefix:

`/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/`

| Source path | Current SHA-256 |
|---|---|
| `rialto-context-test/pool/.treehouse/backend-e79957/2/backend/CLAUDE.md` | `c016b8ae5f571f3af922fd972fdbe2090353ed7b20fce2e67f5c6e614f670bb0` |
| `rialto-context-test/pool/.treehouse/backend-e79957/2/backend/AGENTS.md` | `38644a470d149c2db066202a654c51c89c5e1bdd7e800135bede6184d5b434a9` |
| `rialto-validation-sources/rialto-backend/CLAUDE.md` | `c016b8ae5f571f3af922fd972fdbe2090353ed7b20fce2e67f5c6e614f670bb0` |
| `rialto-validation-sources/rialto-backend/AGENTS.md` | `79014b8a2c13b7ce5ef5142a4cc8936507616f3bf3cdbdca9b9650c2cbc9d6e3` |
| `rialto-validation-sources/rialto-frontend/CLAUDE.md` | `aa59124396ea2fac91efc636fe185932fe27f63284960f6f27233beeb0e0cf7d` |
| `rialto-validation-sources/rialto-frontend/AGENTS.md` | `8c135e463237e05bf577df161b242df3279c3816678c3e083219d22a535f90fe` |
| `rialto-validation-sources/AGENTS.md` | `8e751a4077315abd35e420083a9d87bd8d3490103a63b9c8b0e443bcf5492ca9` |

The workspace-root `rialto-context-test/AGENTS.md` was supplied inline but is absent on disk, so no current file hash is available for it.

No implementation, infrastructure operations, agent launches or historical tasks were performed. No files were changed.

RECOVERY_COMPLETE