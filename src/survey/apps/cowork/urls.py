"""Urls for the Cowork app"""

from django.urls import path

from .views import ApplicationCreateView

urlpatterns = [
    path("application/", ApplicationCreateView.as_view(), name="application-create"),
]
