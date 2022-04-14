from django.urls import path

from measurement.views import demo

urlpatterns = [
    path('demo/', demo),
]


