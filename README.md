# django-unslashed

[![Build Status](https://travis-ci.org/dghubble/servlib.png)](https://travis-ci.org/dghubble/django-unslashed)

Django Middleware that can automatically remove trailing URL slashes and 301 
redirect to the non-slash-terminated URL. This behavior is performed if the
initial URL ends in a slash and is invalid, removing the trailing slash
produces a valid URL, and `REMOVE_SLASH` is set to True. Otherwise there is
no effect.

For example, foo.com/bar/ will be redirected to foo.com/bar if you don't
have a valid URL pattern for foo.com/bar/ but do have a valid pattern for
foo.com/bar and `REMOVE_SLASH=True`.

This middleware provides the inverse of the Django CommonMiddleware 
`APPEND_SLASH` feature.


## Install

To install `django-unslashed`,

```
pip install django-unslashed
```

If you're using a `requirements.txt` file, add `django-unslashed>=0.2.0` to it.


## Usage

Modify your Django `settings.py` file to add `unslashed.middleware.RemoveSlashMiddleware`
to your `MIDDLEWARE_CLASSES` just before or after `django.middleware.common.CommonMiddleware`.

```python
MIDDLEWARE_CLASSES = (
    # ...
    'unslashed.middleware.RemoveSlashMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ...
)
```

Set `REMOVE_SLASH` to True and `APPEND_SLASH` to False,

```python
APPEND_SLASH = False
REMOVE_SLASH = True
```

If `REMOVE_SLASH` is False or unset, the RemoveSlashMiddleware has no effect and you are free to use the Django CommonMiddleware append slash feature with `APPEND_SLASH=True`.


## Rationale

Web applications should have a URL structure which either (1) uses trailing
slashes and redirects to append slashes if invalid non-slashed-terminated URLs are accessed.
(2) uses no trailing slash URLs and removes and redirects to unslahed URLs if
invalid slash terminated URLs are accessed. The prior is the Django default, 
while the later is possible by adding this middleware to your project.


## Notes

Based closely on Django's APPEND_SLASH CommonMiddleware [implementation](https://github.com/django/django/blob/master/django/middleware/common.py).


## Testing

```bash
$ git clone https://github.com/dghubble/django-unslashed.git
$ cd django-unslashed
$ python manage.py test unslashed
Creating test database for alias 'default'...
...
----------------------------------------------------------------------
Ran 3 tests in 0.018s

OK
Destroying test database for alias 'default'...
```


## License

[MIT License](LICENSE)
    
