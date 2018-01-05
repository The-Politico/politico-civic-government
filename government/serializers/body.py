from government.models import Body
from rest_framework import serializers


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = (
            'id',
            'uid',
            'slug',
            'label',
            'short_label',
            'organization',
            'jurisdiction',
            'parent',
        )
