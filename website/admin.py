from django.contrib import admin

from website.models import Setting


class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    ordering = ('name',)


admin.site.register(Setting, SettingAdmin)
