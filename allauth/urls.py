#!/usr/bin/env python3

"""
URLs related to social auth
"""

from django.urls import path
from allauth.views import social_account


urlpatterns = [
    path('', social_account, name="social")
]