from django.contrib import admin
from .models import Scoring, ChallengeRecord

admin.site.register([Scoring, ChallengeRecord])
