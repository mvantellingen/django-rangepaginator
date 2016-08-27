from django.conf.urls import url

from sandbox import views

urlpatterns = [
    url(r'^$', views.index_view),
]
