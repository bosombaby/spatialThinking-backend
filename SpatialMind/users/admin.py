from django.contrib import admin
from .models import Profile, Role

# 修改管理后台头部的标题
admin.site.site_header = "Spatial Thinking Admin"

# 修改管理后台的URL
admin.site.site_url = "/admin/"

# 修改管理后台首页的标题
admin.site.index_title = "空间思维训练平台"
admin.site.site_title = "欢迎您"

admin.site.site_logo = "path:custom_logo.png"

# Register your models here.
admin.site.register(Role)
admin.site.register(Profile)
