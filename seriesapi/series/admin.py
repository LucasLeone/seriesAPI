"""Series admin."""

# Django
from django.contrib import admin

# Model
from seriesapi.series.models import Serie, Season, Episode


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    """Serie admin."""

    list_display = ['title', 'release', 'image']
    list_display_links = ['title']
    search_fields = ['title',]


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    """Season admin."""

    list_display = ['title', 'serie']
    list_display_links = ['title',]
    search_fields = ['title', 'serie']


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    """Episode admin."""

    list_display = ['title', 'season', 'image']
    list_display_links = ['title']
    search_fields = ['title',]