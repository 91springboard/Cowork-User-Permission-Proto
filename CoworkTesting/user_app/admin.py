from django.contrib import admin

# Register your models here.
from user_app.models import CoworkUser, Hub
from django.contrib.auth.models import Permission


class CoworkUserAdmin(admin.ModelAdmin):
    filter_horizontal = ('hubs',)
    list_display = ('username',)

    def username(self, obj):
        return obj.user.username

    def has_change_permission(self, request, obj=None):
        """Returns true if the user has view permission"""
        if request.user.has_perm("user_app.view_coworkuser") or \
                request.user.has_perm("user_app.view_coworkuser"):
            return True
        else:
            return False


class HubAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',)
    list_filter = ('location',)
    search_fields = ['name', 'location']


admin.site.register(CoworkUser, CoworkUserAdmin)
admin.site.register(Hub, HubAdmin)
admin.site.register(Permission)
