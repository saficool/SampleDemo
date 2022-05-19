from rest_framework.generics import (ListCreateAPIView)
from rest_framework.permissions import AllowAny
from organization.models import Organization
from . import serializer


class OrganizationAPI(ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = serializer.OrganizationSerializer
    permission_classes = [AllowAny]
