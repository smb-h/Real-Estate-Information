from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics
from app.api.serializers import PropertySerializer
from app.models import Property
from rest_framework.views import APIView
from app.utils.scrap_kilid import scrap_kilid
from app.utils.scrap_melkana import scrap_melkana
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# Permissions
from rest_framework.permissions import (
											AllowAny,
                                            IsAuthenticated,
                                            IsAdminUser,
                                            IsAuthenticatedOrReadOnly,
                                        )
User = get_user_model()


class PropertyListAPIView(generics.ListAPIView):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    permission_classes = [AllowAny]
    lookup_field = "id"
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter,)
    search_fields = ('area', 'sector', 'url')


class PropertyUpdateAPI(APIView):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    permission_classes = [AllowAny]
    lookup_field = "id"

    # GET
    def get(self, request, *args, **kwargs):
        context = {}
        queryset = Property.objects.all()
        # delete old data
        for prop in queryset:
            prop.delete()
        print("All items deleted.")
        # update kilid
        print("Retrieve Kilid data ...")
        kilid_rs = scrap_kilid()
        for home in kilid_rs:
            ppt = Property.objects.create(
                area = float(home.get("floorArea", 0.0)),
                sector = home.get("sector", ""),
                url = home.get("url", "https://kilid.com/")
            )
            ppt.save()
        print("Kilid data was saved successfully.")
        # update melkana
        print("Retrieve Melkana data ...")
        melkana_rs = scrap_melkana()
        for home in melkana_rs:
            ppt = Property.objects.create(
                area = float(home.get("floorArea", 0.0)),
                sector = home.get("sector", ""),
                url = home.get("url", "https://www.melkana.com/")
            )
            ppt.save()
        print("Melkana data was saved successfully.")
        # Redirect to a success page.
        return Response(context, status = status.HTTP_200_OK)

