import json
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from APIHandler.MyHttpResponse import MyAPIResponse


def hello(request):
    return HttpResponse("你好，这里是用户操作接口")


# 用户注册需求
def register(request):
    return HttpResponse("你好，这里是用户注册接口")


# 用户登录需求
def login(request):
    print(request)
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        print("Welcome", user)
        if user is not None:
            return MyAPIResponse(200, '登录成功', [], True).to_json()
        else:
            return MyAPIResponse(404, '账号或密码错误', [], False).to_json()

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
def getAsyncRoutes(request):
    return MyAPIResponse(200, '登录成功', [routes], True).to_json()