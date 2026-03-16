from datetime import time, datetime

from django.http import HttpResponseForbidden
from django.utils.timezone import localtime


class ReadOnlyMixin:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True

class TimeRestrictedMixin:
    ...
    # start_time = None
    # end_time = None
    # error_message = "Access restricted during those hours."
    #
    # def dispatch(self, request, *args, **kwargs):
    #     # current_time = datetime.now().time()
    #     current_time = localtime().time()
    #
    #     if not (self.start_time <= current_time <= self.end_time):
    #         return HttpResponseForbidden(self.error_message)
    #     return super().dispatch(request, *args, **kwargs)