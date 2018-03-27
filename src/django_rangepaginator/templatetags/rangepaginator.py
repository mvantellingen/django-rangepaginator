from django import template

from django.conf import settings
from django.template import loader
from six.moves.urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from django_rangepaginator.layout import calculate_pages

register = template.Library()



@register.simple_tag
def paginate(page=None, request=None, distance=2, edge=1, extra_class='',
             text_labels=True):
    paginator = page.paginator
    pages = calculate_pages(
        page.number, paginator.num_pages, distance=distance, edge=edge)

    prev_page_url = next_page_url = None
    result = []
    if request:
        parts = urlparse(request.get_full_path())
        params = parse_qs(parts.query)
        for page_num in pages:
            if not page_num:
                result.append((page_num, None))
            else:
                params['page'] = [str(page_num)]
                query = urlencode(params, doseq=True)
                url = urlunparse(parts[:4] + (query,) + parts[5:])
                result.append((page_num, url))

        if page.has_previous():
            params['page'] = page.previous_page_number()
            query = urlencode(params, doseq=True)
            prev_page_url = urlunparse(parts[:4] + (query,) + parts[5:])

        if page.has_next():
            params['page'] = page.next_page_number()
            query = urlencode(params, doseq=True)
            next_page_url = urlunparse(parts[:4] + (query,) + parts[5:])

    else:
        for page_num in pages:
            url = '?%s' % urlencode({'page': str(page_num)})
            result.append((page_num, url))

        if page.has_previous():
            prev_page_url = '?%s' % urlencode({
                'page': str(page.previous_page_number())
            })

        if page.has_next():
            next_page_url = '?%s' % urlencode({
                'page': str(page.next_page_number())
            })

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
