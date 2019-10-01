from django.contrib import admin
from webapp.models import ToDo, Status, Type


class TodoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'summary', 'created_at']
    list_filter = ['status', 'type']
    list_display_links = ['pk', 'summary']
    search_fields = ['summary', 'status', 'type']
    exclude = []
    readonly_fields = ['created_at']


admin.site.register(ToDo, TodoAdmin)
admin.site.register(Status)
admin.site.register(Type)

