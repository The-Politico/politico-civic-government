from government.models import Body
from rest_framework import serializers


class SlimBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = (
            'id',
            'uid',
            'jurisdiction',
        )
