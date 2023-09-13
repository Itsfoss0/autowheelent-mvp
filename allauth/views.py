#!/usr/bin/env python3

"""
Views Related to social accounts
"""

from django.http import HttpResponse

def social_account(request):
    """
    First view
    """
    return HttpResponse("Social accounts....coming soon")