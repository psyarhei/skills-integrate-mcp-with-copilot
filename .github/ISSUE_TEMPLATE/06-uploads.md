name: "File / Image Uploads"
about: "Support secure profile photo uploads and serving"
title: "Add secure file/image upload support"
labels: backend,uploads,security

# File / Image Uploads

- Add endpoint to upload profile photos with validation (type, size).
- Store files safely (local storage or object store) and serve via secure URLs.
- Sanitize filenames and prevent path traversal.

Acceptance criteria:
- Uploads accepted only for allowed MIME types.
- Uploaded images are displayed in profile views.
