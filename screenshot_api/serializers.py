from rest_framework import serializers
from screenshot_api.models import Screenshot


class ScreenshotSerializer(serializers.ModelSerializer):
    """Serializer for the Screenshot."""

    class Meta:
        """Meta class for Screenshot Serializer."""

        model = Screenshot
        fields = '__all__'
