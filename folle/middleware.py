from django.conf import settings
from django.middleware.locale import LocaleMiddleware


class GermanDefaultLocaleMiddleware(LocaleMiddleware):
    """Like LocaleMiddleware, but ignores the browser's Accept-Language
    header for unprefixed URLs so the site defaults to German instead of
    auto-switching to whatever language the visitor's browser prefers.
    Explicit /en/ URLs and a manually chosen language cookie still work.
    """

    def process_request(self, request):
        if settings.LANGUAGE_COOKIE_NAME not in request.COOKIES:
            request.META.pop('HTTP_ACCEPT_LANGUAGE', None)
        super().process_request(request)
