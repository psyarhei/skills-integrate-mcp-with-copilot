name: "Persistent database (SQLite/Postgres)"
about: "Replace in-memory store with a persistent DB and add migrations/import"
title: "Add persistent database and migrations"
labels: backend,database

# Add persistent database and migrations

Replace the current in-memory `activities` store with a persistent database. Tasks:

- Choose a database (SQLite for local/dev, Postgres for production).
- Add a small ORM or use `databases`/SQLAlchemy.
- Implement migrations or an import script (use `student.sql` as a reference).
- Update API endpoints to persist and read from DB.

Acceptance criteria:
- Data persists across restarts.
- Migration/import script provided.
- README updated with setup steps.
