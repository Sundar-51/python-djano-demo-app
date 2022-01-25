from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

def filter(request):
    queryset_list = Jobsearch.objects.all().order_by('job_id')
    
    skilllist = request.GET.get('skillsets', None)
    locationParams = request.GET.getlist('location', None)
    jobParams = request.GET.getlist('job_roles', None)
    degreeParams = request.GET.getlist('degree', None)
    deptParams = request.GET.getlist('dept', None)
    passout1Params = request.GET.get('yop_from', None)
    passout2Params = request.GET.get('yop_to', None)
    collocParams = request.GET.getlist('c_city', None)
    colnameParams = request.GET.getlist('collegename', None)
    marks = request.GET.getlist('marks',None)
    gender = request.GET.getlist('gender', None)
    jobtype = request.GET.getlist('jt', None)
    exp = request.GET.getlist('exp_from', None)
    salary = request.GET.getlist('salary_from', None)

    if skilllist:
        skillParams = skilllist.split(',')
        queryset_list = queryset_list.filter(skillset__in=skillParams)
    if locationParams:
        queryset_list = queryset_list.filter(location__in=locationParams)
    if jobParams:
        queryset_list = queryset_list.filter(job__in=jobParams)
    if degreeParams:
        queryset_list = queryset_list.filter(description__in=['B.Arch'])
    if deptParams:
        queryset_list = queryset_list.filter(degree__in=deptParams)
    if collocParams:
        queryset_list = queryset_list.filter(collegelocation__in=collocParams)
    if colnameParams:
        queryset_list = queryset_list.filter(collegename__in=colnameParams)
    if marks:
        queryset_list = queryset_list.filter(marks__in=marks)
    if gender:
        queryset_list = queryset_list.filter(gender__in=gender)
    if passout1Params:
        queryset_list = queryset_list.filter(passin__gte = passout1Params)
    if passout2Params:
        queryset_list = queryset_list.filter(collegelocation__lte = passout2Params)
    if jobtype:
        queryset_list = queryset_list.filter(jobtype__in=jobtype)
    if exp:
        queryset_list = queryset_list.filter(exp__in=exp)
    if salary:
        queryset_list = queryset_list.filter(salary__in=salary)
    
    return queryset_list

def JobList(request):
    qs = filter(request)
   
    pagesize = request.GET.get("per_page")
    
    if pagesize:
        paginator = Paginator(qs, int(pagesize))
    else:
        paginator = Paginator(qs, 10)
    page = request.GET.get('page', 1)
    productss = paginator.get_page(page)
    
    context = {
        'joblist': productss,
        'pagesize': pagesize
    }
    
    return render(request, "Fieldsearch.html", context)