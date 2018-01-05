from government.models import Office
from rest_framework import serializers


class SlimOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = (
            'id',
            'name',
        )
