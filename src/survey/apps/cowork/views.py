"""Cowork survey views"""

from django.views.generic import CreateView

from .models import Application


class ApplicationCreateView(CreateView):
    """Application create view"""

    model = Application
    fields = "__all__"
