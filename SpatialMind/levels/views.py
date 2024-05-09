import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Level,Question
from rest_framework.decorators import api_view, authentication_classes, permission_classes


# 获取关卡的题目
@api_view(['POST'])
def getLevelsQuestion(request):
    data = json.loads(request.body)
    level_id = int(data['level_id'])
    subject_id = int(data['subject_id'])


