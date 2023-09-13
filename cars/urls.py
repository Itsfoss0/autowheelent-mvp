#!/usr/bin/env python3

"""
URLs related to cars
"""

from django.urls import path
from cars.views import cars


urlpatterns = [
    path('', cars, name='cars')
]