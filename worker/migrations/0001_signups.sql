-- One row per address. Emails are stored lowercased, so the same person
-- signing up twice (or with different capitalization) stays one row.
CREATE TABLE signups (
  email      TEXT PRIMARY KEY,
  name       TEXT NOT NULL DEFAULT '',
  created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
);
