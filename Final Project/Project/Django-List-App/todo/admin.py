"""
Created: November 18, 2022
"""
from django.contrib import admin

from .models import Todo

admin.site.register(Todo)