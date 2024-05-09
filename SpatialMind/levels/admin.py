from django.contrib import admin
from .models import Subject, Badge, Level, Question

admin.site.register([Subject, Badge, Level, Question])
