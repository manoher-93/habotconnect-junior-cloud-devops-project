#!/usr/bin/env bash
set -euo pipefail

printf '\n[1/4] Python compile check\n'
python -m compileall -q src tests

printf '\n[2/4] Deterministic Python/DCYN tests\n'
python -m unittest tests.test_dcyn tests.test_dcyn_invalid_example -v

if python -c 'import django, rest_framework' >/dev/null 2>&1; then
  printf '\n[2b/4] Django REST Framework serializer tests\n'
  python -m unittest tests.test_serializer -v
else
  printf '\n[2b/4] Django REST Framework tests skipped: Django/DRF are not installed in this local environment.\n'
  printf 'CI installs requirements.txt before running the full test suite.\n'
fi

printf '\n[3/4] Deterministic secret scan\n'
python scripts/check_secrets.py

printf '\n[4/4] Fail-closed demonstration\n'
bash scripts/demo_fail_closed.sh

printf '\nLocal checks completed. Terraform checks require the Terraform CLI; CI runs the full Terraform/TFLint/Checkov/Gitleaks gates.\n'
