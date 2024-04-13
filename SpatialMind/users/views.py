from django.http import HttpResponse
from rest_framework.response import Response
from APIHandler.MyHttpResponse import MyAPIResponse


def hello(request):
    return HttpResponse("你好，这里是用户操作接口")


# 用户注册需求
def register(request):
    return HttpResponse("你好，这里是用户注册接口")


# 用户登录需求
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
    return MyAPIResponse(200, 'success', []).to_json()
