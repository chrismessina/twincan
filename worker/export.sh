#!/bin/sh
# Print every beta signup as CSV for App Store Connect: TestFlight > your
# external group > Testers > "+" > Import from CSV. Columns are First Name,
# Last Name, Email; the name is split at its first space.
#   ./export.sh > testers.csv            all signups
#   ./export.sh 2026-11-10 > new.csv     signups since a date (UTC)
set -eu
cd "$(dirname "$0")"
since="${1:-0000}"
case "$since" in *[!0-9T:Z-]*) echo "date must look like 2026-11-10" >&2; exit 1;; esac
wrangler d1 execute twincan-beta --remote --json --command \
  "SELECT name, email FROM signups WHERE created_at >= '$since' ORDER BY created_at" |
node -e '
  const raw = require("fs").readFileSync(0, "utf8");
  let rows;
  try { rows = JSON.parse(raw)[0].results; }
  catch { console.error("wrangler did not return JSON; it said:\n" + raw.slice(0, 500)); process.exit(1); }
  const q = (s) => /[",\n]/.test(s) ? `"${s.replace(/"/g, "\"\"")}"` : s;
  for (const { name, email } of rows) {
    const i = name.indexOf(" ");
    const [first, last] = i < 0 ? [name, ""] : [name.slice(0, i), name.slice(i + 1)];
    console.log([first, last, email].map(q).join(","));
  }
  console.error(`${rows.length} signup(s)`);
'
