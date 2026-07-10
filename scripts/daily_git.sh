#!/bin/bash

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

cd "$PROJECT_DIR" || exit

git add .

if ! git diff --cached --quiet; then
    git commit -m "Daily update $(date '+%Y-%m-%d %H:%M')"
    git push origin main
fi
