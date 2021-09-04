"""Series URLs."""

# Django
from django.urls import path

# Views
from .views import series as series_views


urlpatterns = [
    path('series/', series_views.SeriesList.as_view()),
    # path('series/<int:pk>/', series_views.)
]