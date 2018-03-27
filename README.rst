=====================
django-rangepaginator
=====================

This Django app provides a templatetag to render pagination widgets which include a range of pages around the current active one.

.. image:: docs/_static/example.png?stop-caching-me

Status
======
.. image:: https://travis-ci.org/mvantellingen/django-rangepaginator.svg?branch=master
    :target: https://travis-ci.org/mvantellingen/django-rangepaginator

.. image:: http://codecov.io/github/mvantellingen/django-rangepaginator/coverage.svg?branch=master
    :target: http://codecov.io/github/mvantellingen/django-rangepaginator?branch=master

.. image:: https://img.shields.io/pypi/v/django-rangepaginator.svg
    :target: https://pypi.python.org/pypi/django-rangepaginator/


Installation
============

.. code-block:: shell

   pip install django_rangepaginator

Update your Django settings:

.. code-block:: python


    INSTALLED_APPS += [
        'django_rangepaginator'
    ]

    # Use bootstrap4 template
    RANGE_PAGINATOR_TEMPLATE = 'django_rangepaginator/bootstrap3.html'

    # Use bootstrap3 template (default)
    RANGE_PAGINATOR_TEMPLATE = 'django_rangepaginator/bootstrap4.html'


Usage
=====
.. code-block:: django

    {% load rangepaginator %}
    {% paginate page request=request %}

The following options are available:

- distance: number of pages around current active one (default = 2)
- edge: number of pages at the start and end (default = 1)
- extra_class: add extra css classes to the pagination div (default = '')
- text_labels: use strings for previous/next instead of symbols (default = True)

Demo
====
A sandbox environment is available in the repository, run the following:

.. code-block:: shell

   ./sandbox/manage.py migrate
   ./sandbox/manage.py runserver

Bugs/features
=============

Let me know! :-)


