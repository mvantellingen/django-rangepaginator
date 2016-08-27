from django.shortcuts import render_to_response
from django.core.paginator import Paginator


def index_view(request):
    objects = ['foo'] * 100
    paginator = Paginator(objects, 2)

    page = paginator.page(request.GET.get('page', 1))
    return render_to_response('index.html', {'page': page, 'request': request})
