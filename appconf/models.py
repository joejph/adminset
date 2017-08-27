#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from cmdb.models import Host


class AppOwner(models.Model):
    name = models.CharField(u"负责人姓名", max_length=50, unique=True, null=False, blank=False)
    phone = models.CharField(u"负责人手机", max_length=50, null=False, blank=False)
    qq = models.CharField(u"负责人QQ", max_length=100, null=True, blank=True)
    weChat = models.CharField(u"负责人微信", max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(u"产品线名称", max_length=50, unique=True, null=False, blank=False)
    description = models.CharField(u"产品线描述", max_length=255, null=True, blank=True)
    owner = models.ForeignKey(
        AppOwner, verbose_name=u"产品线负责人"
    )

    def __unicode__(self):
        return self.name


class Project(models.Model):
    LANGUAGE_TYPES = (
        ("Java", "Java"),
        ("PHP", "PHP"),
        ("Python", "Python"),
        ("C#", "C#"),
        ("Html", "Html"),
        ("Javascript", "Javascript"),
        ("C/C++", "C/C++"),
        ("Ruby", "Ruby"),
        ("Other", "Other"),
    )

    APP_TYPE = (
        ("Frontend", "Frontend"),
        ("Middleware", "Middleware"),
        ("Backend", "Backend"),
    )

    SERVER_TYPE = (
        ("Tomcat", "Tomcat"),
        ("Weblogic", "Weblogic"),
        ("JETTY", "JETTY"),
        ("Nginx", "Nginx"),
        ("Gunicorn", "Gunicorn"),
        ("Uwsgi", "Uwsgi"),
        ("Apache", "Apache"),
        ("IIS", "IIS"),
    )

    APP_ARCH = (
        ("Django", "Django"),
        ("Flask", "Flask"),
        ("Tornado", "Tornado"),
        ("Dubbo", "Dubbo"),
        ("SSH", "SSH"),
        ("Spring boot", "Spring boot"),
        ("Spring cloud", "Spring cloud"),
        ("Laravel", "Laravel"),
        ("ThinkPHP", "ThinkPHP"),
        ("Phalcon", "Phalcon"),
        ("other", "other"),
    )

    name = models.CharField(u"项目名称", max_length=50, unique=True, null=False, blank=False)
    description = models.CharField(u"项目描述", max_length=255, null=True, blank=True)
    language_type = models.CharField(u"语言类型", choices=LANGUAGE_TYPES, max_length=30, null=True, blank=True)
    app_type = models.CharField(u"程序类型", choices=APP_TYPE, max_length=30, null=True, blank=True)
    server_type = models.CharField(u"服务器类型", choices=SERVER_TYPE, max_length=30, null=True, blank=True)
    app_arch = models.CharField(u"程序框架", choices=APP_ARCH, max_length=30, null=True, blank=True)
    appPath = models.CharField(u"程序路径", max_length=255, null=False, blank=False)
    configPath = models.CharField(u"配置文件路径", max_length=255, null=True, blank=True)
    product = models.ForeignKey(
            Product,
            null=False,
            verbose_name=u"所属产品线"
    )
    owner = models.ForeignKey(
            AppOwner,
            null=False,
            verbose_name=u"项目负责人"
    )
    serverList = models.ManyToManyField(
            Host,
            blank=True,
            verbose_name=u"服务器"
    )





