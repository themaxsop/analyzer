from django.urls import path, include
from .views import upload_create

urlpatterns = [
    path('', upload_create, name="upload.create"),
]
