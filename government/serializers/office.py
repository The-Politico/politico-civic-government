from government.models import Office
from rest_framework import serializers


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = (
            'id',
            'uid',
            'slug',
            'name',
            'label',
            'short_label',
            'division',
            'jurisdiction',
            'body',
        )
