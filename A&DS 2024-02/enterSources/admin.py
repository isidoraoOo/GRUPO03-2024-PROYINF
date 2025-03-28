from django.contrib import admin
from enterSources.models import Sources, Cat_x_Source, Categories

# Register your models here.

# Permite realizar una busqueda por 'link' o por fecha en que se ingreso el link.
# Ademas de agregar un cuadro para filtrar por un rango fecha.
class SourcesAdmin(admin.ModelAdmin):
    list_display=("link", "created_at")
    search_fields=("link", "created_at",)
    list_filter=("created_at",)

# Agrega un cuadro para filtrar los elementos según la categoria.
class CategoriesAdmin(admin.ModelAdmin):
    list_filter=("category",)

admin.site.register(Sources, SourcesAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Cat_x_Source)