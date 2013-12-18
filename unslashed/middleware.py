from django import http
from django.conf import settings
from django.core import urlresolvers
from django.core.exceptions import ImproperlyConfigured
from django.utils.http import urlquote
from django.utils import six


class RemoveSlashMiddleware(object):
    """
    This middleware provides the inverse of the APPEND_SLASH option built into
    django.middleware.common.CommonMiddleware. It should be placed just before
    or just after CommonMiddleware.

    If REMOVE_SLASH is True, the initial URL ends with a slash, and it is not 
    found in the URLconf, then a new URL is formed by removing the slash a the
    end. If this new URL is found in the URLconf, then Django redirects the 
    request to this new URL. Otherwise, the initial URL is processed as usual.

    For example, foo.com/bar/ will be redirected to foo.com/bar if you don't
    have a valid URL pattern for foo.com/bar/ but do have a valid pattern for
    foo.com/bar.

    Using this middlware with REMOVE_SLASH set to False or without REMOVE_SLASH 
    set means it will do nothing.

    Based closely on Django's APPEND_SLASH CommonMiddleware implementation at
    https://github.com/django/django/blob/master/django/middleware/common.py
    """

    def process_request(self, request):

        # Check for a redirect based on settings.APPEND_SLASH
        # and settings.PREPEND_WWW
        host = request.get_host()
        old_url = [host, request.path]
        new_url = old_url[:]

        if getattr(settings, 'APPEND_SLASH') and getattr(settings, 'REMOVE_SLASH'):
            raise ImproperlyConfigured("APPEND_SLASH and REMOVE_SLASH may not both be True.")

        # Remove slash if REMOVE_SLASH is set and the URL has a trailing slash
        # and there is no pattern for the current path
        if getattr(settings, 'REMOVE_SLASH', False) and old_url[1].endswith('/'):
            urlconf = getattr(request, 'urlconf', None)
            if (not urlresolvers.is_valid_path(request.path_info, urlconf)) and urlresolvers.is_valid_path(request.path_info[:-1], urlconf):
                new_url[1] = new_url[1][:-1]
                if settings.DEBUG and request.method == 'POST':
                    raise RuntimeError((""
                    "You called this URL via POST, but the URL ends in a "
                    "slash and you have REMOVE_SLASH set. Django can't "
                    "redirect to the non-slash URL while maintaining POST "
                    "data. Change your form to point to %s%s (without a "
                    "trailing slash), or set REMOVE_SLASH=False in your "
                    "Django settings.") % (new_url[0], new_url[1]))

        if new_url == old_url:
            # No redirects required.
            return
        if new_url[0]:
            newurl = "%s://%s%s" % (
                'https' if request.is_secure() else 'http', 
                new_url[0], urlquote(new_url[1]))
        else:
            newurl = urlquote(new_url[1])
        if request.META.get('QUERY_STRING', ''):
            if six.PY3:
                newurl += '?' + request.META['QUERY_STRING']
            else:
                # `query_string` is a bytestring. Appending it to the unicode
                # string `newurl` will fail if it isn't ASCII-only. This isn't
                # allowed; only broken software generates such query strings.
                # Better drop the invalid query string than crash (#15152).
                try:
                    newurl += '?' + request.META['QUERY_STRING'].decode()
                except UnicodeDecodeError:
                    pass
        return http.HttpResponsePermanentRedirect(newurl)


