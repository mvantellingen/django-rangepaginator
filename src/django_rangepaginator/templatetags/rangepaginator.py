from django import template

from django_rangepaginator.layout import calculate_pages
from six.moves.urllib.parse import parse_qs, urlencode, urlparse, urlunparse

register = template.Library()


@register.inclusion_tag('django_rangepaginator/bootstrap3.html')
def paginate(page=None, distance=2, request=None):
    paginator = page.paginator
    pages = calculate_pages(
        page.number, paginator.num_pages, distance=distance)

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
    else:
        for page_num in pages:
            url = '?%s' % urlencode({'page': str(page_num)})
            result.append((page_num, url))
    pages = result

    return {
        'current': page.number,
        'pages': pages,
        'paginator': paginator,
    }
