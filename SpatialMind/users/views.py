import json
from datetime import date
from .models import Profile
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from APIHandler.MyHttpResponse import MyAPIResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


def hello(request):
    return HttpResponse("你好，这里是用户操作接口")


# 用户注册需求
@api_view(['POST'])
def register(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    user = User.objects.filter(username=username)
    if user is not None:
        user = User.objects.create_user(username, '', password)
        user.save()
        return MyAPIResponse(200, '注册成功', [], True).to_json()
    else:
        return MyAPIResponse(404, '用户名已存在', [], False).to_json()


# 用户登录需求
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    user = authenticate(request, username=username, password=password)
    print("Welcome", user)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return MyAPIResponse(200, '登录成功', {
            "id": user.id,
            "username": user.username,
            "roles": ["admin"],
            "accessToken": str(refresh.access_token),
            "refreshToken": str(refresh),
            "expires": "2030/10/30 00:00:00"
        }, True).to_json()
    else:
        return MyAPIResponse(404, '账号或密码错误', [], False).to_json()


# 获取用户信息
@api_view(['POST'])
def getUserInfo(request):
    data = json.loads(request.body)
    user_id = data.get('userId')
    user = User.objects.get(pk=user_id)
    if user is not None:
        return MyAPIResponse(200, '查询成功', {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "last_login": user.last_login.strftime('%Y-%m-%d %H:%M:%S'),
            "nickname": user.profile.nickname,

            "roles": ["admin"]
        }, True).to_json()
    else:
        return MyAPIResponse(404, '未查询到用户', [], False).to_json()


routes = {
    "path": "/permission",
    "meta": {
        "title": "权限管理",
        "icon": "ep:lollipop",
        "rank": 10
    },
    "children": [
        {
            "path": "/permission/page/index",
            "name": "PermissionPage",
            "meta": {
                "title": "页面权限",
                "roles": ["admin", "common"]
            }
        },
        {
            "path": "/permission/button/index",
            "name": "PermissionButton",
            "meta": {
                "title": "按钮权限",
                "roles": ["admin", "common"],
                "auths": [
                    "permission:btn:add",
                    "permission:btn:edit",
                    "permission:btn:delete"
                ]
            }
        }
    ]
}


@api_view(['GET'])
def getAsyncRoutes(request):
    return MyAPIResponse(200, '登录成功', [routes], True).to_json()
