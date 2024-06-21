from django.contrib import admin
from .models import App2

# Register your models here.
#admin.site.register(App2)
@admin.register(App2)
class App2Admin(admin.ModelAdmin):
    list_display = ('nombre',)
