from government.models import Jurisdiction
from rest_framework import serializers


class SlimJurisdictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jurisdiction
        fields = (
            'id',
            'name',
        )
