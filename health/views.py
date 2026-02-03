from django.http import HttpRequest
from django.http import JsonResponse


def health_endpoint(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"health": "ok"})
