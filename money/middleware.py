# from django.http import HttpResponseForbidden, HttpResponse
# from django.utils import timezone
#
#
# class LoggIPWriterMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request, *args, **kwargs):
#         now = timezone.now()
#
#         if now.hour < 8 or now.hour > 18:
#             return HttpResponse('Saytimiz 8:00 dan 18:00 gacha ishlatyd')
#         return self.get_response(request, *args, **kwargs)
#
#
# class BlockIpMiddleware:
#     requests = {}
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         ip = request.META.get('REMOTE_ADDR', 'NOMALUM IP')
#         now = timezone.now()
#
#         if ip not in self.requests:
#             self.requests[ip] = []
#
#         for i in self.requests[ip]:
#             pass
#     #
#     # if not request.headers.get([ip]):
#     #
#     #
#     # for i in request[ip]:
#     #     if now - i > 10:
#     #         request[ip].remove(i)
#     # if len(request[ip]) > 5:
#     #     return HttpResponse('Siz uchhun sayt blocklangan ')
