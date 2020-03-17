from rest_framework import serializers

from app.models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ["area", "sector", "url", "created"]



