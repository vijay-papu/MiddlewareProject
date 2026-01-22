class ExecutionFlowMiddleware(object):
    def __init__(self, get_response):
        print("init() is executed only once..!! for ExecutionFlowMiddleware")
        self.get_response = get_response
    def __call__(self, request):
        print('This line added at pre-processing of before-view-request')
        response = self.get_response(request)
        print('This line added at post-processing of after-view-response')
        return response

from django.http import HttpResponse
class AppMaintainanceMiddleware(object):
    def __init__(self, get_response):
        print("init() method is called... forAppMaintainanceMiddleware ")
        self.get_response = get_response
    def __call__(self, request):
        return HttpResponse('<h1>Currently Application under Maintainance...<br/><br/>Plz try after 6am...!!<h1><hr/>')

from django.http import HttpResponse
class ErrorMessageMiddleware(object):
    def __init__(self, get_response):
        print("init() method is called... for error-app ErrorMessageMiddleware")
        self.get_response = get_response
    def __call__(self, request):
        return self.get_response(request)
    def process_execution(self, request, execption):
        return HttpResponse('<h1>Currently Currently we are facing technical problems...(Exception)<br/><br/>Please try after some time..!!<h1><hr/>')

class FirstMiddleware(object):
    def __init__(self, get_response):
         print("init() Executed for firstMiddleware")
         self.get_response = get_response

    def __call__(self, request):
        print('This line printed by FirstMiddleware at pre-processing of request')
        response = self.get_response(request)
        print('This line printed by FirstMiddleware at post-processing of request')
        return response

class SecondMiddleware(object):
    def __init__(self, get_response):
         print("init() Executed for SecondMiddleware")
         self.get_response = get_response

    def __call__(self, request):
        print('This line printed by SecondMiddleware at pre-processing of request')
        response = self.get_response(request)
        print('This line printed by SecondMiddleware at post-processing of request')
        return response
