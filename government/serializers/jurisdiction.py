from government.models import Jurisdiction
from rest_framework import serializers


class JurisdictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jurisdiction
        fields = (
            'id',
            'uid',
            'slug',
            'name',
            'division',
            'parent',
        )
