django-unslashed
================

.. image:: https://pypip.in/version/django-unslashed/badge.png
    :target: https://pypi.python.org/pypi/django-unslashed/
    :alt: Latest Version

.. image:: https://travis-ci.org/dghubble/django-unslashed.png
    :target: https://travis-ci.org/dghubble/django-unslashed
    :alt: Build Status

.. image:: https://pypip.in/download/django-unslashed/badge.png
    :target: https://pypi.python.org/pypi/django-unslashed/
    :alt: Downloads

.. image:: https://pypip.in/license/django-unslashed/badge.png
    :target: https://pypi.python.org/pypi/django-unslashed/
    :alt: License

This middleware provides the inverse of the Django CommonMiddleware :code:`APPEND_SLASH` feature. It can automatically remove trailing URL slashes and 301 redirect to the non-slash-terminated URL. This behavior is performed if the initial URL ends in a slash and is invalid, removing the trailing slash produces a valid URL, and :code:`REMOVE_SLASH` is set to True. Otherwise there is no effect.

For example, :code:`foo.com/bar/` will be redirected to :code:`foo.com/bar` if you don't have a valid URL pattern for :code:`foo.com/bar/` but do have a valid pattern for foo.com/bar and :code:`REMOVE_SLASH=True`.