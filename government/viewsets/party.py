from government.models import Party
from government.serializers import PartySerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)
    serializer_class = PartySerializer
