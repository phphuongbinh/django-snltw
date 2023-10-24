
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import json


def login(request):
  data =  json.load(open("members/data/hocSinh.json","r"))
  
  data = {
    'dataHS':data
  }
  template = loader.get_template('members/template/index.html')
  return HttpResponse(template.render(data , request))

def register(request):
  template = loader.get_template('members/template/template.html')
  giaovien = json.load(open("members/data/giaoVien.json","r"))

  giaovien = {
    "dataGV":giaovien
  }

  return HttpResponse(template.render(giaovien, request))


def home(request):
  return render(request, 'home.html')