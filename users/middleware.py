import logging
from django.utils.timezone import now
from django.http import HttpResponseNotFound, HttpResponseServerError

logger = logging.getLogger(__name__)

class AccessLoggerMiddleware:
    """
    Логування доступу до захищених сторінок
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            logger.info(f"User {request.user.username} accessed {request.path} at {now()}")
            response = self.get_response(request)
        return response


class ErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            return HttpResponseNotFound("Сторінку не знайдено.")
        elif response.status_code == 500:
            return HttpResponseServerError("Сталася помилка на сервері.")
        return response