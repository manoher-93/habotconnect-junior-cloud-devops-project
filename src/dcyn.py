# Candidate: Manoher Singh | manoharmsp93@gmail.com | +91-9648548275
# HabotConnect Hiring Project — deterministic onboarding decision library

"""Deterministic Yes/No validation for the student onboarding contract."""

from __future__ import annotations

import re
from datetime import date
from typing import Any
from uuid import UUID

EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
COUNTRY_RE = re.compile(r"^[A-Z]{2}$")
ORG_RE = re.compile(r"^[a-z0-9-]{1,64}$")
ALLOWED_FIELDS = {
    "student_id",
    "parent_email",
    "student_name",
    "date_of_birth",
    "requires_learning_support",
    "support_type",
    "guardian_consent",
    "data_processing_consent",
    "country_code",
    "organization_id",
}


def _age_on(date_of_birth: date, today: date) -> int:
    return today.year - date_of_birth.year - (
        (today.month, today.day) < (date_of_birth.month, date_of_birth.day)
    )


def evaluate_onboarding(data: dict[str, Any]) -> dict[str, Any]:
    """Return a binary decision plus stable, machine-readable reason codes."""
    reasons: list[str] = []
    codes: list[str] = []
    required = ALLOWED_FIELDS - {"support_type"}

    unknown = sorted(set(data) - ALLOWED_FIELDS)
    for field in unknown:
        codes.append("D001")
        reasons.append(f"{field}: unknown field")
    for field in sorted(required - set(data)):
        codes.append("D002")
        reasons.append(f"{field}: required")

    if reasons:
        return {"decision": "No", "codes": codes, "reasons": reasons}

    student_id = data["student_id"]
    try:
        UUID(student_id)
    except (TypeError, ValueError, AttributeError):
        codes.append("D003")
        reasons.append("student_id: valid UUID required")

    email = data["parent_email"]
    if not isinstance(email, str) or len(email) > 254 or not EMAIL_RE.fullmatch(email):
        codes.append("D004")
        reasons.append("parent_email: valid email with maximum 254 characters required")

    name = data["student_name"]
    if not isinstance(name, str) or not 2 <= len(name.strip()) <= 100:
        codes.append("D005")
        reasons.append("student_name: 2-100 non-whitespace characters required")

    try:
        dob = date.fromisoformat(data["date_of_birth"])
        age = _age_on(dob, date.today())
        if not 3 <= age <= 18:
            codes.append("D006")
            reasons.append("date_of_birth: student age must be between 3 and 18")
    except (TypeError, ValueError):
        codes.append("D007")
        reasons.append("date_of_birth: valid ISO date required")

    support_flag = data["requires_learning_support"]
    if not isinstance(support_flag, bool):
        codes.append("D008")
        reasons.append("requires_learning_support: boolean required")

    support_type = data.get("support_type")
    if support_flag is True:
        if not isinstance(support_type, str) or not 2 <= len(support_type.strip()) <= 100:
            codes.append("D009")
            reasons.append("support_type: required and must contain 2-100 characters")
    elif support_type is not None and (
        not isinstance(support_type, str) or not 2 <= len(support_type.strip()) <= 100
    ):
        codes.append("D010")
        reasons.append("support_type: when supplied, must contain 2-100 characters")

    if data["guardian_consent"] is not True:
        codes.append("D011")
        reasons.append("guardian_consent: must be true")
    if data["data_processing_consent"] is not True:
        codes.append("D012")
        reasons.append("data_processing_consent: must be true")

    country = data["country_code"]
    if not isinstance(country, str) or not COUNTRY_RE.fullmatch(country):
        codes.append("D013")
        reasons.append("country_code: exactly two uppercase letters required")

    organization = data["organization_id"]
    if not isinstance(organization, str) or not ORG_RE.fullmatch(organization):
        codes.append("D014")
        reasons.append("organization_id: 1-64 lowercase letters, numbers, or hyphen required")

    if reasons:
        return {"decision": "No", "codes": codes, "reasons": reasons}
    return {"decision": "Yes", "codes": [], "reasons": []}

