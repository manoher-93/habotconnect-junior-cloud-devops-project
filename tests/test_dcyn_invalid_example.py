# Candidate: Manoher Singh | manoharmsp93@gmail.com | +91-9648548275
# HabotConnect Hiring Project — explicit invalid example test

import unittest

from src.dcyn import evaluate_onboarding


class InvalidExampleTests(unittest.TestCase):
    def test_sample_invalid_payload_is_rejected_with_multiple_reasons(self):
        payload = {
            "student_id": "not-a-uuid",
            "parent_email": "parent@example.com",
            "student_name": "Aarav Singh",
            "date_of_birth": "2014-05-12",
            "requires_learning_support": True,
            "support_type": "Reading support",
            "guardian_consent": False,
            "data_processing_consent": True,
            "country_code": "ae",
            "organization_id": "habot-demo",
        }
        result = evaluate_onboarding(payload)
        self.assertEqual(result["decision"], "No")
        self.assertIn("D003", result["codes"])
        self.assertIn("D011", result["codes"])
        self.assertIn("D013", result["codes"])


if __name__ == "__main__":
    unittest.main()
