"""LSDProjectManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lsd import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('LSD/login/', views.login),  # 登录界面 判断身份
    path('LSD/all_salesman/', views.all_salesman),  # 查看业务员列表
    # path('LSD/get_project_count/', views.get_project_count),  # 查看单个业务员项目个数
    # path('LSD/all_project/', views.all_project),  # 查看项目列表
    # path('LSD/add_salesman/', views.add_salesman),  # 添加业务员
    # path('LSD/del_salesman/', views.del_salesman),  # 删除业务员
    # path('LSD/search_with_salesman/', views.search_with_salesman),  # 业务员的负责项目查询
    # path('LSD/search_project/', views.search_project),  # 项目搜索
    # path('LSD/add_project/', views.add_project),  # 添加项目
    # path('LSD/del_project/', views.del_project),  # 删除项目
    # path('LSD/single_project_detail/', views.single_project_detail),  # 查看单个项目详细信息
    # path('LSD/single_project_report/', views.single_project_report),  # 查看单个项目汇报记录
    # path('LSD/single_project_record/', views.single_project_record),  # 查看单个项目留言
    # path('LSD/record/', views.record),  # 留言
    # path('LSD/get_report/', views.get_report),  # 查看单个汇报
    # path('LSD/add_report/', views.add_report),  # 添加汇报
    # path('LSD/get_ones_record/', views.get_ones_record),  # 查看老板给业务员的消息
]
