from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from users.api.views import UserViewSet
from app.api.views import PropertyViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("users", UserViewSet)
router.register("app", PropertyViewSet)


app_name = "API"
urlpatterns = router.urls

