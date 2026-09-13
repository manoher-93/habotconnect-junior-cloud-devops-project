# Candidate: Manoher Singh | manoharmsp93@gmail.com | +91-9648548275
# HabotConnect Hiring Project — fail-closed demonstration

#!/usr/bin/env bash
set -euo pipefail

tmp_file="scripts/_demo_insecure_secret.py"
trap 'rm -f "$tmp_file"' EXIT

# Construct the assignment-only demo secret at runtime so the scanner does not
# flag this demonstration script itself before the test begins.
key_name="api"_"key"
key_value="DEMO_NOT_A_REAL_KEY_""123456789"
printf '%s
' "$key_name = \"$key_value\"" > "$tmp_file"

if python scripts/check_secrets.py; then
  echo "ERROR: the fail-closed scanner did not block the demo secret."
  exit 1
else
  echo "PASS: insecure commit was blocked as expected."
fi
