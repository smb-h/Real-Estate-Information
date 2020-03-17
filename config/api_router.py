from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import include, path
from users.api.views import UserViewSet


# https://www.django-rest-framework.org/api-guide/routers/

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("users", UserViewSet)
# router.register("App", PropertyViewSet)


app_name = "API"
urlpatterns = router.urls
urlpatterns += [
    # App
    path("App/", include("app.api.urls", namespace="App")),
]

