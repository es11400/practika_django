from django.conf import settings

from django.utils.cache import patch_vary_headers
from django.utils import translation


class LanguageMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        forced_language = request.GET.get('lang')
        if forced_language:
            request.session['lang'] = forced_language

        session_language = request.session.get('lang')
        if session_language:
            translation.activate(session_language)

        response = self.get_response(request)



        # Code to be executed for each request/response after
        # the view is called.

        return response