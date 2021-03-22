"""Admin for the cowork app"""

from django.contrib import admin

from . import models


@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    """Applications administration"""

    list_display = (
        "last_name",
        "first_name",
        "email",
        "city",
        "desired_role",
        "max_monthly_bill",
        "has_validated_email",
    )

    list_filter = (
        "city",
        "desired_role",
        "max_monthly_bill",
        "has_validated_email",
    )
