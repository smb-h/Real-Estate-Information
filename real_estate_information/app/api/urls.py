from django.urls import path
from app.api.views import PropertyUpdateAPI, PropertyListAPIView


app_name = "App"
urlpatterns = [
    path('', PropertyListAPIView.as_view(), name = "list_api"),
    # Update DB
    path('Update-DB/', PropertyUpdateAPI.as_view(), name = "update_db_api"),
]


