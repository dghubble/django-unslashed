import os
from unslashed import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    # Required information
    name = 'django-unslashed',
    version = __version__,
    author = 'Dalton Hubble',
    author_email = 'dghubble@gmail.com',
    url = 'https://github.com/dghubble/django-unslashed',

    packages = ['unslashed'],

    # Package dependencies
    install_requires = ['Django>=1.0'],

    # Metadata
    license = 'MIT License',
    keywords = 'django slash remove trailing unslash remove_slash path',
    description = 'Django Middleware that can automatically remove trailing URL slashes and 301 redirect to the non-slash-terminated URL.',
    long_description = read('README.md'),
    classifiers = [
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        # Extras
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP'],
)