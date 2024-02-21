from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [
        "email",
        "first_name",
        "last_name",
        "is_admin",
        "is_superuser",
    ]
    list_filter = ["is_admin"]
    search_fields = ["email", "first_name", "last_name"]
    ordering = ["first_name", "last_name"]
    filter_horizontal = ["groups", "user_permissions"]
    readonly_fields = ["uuid", "last_login"]
    fieldsets = (
        ("Authentication", {
            "fields": (
                "email",
                "password",
            )
        }),
        (("Personal Info"), {
            "fields": (
                "uuid",
                "first_name",
                "last_name",
            )
        }),
        (("Permissions"), {
            "fields": (
                "is_active",
                "is_admin",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        (("Important dates"), {
            "fields": ("last_login", )
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields["is_superuser"].disabled = True
        return form
