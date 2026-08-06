#!/usr/bin/env bash
set -euo pipefail

DB_NAME="${1:-fishtech}"

if ! command -v psql >/dev/null 2>&1; then
    echo "psql not found. Install PostgreSQL first (e.g. 'brew install postgresql@16')." >&2
    exit 1
fi

if ! psql -lqt | cut -d '|' -f 1 | grep -qw "$DB_NAME"; then
    echo "Creating database '$DB_NAME'..."
    createdb "$DB_NAME"
else
    echo "Database '$DB_NAME' already exists, skipping creation."
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "Applying schema.sql to '$DB_NAME'..."
psql -d "$DB_NAME" -f "$SCRIPT_DIR/schema.sql"

echo "Done. Set DATABASE_URL to: postgresql://$(whoami)@localhost:5432/$DB_NAME"
