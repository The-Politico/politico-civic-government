# Imports from other dependencies.
from rest_framework import serializers


# Imports from government.
from government.models import Office


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = "__all__"
