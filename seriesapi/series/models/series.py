"""Series models."""

# Django
from django.db import models

# Utilities
from seriesapi.utils.models import SeriesAPIModel
from django.utils import timezone


class Serie(SeriesAPIModel):
    """Serie model."""

    title = models.CharField('Series title', max_length=250)
    release = models.DateField('Release date', default=timezone.now())
    description = models.TextField('Series description', blank=True, null=True)
    image = models.ImageField('Series image', upload_to='series/images/')

    def __str__(self):
        """Return series title."""
        return self.title


class Season(SeriesAPIModel):
    """Season model."""

    title = models.CharField('Season title', max_length=250)

    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)

    def __str__(self):
        """Return season title and serie."""
        return f'{self.serie}: {self.title}'


class Episode(SeriesAPIModel):
    """Episode model."""

    title = models.CharField('Episode title', max_length=250)

    video = models.URLField()
    image = models.ImageField('Episode image', upload_to='episodes/images/')

    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        """Return episode title, season title and serie."""
        return f'{self.season.serie}: {self.season}: {self.title}'