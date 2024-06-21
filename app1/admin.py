from django.contrib import admin
from .models import App1

# Register your models here.
#admin.site.register(App1)
@admin.register(App1)
class App1Admin(admin.ModelAdmin):
    list_display = ('nombre','pais', 'edad',)
    list_filter = ('edad',)
    search_fields = ('nombre','pais',)
    #fields = ('nombre',)