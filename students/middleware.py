import time

from .views import create_student, edit_student


# https://webdevblog.ru/nachalo-raboty-s-middleware-v-django/
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print('This is happening before view')
        response = get_response(request)
        print('This is happening after view')

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware


class TimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        t1 = time.time()
        response = self.get_response(request)
        t2 = time.time()
        print("TOTAL TIME:", (t2 - t1), 'seconds')

        # Code to be executed for each request/response after
        # the view is called.

        return response


class PhoneFormatterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if (view_func == create_student or view_func == edit_student) and \
            request.method == 'POST' and (phone := request.POST.get('phone')):
            post = request.POST.copy()
            post['phone'] = int(phone.strip('').replace('+', '').replace('(', '').replace(')', ''))
            request.POST = post
