from django.contrib import admin
from .models import *
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered


class ProduitAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Produit._meta.get_fields()]
admin.site.register(Produit, ProduitAdmin)

class CollecteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Collecte._meta.get_fields()]
admin.site.register(Collecte, CollecteAdmin)

class CollecteproduitAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CollecteProduit._meta.get_fields()]
admin.site.register(CollecteProduit, CollecteproduitAdmin)

class AchatAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Achat._meta.get_fields()]
admin.site.register(Achat, AchatAdmin)

class CspAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Csp._meta.get_fields()]
admin.site.register(Csp, CspAdmin)

class MagasinAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Magasin._meta.get_fields()]
admin.site.register(Magasin, MagasinAdmin)