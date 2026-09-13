# Candidate: Manoher Singh | manoharmsp93@gmail.com | +91-9648548275
# HabotConnect Hiring Project — Django REST Framework serializer

"""Django REST Framework serializer for the explicit onboarding contract."""

from __future__ import annotations

from datetime import date

from rest_framework import serializers

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


class StudentOnboardingSerializer(serializers.Serializer):
    student_id = serializers.UUIDField()
    parent_email = serializers.EmailField(max_length=254)
    student_name = serializers.CharField(min_length=2, max_length=100, trim_whitespace=True)
    date_of_birth = serializers.DateField()
    requires_learning_support = serializers.BooleanField()
    support_type = serializers.CharField(
        min_length=2, max_length=100, trim_whitespace=True, required=False, allow_blank=False
    )
    guardian_consent = serializers.BooleanField()
    data_processing_consent = serializers.BooleanField()
    country_code = serializers.RegexField(regex=r"^[A-Z]{2}$")
    organization_id = serializers.RegexField(regex=r"^[a-z0-9-]{1,64}$")

    def to_internal_value(self, data):
        unknown = sorted(set(data) - ALLOWED_FIELDS)
        if unknown:
            raise serializers.ValidationError(
                {"non_field_errors": [f"Unknown field(s): {', '.join(unknown)}"]}
            )
        return super().to_internal_value(data)

    def validate_date_of_birth(self, value: date) -> date:
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if not 3 <= age <= 18:
            raise serializers.ValidationError("Student age must be between 3 and 18.")
        return value

    def validate(self, attrs):
        if attrs["requires_learning_support"] and "support_type" not in attrs:
            raise serializers.ValidationError(
                {"support_type": "This field is required when learning support is required."}
            )
        if not attrs["guardian_consent"]:
            raise serializers.ValidationError(
                {"guardian_consent": "Guardian consent must be true."}
            )
        if not attrs["data_processing_consent"]:
            raise serializers.ValidationError(
                {"data_processing_consent": "Data-processing consent must be true."}
            )
        return attrs
