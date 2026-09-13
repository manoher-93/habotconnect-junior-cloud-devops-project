# Candidate: Manoher Singh | manoharmsp93@gmail.com | +91-9648548275
# HabotConnect Hiring Project — serializer tests

import unittest
import secrets

from django.conf import settings

if not settings.configured:
    settings.configure(
        SECRET_KEY=secrets.token_urlsafe(32),
        INSTALLED_APPS=["rest_framework"],
        REST_FRAMEWORK={},
        USE_TZ=True,
        DEFAULT_CHARSET="utf-8",
    )

import django

django.setup()

from src.serializers import StudentOnboardingSerializer


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


class SerializerTests(unittest.TestCase):
    def test_valid_payload(self):
        serializer = StudentOnboardingSerializer(data=VALID)
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_invalid_consent(self):
        payload = dict(VALID)
        payload["data_processing_consent"] = False
        serializer = StudentOnboardingSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertIn("data_processing_consent", serializer.errors)

    def test_support_type_required(self):
        payload = dict(VALID)
        payload.pop("support_type")
        serializer = StudentOnboardingSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertIn("support_type", serializer.errors)


if __name__ == "__main__":
    unittest.main()
