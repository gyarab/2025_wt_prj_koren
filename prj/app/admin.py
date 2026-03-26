from django.contrib import admin
from .models import *


@admin.register(Znacka)
class ZnackaAdmin(admin.ModelAdmin):
    list_display = ("id", "nazev")
    search_fields = ("nazev",)


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ("id", "nazev", "znacka")
    search_fields = ("nazev",)
    list_filter = ("znacka",)


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ("id", "nazev", "model")
    search_fields = ("nazev",)
    list_filter = ("model",)


@admin.register(Motorizace)
class MotorizaceAdmin(admin.ModelAdmin):
    list_display = ("id", "typ", "auto")
    search_fields = ("typ",)
    list_filter = ("auto",)


@admin.register(Uzivatel)
class UzivatelAdmin(admin.ModelAdmin):
    list_display = ("id", "jmeno")
    search_fields = ("jmeno",)


@admin.register(Recenze)
class RecenzeAdmin(admin.ModelAdmin):
    list_display = ("id", "auto", "text")
    search_fields = ("text",)
    list_filter = ("auto",)


@admin.register(Komentar)
class KomentarAdmin(admin.ModelAdmin):
    list_display = ("id", "recenze", "text")
    search_fields = ("text",)
    list_filter = ("recenze",)


@admin.register(Hodnoceni)
class HodnoceniAdmin(admin.ModelAdmin):
    list_display = ("id", "hodnota", "auto", "uzivatel")
    list_filter = ("auto", "uzivatel")
