"""Series views."""

# Django REST Framework
from rest_framework import generics

# Serializers
from seriesapi.series.serializers.series import (
    SerieModelSerializer,
    SeasonModelSerializer,
    EpisodeModelSerializer
)

# Models
from seriesapi.series.models.series import Serie, Season, Episode


class SeriesList(generics.ListAPIView):
    """Series list."""

    queryset = Serie.objects.all()
    serializer_class = SerieModelSerializer
