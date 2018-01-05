from government.models import Party
from rest_framework import serializers


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = (
            'id',
            'uid',
            'slug',
            'label',
            'short_label',
            'organization',
            'ap_code',
            'aggregate_candidates',
        )
