from django.contrib import admin
from django.urls import path
from lobhunter.api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
