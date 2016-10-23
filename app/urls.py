from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w-]+)/post/$', views.single_post, name='single_post'),
    url(r'^(?P<category>[\w-]+)/category/$', views.show_category, name='category'),
]
