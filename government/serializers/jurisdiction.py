# Imports from other dependencies.
from rest_framework import serializers


# Imports from government.
from government.models import Jurisdiction


class JurisdictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jurisdiction
        fields = "__all__"
