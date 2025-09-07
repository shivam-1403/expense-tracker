from tracker.models import RequestLogs

class RequestLogin:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        request_info = request
        # print(request_info)
        # print(request_info.path, request_info.method)
        RequestLogs.objects.create(
            request_info = vars(request_info),
            request_type = request_info.method,
            request_method = request_info.path,
        )
        return self.get_response(request)