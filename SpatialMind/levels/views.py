import json
from django.shortcuts import render
from django.http import HttpResponse
from APIHandler.MyHttpResponse import MyAPIResponse
from .models import Level, Question
from rest_framework.decorators import api_view, authentication_classes, permission_classes


# 获取关卡的题目
@api_view(['POST'])
def getLevelsQuestion(request):
    data = json.loads(request.body)
    level_id = int(data['level_id'])
    subject_id = int(data['subject_id'])
    level = Level.objects.get(level_id=level_id, subject_id=subject_id)
    if level is not None:
        questions_list = list(
            level.question.all().values('question_id', 'level_id', 'content', 'answer', 'option_a', 'option_b',
                                        'option_c', 'option_d', 'solution'))
        badge = level.badge

        return MyAPIResponse(200, '查询成功', {
            'level_id': level.level_id,
            'level_name': level.level_name,
            'description': level.description,
            'question': questions_list,
            "badge": {
                'badge_id': badge.badge_id,
                'name': badge.name,
                'description': badge.description,
                'content': badge.content,
                # 'local_link': badge.local_link,
                'online_link': badge.online_link,
                'acquired_count': badge.acquired_count
            }

        }, True).to_json()
    else:
        return MyAPIResponse(404, '查询失败', [], False).to_json()
