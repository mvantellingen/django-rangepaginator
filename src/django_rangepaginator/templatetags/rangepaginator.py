from django import template

from django_rangepaginator.layout import calculate_pages
from six.moves.urllib.parse import parse_qs, urlencode, urlparse, urlunparse

register = template.Library()


@register.inclusion_tag('django_rangepaginator/bootstrap3.html')
def paginate(page=None, distance=2, request=None):
    paginator = page.paginator
    pages = calculate_pages(
        page.number, paginator.num_pages, distance=distance)

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

    return {
        'current': page.number,
        'page': page,
        'pages': pages,
        'paginator': paginator,
        'next_page_url': next_page_url,
        'prev_page_url': prev_page_url,
    }
