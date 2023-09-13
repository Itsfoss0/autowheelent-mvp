#!/usr/bin/env python3

"""
URLS for the landing pages
"""

from django.urls import path
from pages.views import home

urlpatterns = [
    path('', home, name="home")
]