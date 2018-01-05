from government.models import Jurisdiction
from government.serializers import (JurisdictionSerializer,
                                    SlimJurisdictionSerializer)
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser


class JurisdictionViewSet(viewsets.ModelViewSet):
    queryset = Jurisdiction.objects.all()
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)

    def get_serializer_class(self):
        if self.action == 'list':
            return SlimJurisdictionSerializer
        else:
            return JurisdictionSerializer
