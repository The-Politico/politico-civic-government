from government.models import Body
from government.serializers import BodySerializer, SlimBodySerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser


class BodyViewSet(viewsets.ModelViewSet):
    queryset = Body.objects.all()
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)

    def get_serializer_class(self):
        if self.action == 'list':
            return SlimBodySerializer
        else:
            return BodySerializer
