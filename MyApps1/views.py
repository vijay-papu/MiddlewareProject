from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def welcome_view(request):
    print('This line added by view function(A-P-Resp) welcome_view..!!!')
    return HttpResponse('<h1>Custom ExecutionFlowMiddleware Demo</h1><hr/>')

from django.http import HttpResponse
def home_Page_view(request):
    return HttpResponse('<h1>Hello this is from home page view</h1>')

from django.http import HttpResponse
def home_Page_view2(request):
    return HttpResponse('<h1>Hello this is from home page view2</h1>')

from django.http import HttpResponse
def home_Page_view3(request):
    return HttpResponse('<h1>Hello this is from home page view3</h1>')
