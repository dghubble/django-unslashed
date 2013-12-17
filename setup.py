from distutils.core import setup 

setup(
    # Required information
    name = 'django-unslash',
    version = '0.0.1',
    author = 'Dalton Hubble',
    author_email = 'dghubble@gmail.com',
    url = 'https://github.com/dghubble/django-unslash',

    packages = ['unslash'],

    # Package dependencies
    install_requires = ['Django>=1.0'],

    # Metadata
    keywords = 'django slash remove trailing unslash remove_slash path',
    description = 'Django Middleware that can automatically remove trailing \
    URL slashes and 301 redirect to the non-slash-terminated URL.',
    long_description = 'long description',
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