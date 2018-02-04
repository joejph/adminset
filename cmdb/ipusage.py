#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from forms import IdcForm
from .models import Idc
from django.contrib.auth.decorators import login_required
from accounts.permission import permission_verify


@login_required()
@permission_verify()
def ipusage(request):
    temp_name = "cmdb/cmdb-header.html"
    ip_info = IPUsage.objects.all()
    return render(request, 'cmdb/ipusage.html', locals())


@login_required()
@permission_verify()
def idc_add(request):
    temp_name = "cmdb/cmdb-header.html"
    if request.method == "POST":
        idc_form = IdcForm(request.POST)
        if idc_form.is_valid():
            idc_form.save()
            tips = u"增加成功！"
            display_control = ""
        else:
            tips = u"增加失败！"
            display_control = ""
        return render(request, "cmdb/idc_add.html", locals())
    else:
        display_control = "none"
        idc_form = IdcForm()
        return render(request, "cmdb/idc_add.html", locals())

@login_required()
@permission_verify()
def idc_edit(request, ids):
    obj = Idc.objects.get(id=ids)
    allidc = Idc.objects.all()
    return render(request, "cmdb/idc_edit.html", locals())


@login_required()
@permission_verify()
def ipusage_save(request):
    temp_name = "cmdb/cmdb-header.html"
    if request.method == 'POST':
        ip_id = request.POST.get('id')
        ip_addr = request.POST.get('ip_addr')
        mac_addr = request.POST.get('mac_addr')
        status = request.POST.get('status')
        category = request.POST.get('category')
        hostname = request.POST.get('hostname')
        appname = request.POST.get('appname')
        appmodule = request.POST.get('appmodule')
        ipu_item = IPUsage.objects.get(id=ip_id)
        ipu_item.ip_addr = ip_addr
        ipu_item.mac_addr = mac_addr
        ipu_item.status = status
        ipu_item.category = category
        ipu_item.hostname = hostname
        ipu_item.appname = appname
        ipu_item.appmodule = appmodule
        ipu_item.save()
        obj = ipu_item
        status = 1
    else:
        status = 2
    return render(request, "cmdb/ipusage_edit.html", locals())