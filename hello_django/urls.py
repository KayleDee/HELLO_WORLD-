from django.contrib import admin
from django.urls import path

from app.views import hello_view

# Request === work === Response

urlpatterns = [
    path("hello/", hello_view),
    path("admin/", admin.site.urls),
]
