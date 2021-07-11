from django.http import HttpResponse
from .output import Output


class Logins:
    __slots__ = ['_start', '_end']

    def __init__(
            self,
            start: int = 0,
            end: int = 0,
    ):
        if start > 0 and not self._validate_epoch(start):
            raise ValueError('Start value is invalid')
        if end > 0 and not self._validate_epoch(end):
            raise ValueError('End value is invalid')
        self._start = start
        self._end = end

    def by_country(self, country: str):
        params = {
            'start': self._start,
            'end': self._end,
            'country': country,
        }
        handler = Output()
        res, content_type = handler.success(list(), params)
        return HttpResponse(res, content_type=content_type)

    @staticmethod
    def _validate_epoch(epoch: int) -> bool:
        return 1575072000 <= epoch <= time.time()
