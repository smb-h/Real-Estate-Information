from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from app.api.serializers import PropertySerializer
from app.models import Property

User = get_user_model()


class PropertyViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    lookup_field = "id"

    # def get_queryset(self, *args, **kwargs):
        # return self.queryset.filter(id=self.request.user.id)
        # return self.queryset.all()

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = PropertySerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

