# Candidate: Manoher Singh | manoharmsp93@gmail.com | +91-9648548275
# HabotConnect Hiring Project — DCYN tests

import unittest

from src.dcyn import evaluate_onboarding


VALID = {
    "student_id": "550e8400-e29b-41d4-a716-446655440000",
    "parent_email": "parent@example.com",
    "student_name": "Aarav Singh",
    "date_of_birth": "2014-05-12",
    "requires_learning_support": True,
    "support_type": "Reading support",
    "guardian_consent": True,
    "data_processing_consent": True,
    "country_code": "AE",
    "organization_id": "habot-demo",
}


class DCYNTests(unittest.TestCase):
    def test_valid_payload_is_yes(self):
        result = evaluate_onboarding(VALID)
        self.assertEqual(result["decision"], "Yes")
        self.assertEqual(result["codes"], [])
        self.assertEqual(result["reasons"], [])

    def test_missing_consent_is_no(self):
        payload = dict(VALID)
        payload["guardian_consent"] = False
        result = evaluate_onboarding(payload)
        self.assertEqual(result["decision"], "No")
        self.assertIn("D011", result["codes"])

    def test_support_type_is_required(self):
        payload = dict(VALID)
        payload.pop("support_type")
        result = evaluate_onboarding(payload)
        self.assertEqual(result["decision"], "No")
        self.assertIn("D009", result["codes"])

    def test_country_code_is_strict(self):
        payload = dict(VALID)
        payload["country_code"] = "ae"
        result = evaluate_onboarding(payload)
        self.assertEqual(result["decision"], "No")


    def test_invalid_uuid_is_no(self):
        payload = dict(VALID)
        payload["student_id"] = "not-a-uuid"
        result = evaluate_onboarding(payload)
        self.assertEqual(result["decision"], "No")
        self.assertIn("D003", result["codes"])

    def test_unknown_field_is_no(self):
        payload = dict(VALID)
        payload["unexpected"] = "value"
        result = evaluate_onboarding(payload)
        self.assertEqual(result["decision"], "No")
        self.assertIn("D001", result["codes"])

    def test_support_type_is_validated_when_optional(self):
        payload = dict(VALID)
        payload["requires_learning_support"] = False
        payload["support_type"] = ""
        result = evaluate_onboarding(payload)
        self.assertEqual(result["decision"], "No")

if __name__ == "__main__":
    unittest.main()
