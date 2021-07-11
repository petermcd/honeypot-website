from django.shortcuts import render
from django.http import HttpResponse
from .logins import Logins
from .output import Output


def country_view(request, country: str = None):
    start = int(request.GET.get('start', 0))
    end = int(request.GET.get('end', 0))
    try:
        db = Logins(start=start, end=end)
    except ValueError as ex:
        handler = Output()
        res, content_type = handler.failure(str(ex))
        return HttpResponse(res, content_type=content_type)

    return db.by_country(country=country)
