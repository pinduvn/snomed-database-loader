from django.contrib import admin
from django_snomed.models import DescriptionF
# Register your models here.


@admin.register(DescriptionF)
class ProductoAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        'term_reducido',
    )
    date_hierarchy = 'effectivetime'
    #ordering = ['term']  # -nombre escendente, nombre ascendente
    search_fields = [
        'term'
        ]
    list_filter = (
        'languagecode',
        'active',
    )


from django.apps import apps
models = apps.get_models()
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
