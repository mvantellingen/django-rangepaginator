from django.template import Context, RequestContext, Template
from django.core.paginator import Paginator


def render_template(value, **context):
    template = Template(value)

    request = context.get('request')
    ctx = RequestContext(request, context) if request else Context(context)
    return template.render(ctx).strip()


def test_paginate_first():
    objects = ['foo'] * 50
    paginator = Paginator(objects, 1)
    page = paginator.page(1)

    content = render_template(
        "{% load rangepaginator %}{% paginate page %}",
        page=page)
    assert content


def test_paginate_last():
    objects = ['foo'] * 50
    paginator = Paginator(objects, 1)
    page = paginator.page(50)

    content = render_template(
        "{% load rangepaginator %}{% paginate page %}",
        page=page)
    assert content


def test_paginate_with_request_first(rf):
    request = rf.get('/', data={'foo': 'bar'})
    objects = ['foo'] * 50
    paginator = Paginator(objects, 1)
    page = paginator.page(1)

    content = render_template(
        "{% load rangepaginator %}{% paginate page request=request %}",
        page=page, request=request)
    assert content
    assert 'foo=bar' in content


def test_paginate_with_request_last(rf):
    request = rf.get('/', data={'foo': 'bar'})
    objects = ['foo'] * 50
    paginator = Paginator(objects, 1)
    page = paginator.page(50)

    content = render_template(
        "{% load rangepaginator %}{% paginate page request=request %}",
        page=page, request=request)
    assert content
    assert 'foo=bar' in content
