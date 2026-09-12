#!/bin/bash
set -e
cd /Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A
. tests/lib.sh
FM_RIALTO_LIVE=1
fm_live_gate opt-in FM_RIALTO_LIVE omp tmux treehouse python3
export FM_HOME=/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-omp-recovery/home
export PATH=/Users/tomasz/.no-mistakes/worktrees/4019102881cf/01M2BJC44MJV1HEJ1P50949S5A/config/rialto-omp-recovery/bin:"$PATH"
unset TMUX FM_TASK_ID
exec "$@"
