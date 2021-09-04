"""Series serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from seriesapi.series.models import Serie, Season, Episode



class EpisodeModelSerializer(serializers.ModelSerializer):
    """Episode model serializer."""

    class Meta:
        """Meta class."""

        model = Episode
        fields = ('title', )


class SeasonModelSerializer(serializers.ModelSerializer):
    """Season model serializer."""

    episodes = EpisodeModelSerializer(many=True)

    class Meta:
        """Meta class."""

        model = Season
        fields = ('title', 'episodes')


class SerieModelSerializer(serializers.ModelSerializer):
    """Serie model serializer."""

    seasons = SeasonModelSerializer(many=True)

    class Meta:
        """Meta class."""

        model = Serie
        fields = ('title', 'description', 'seasons')


