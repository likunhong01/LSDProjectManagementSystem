from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count,Sum
from lsd import models


# Create your views here.
# 登录函数
def login(request):
    responses = []
    response = {}
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        name = request.POST.get("user_name")
        password = request.POST.get("password")
        try:
            user = models.User.objects.get(user_name=name)
        except Exception :
            response['msg'] = "fail"
            responses.append(response)
            return JsonResponse(data=responses, safe=False)
        else:
            if password == user.password:
                if user.authority == "root":
                    response['msg'] = 'success'
                    responses.append(response)
                    return render(request, 'boss_index.html')
                else:
                    response['msg'] = 'success'
                    responses.append(response)
                    return render(request, 'salesman_index.html')


# 查看业务员列表
def all_salesman(request):
    responses = []
    response = {}
    if request.method == "GET":
        users = models.User.objects.filter(authority="nroot")
        for user in users:
            response['user_name'] = user.user_name
            response['telephone'] = user.telephone
            responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 查看单个业务员项目个数
def get_project_count(request):
    responses = []
    response = {}
    if request.method == "GET":
        count = 0
        name = request.GET.get("user_name")
        user_id = models.User.objects.GET(user_name=name)
        projects = models.UserProject.objects.filter(user_id=user_id)
        for project in projects:
            count += 1
        response['count'] = count
        responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 查看项目列表
def all_project(request):
    responses = []
    response = {}
    duty = {}
    if request.method == "GET":
        projects = models.Project.objects.filter(effective=0)
        for project in projects:
            response['project_id'] = project.project_id
            response['project_name'] = project.project_name
            response['time'] = project.time
            users = models.UserProject.objects.filter(pro_id=project.project_id)
            for user in users:
                user_name = models.User.objects.filter(user_id=user.user_id)
                duty.append(user_name)
            response['user'] = duty
            responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 添加业务员
def add_salesman(request):
    responses = []
    response = {}
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")

        models.User.objects.create(user_name=user_name, password=password)
        response['msg'] = "success"
        responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 删除业务员
def del_salesman(request):
    responses = []
    response = {}
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user = models.User.objects.filter(user_name=user_name)
        user.delete()
        response['msg'] = "success"
        responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 业务员的负责项目查询
def search_with_salesman(request):
    responses = []
    response = {}
    duty = []
    if request.method == "GET":
        name = request.GET.get("user_name")
        user_id = models.User.objects.GET(user_name=name)
        projects_id = models.UserProject.objects.filter(user_id=user_id)
        for project_id in projects_id:
            project = models.Project.objects.filter(project_id=project_id, effective=0)
            response['project_id'] = project_id
            response['project_name'] = project.project_name
            response['time'] = project.time
            users = models.UserProject.objects.filter(pro_id=project_id)
            for user in users:
                user_name = models.User.objects.filter(user_id=user.user_id)
                duty.append(user_name)
            response['user'] = duty
            responses.append(response)
        return JsonResponse(data=responses, safe=False)

# 项目搜索


# 添加项目
def add_project(request):
    responses = []
    response = {}
    if request.method == "PUT":
        project_name = request.POST.get("project_name")
        source = request.POST.get("source")
        introduction = request.POST.get("introduction")
        contacts = request.POST.get("contacts")
        telephone = request.POST.get("telephone")
        models.Project.objects.create(project_name=project_name, source=source,
                                      introduction=introduction, contacts=contacts, telephone=telephone)
        response['msg'] = "success"
        responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 删除项目
def del_project(request):
    responses = []
    response = {}
    if request.method == "POST":
        project_id = request.POST.get("project_id")
        project = models.Project.objects.filter(project_id=project_id)
        project.delete()
        response['msg'] = "success"
        responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 查看单个项目详细信息
def single_project_detail(request):
    responses = []
    response = {}
    if request.method == "GET":
        project_id = request.GET.get("project_id")
        project = models.Project.objects.filter(project_id=project_id)
        response["project_name"] = project.project_name
        response["source"] = project.source
        response["introduction"] = project.introduction
        response["contacts"] = project.contacts
        response["telephone"] = project.telephone
        responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 查看单个项目汇报记录
def single_project_report(request):
    responses = []
    if request.method == "GET":
        project_id = request.GET.get("project_id")
        project = models.Project.objects.filter(project_id=project_id)
        reports = models.Report.objects.filter(project_id=project_id)
        for report in reports:
            response = {}
            response["report_id"] = report.report_id
            response["project_name"] = project.project_name
            response["reporter"] = report.reporter
            response["time"] = report.time
            responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 查看单个项目的老板留言
def single_project_record(request):
    responses = []
    if request.method == "GET":
        report_id = request.GET.get("report_id")
        messages = models.Message.objects.filter(report_id=report_id)
        for message in messages:
            response = {}
            response["content"] = message.content
            response["time"] = message.time
            responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 留言
def record(request):
    responses = []
    response = {}
    if request.method == "PUT":
        report_id = request.POST.get("report_id")
        content = request.POST.get("content")
        models.Message.objects.create(report_id=report_id, content=content)
        response['msg'] = "success"
        responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 查看单个汇报
def get_report(request):
    responses = []
    response = {}
    if request.method == "GET":
        report_id = request.GET.get("report_id")
        report = models.Report.objects.filter(report_id=report_id)
        project = models.Project.objects.filter(project_id=report.project_id)
        response["project_name"] = project.project_name
        response["progress"] = report.progress
        response["workable"] = report.workable
        response["supply"] = report.supply
        response["capital"] = report.capital
        response["invoice"] = report.invoice
        response["other"] = report.other
        responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 添加汇报
def add_report(request):
    responses = []
    response = {}
    if request.method == "PUT":
        report_id = request.POST.get("report_id")
        project_id = request.POST.get("project_id")
        progress = request.POST.get("progress")
        workable = request.POST.get("workable")
        supply = request.POST.get("supply")
        capital = request.POST.get("capital")
        invoice = request.POST.get("invoice")
        other = request.POST.get("other")
        models.Report.objects.create(report_id=report_id, project_id=project_id, progress=progress,
                                     workable=workable, supply=supply, capital=capital, invoice=invoice, other=other)
        response['msg'] = "success"
        responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 查看老板给业务员的消息
def get_ones_record(request):
    responses = []
    if request.method == "GET":
        user_name = request.GET.get("user_name")
        user = models.User.objects.filter(user_name=user_name)
        user_id = user.user_id
        project_ids = models.UserProject.objects.filter(user_id=user_id)
        for project_id in project_ids:
            project = models.Project.objects.filter(project_id=project_id, effective=0)
            reports = models.Report.objects.filter(project_id=project.project_id)
            for report in reports:
                try:
                    message = models.Message.objects.get(report_id=report.report_id)
                except Exception:
                    continue
                else:
                    response = {}
                    response["message"] = message.content
                    response["time"] = message.time
                    response["project_id"] = project.project_id
                    responses.append(response)
        return JsonResponse(data=responses, safe=False)
