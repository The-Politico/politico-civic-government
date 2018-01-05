from government.models import Office
from government.serializers import OfficeSerializer, SlimOfficeSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)

    def get_serializer_class(self):
        if self.action == 'list':
            return SlimOfficeSerializer
        else:
            return OfficeSerializer
