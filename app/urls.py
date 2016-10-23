from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.single_post, name='single_post'),
    url(r'^(?P<category>[\w-]+)$', views.show_category, name='category'),
]
