from django import template

from django.conf import settings
from django.template import loader
from furl import furl

from django_rangepaginator.layout import calculate_pages

register = template.Library()


@register.simple_tag
def paginate_links(page, request, with_canonical=False):
    canonical = prev_page_url = next_page_url = None
    current_url = furl(request.get_full_path() if request else '')

    if with_canonical:
        if current_url.args.get('page') == '1':
            del current_url.args['page']
        canonical = current_url.url

    if page.has_previous():
        prev_page_url = _get_url_with_page_num(
            current_url, page.previous_page_number())
        if request:
            prev_page_url = request.build_absolute_uri(prev_page_url)

    if page.has_next():
        next_page_url = _get_url_with_page_num(
            current_url, page.next_page_number())
        if request:
            next_page_url = request.build_absolute_uri(next_page_url)

    context = {
        'page': page,
        'canonical': canonical,
        'base_url': request.build_absolute_uri(request.path),
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    }
    template = loader.get_template('django_rangepaginator/link_tags.html')
    return template.render(context)


@register.simple_tag
def paginate(page=None, request=None, distance=2, edge=1, extra_class='',
             text_labels=True):
    paginator = page.paginator
    pages = calculate_pages(
        page.number, paginator.num_pages, distance=distance, edge=edge)

    prev_page_url = next_page_url = None
    result = []

    current_url = furl(request.get_full_path() if request else '')
    for page_num in pages:
        if not page_num:
            result.append((page_num, None))
        else:
            page_url = _get_url_with_page_num(current_url, page_num)
            result.append((page_num, page_url))

    if page.has_previous():
        prev_page_url = _get_url_with_page_num(
            current_url, page.previous_page_number())

    if page.has_next():
        next_page_url = _get_url_with_page_num(
            current_url, page.next_page_number())

    pages = result

    context = {
        'current': page.number,
        'page': page,
        'pages': pages,
        'paginator': paginator,
        'next_page_url': next_page_url,
        'prev_page_url': prev_page_url,
        'extra_class': extra_class,
        'text_labels': text_labels,
    }

    template_name = getattr(
        settings, 'RANGE_PAGINATOR_TEMPLATE',
        'django_rangepaginator/bootstrap3.html')
    template = loader.get_template(template_name)
    return template.render(context)


def _get_url_with_page_num(current_url, page_num):
    if page_num != 1:
        current_url.args['page'] = page_num
    elif 'page' in current_url.args:
        del current_url.args['page']
    return current_url.url
