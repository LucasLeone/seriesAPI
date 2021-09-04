"""Series serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from seriesapi.series.models import Serie, Season, Episode


class SerieModelSerializer(serializers.ModelSerializer):
    """Serie model serializer."""

    seasons = serializers.StringRelatedField(many=True)

    class Meta:
        """Meta class."""

        model = Serie
        fields = '__all__'


class SeasonModelSerializer(serializers.ModelSerializer):
    """Season model serializer."""

    episodes = serializers.StringRelatedField(many=True)

    class Meta:
        """Meta class."""

        model = Season
        fields = '__all__'


class EpisodeModelSerializer(serializers.ModelSerializer):
    """Episode model serializer."""

    class Meta:
        """Meta class."""

        model = Episode
        fields = '__all__'