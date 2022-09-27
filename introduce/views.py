from os import access
from django.shortcuts import render
from introduce.models import AccessLog

# Create your views here.
def introduce(request):
    access_log = AccessLog()
    access_log.location = "introduce" #접속페이지이름
    access_log.save() #이게 있어야 저장이 됨
    
    return render(request, 'introduce.html')