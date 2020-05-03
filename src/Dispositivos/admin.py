from django.contrib import admin

# Register your models here.
from .models import Movil


class AdminMovil(admin.ModelAdmin):
    list_display = ["marca", "modelo", "SO"]
    search_fields = ["marca", "modelo"]
    list_filter = ["marca"]

    class Meta:
        model = Movil


admin.site.register(Movil, AdminMovil)
