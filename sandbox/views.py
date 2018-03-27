from django.test import override_settings
from django.shortcuts import render_to_response
from django.core.paginator import Paginator


def example_view(request, template_name):
    objects = ['foo'] * 100
    paginator = Paginator(objects, 2)

    page = paginator.page(request.GET.get('page', 1))

    use_template = 'django_rangepaginator/%s.html' % template_name
    with override_settings(RANGE_PAGINATOR_TEMPLATE=use_template):
        return render_to_response(
            '%s.html' % template_name, {'page': page, 'request': request})
