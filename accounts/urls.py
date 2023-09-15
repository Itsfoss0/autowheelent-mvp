#!/usr/bin/env python3
"""
Urls related to user accounts
"""

from django.urls import path
from accounts.views import account


urlpatterns = [
    path('', account, name="account")
]
