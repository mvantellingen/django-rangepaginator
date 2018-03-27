from django.conf.urls import url

from django.views.generic import TemplateView


from sandbox import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^bootstrap3$', views.example_view, kwargs={
        'template_name': 'bootstrap3'
    }, name='bootstrap3'),
    url(r'^bootstrap4$', views.example_view, kwargs={
        'template_name': 'bootstrap4'
    }, name='bootstrap4'),
]
