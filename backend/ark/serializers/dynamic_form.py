from rest_framework import serializers
from ..models.dynamic_form import DynamicFormSubmission


class DynamicFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicFormSubmission
        fields = ["name", "data", "submitted_at"]
        read_only_fields = ["submitted_at"]
