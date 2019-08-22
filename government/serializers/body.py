# Imports from other dependencies.
from rest_framework import serializers


# Imports from government.
from government.models import Body


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = "__all__"
