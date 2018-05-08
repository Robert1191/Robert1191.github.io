# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())