# Issues to create for enhancements

This file lists proposed issues derived from the external project comparison. Create these as GitHub Issues (or use these templates under `.github/ISSUE_TEMPLATE/`).

1. Add persistent database and migrations
   - Description: Replace in-memory activity store with a persistent database (SQLite/Postgres) and add migration/import script using the schema from `student.sql`.
   - Labels: backend, database

2. Implement authentication & session management
   - Description: Add user authentication (students/admins), session handling or token-based auth, and protected admin endpoints.
   - Labels: backend, auth, security

3. Add admin & profile management CRUD
   - Description: Implement admin/profile pages and API endpoints to view, edit, and delete admin profiles and student records.
   - Labels: backend, api, admin

4. Multi-role dashboards and role-based views
   - Description: Create separate dashboards (admin vs student) and role-based access to pages like `dashboard.php` analogs.
   - Labels: frontend, ux, backend

5. Enforce enrollment restrictions server-side
   - Description: Implement server-side logic for `max_participants`, eligibility checks, and other enrollment restrictions.
   - Labels: backend, validation

6. Add file/image uploads for profiles
   - Description: Add secure profile photo uploads, storage, and serving (with validation and sanitization).
   - Labels: backend, uploads, security

7. CRUD for Students and SQL import
   - Description: Add full CRUD for `Student` records and provide an SQL import/migration using `student.sql` as a starter.
   - Labels: backend, database


---

If you want these created as actual GitHub Issues instead of this file, let me know and I can open them (requires creating Issues directly on GitHub).