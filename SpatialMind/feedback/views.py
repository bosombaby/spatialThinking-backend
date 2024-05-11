import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import ChallengeRecord, Scoring
from rest_framework.decorators import api_view
from APIHandler.MyHttpResponse import MyAPIResponse
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


# 分数 => 评估 => 评价

def get_scoring_standard(score):
    objects = Scoring.objects.all()
    for item in objects:
        parts = item.score_range.split('-')
        low_score = int(parts[0])
        high_score = int(parts[1])
        if low_score <= score <= high_score:
            return item.scoring_id
    return None


# TODO：一个关卡多条闯关记录，根据时间线回溯
# 创建闯关记录，目前生成单条记录，先查询，如果有就修改
@api_view(['POST'])
def createRecord(request):
    data = json.loads(request.body)
    user_id = int(data['user_id'])
    level_id = int(data['level_id'])
    result = data['result']
    answer = data['answer']
    score = int(data['score'])

    # 先判断能否查到 对象
    operate = '更新成功'
    try:
        record = ChallengeRecord.objects.get(user_id=user_id, level_id=level_id)
    except ObjectDoesNotExist:
        operate = '添加成功'
        record = ChallengeRecord()
    except MultipleObjectsReturned:
        return MyAPIResponse(500, '找到了多个挑战记录，这不应该发生', [], False).to_json()

    record.user_id = user_id
    record.level_id = level_id
    record.result = result
    record.answer = answer
    record.score = score

    scoring_id = get_scoring_standard(score)
    if scoring_id is not None:
        record.scoring_id = scoring_id

    record.save()
    return MyAPIResponse(200, operate, [], True).to_json()

# # 获取闯关记录
# @api_view(['POST'])
# def getRecord(request):
#
