# Imports from other dependencies.
from rest_framework import serializers


# Imports from government.
from government.models import Party


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = "__all__"
