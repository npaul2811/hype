from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name='blog_index',),
    url(r'^(?P<slug>[a-zA-Z0-9\-]+)/$', views.BlogSingle.as_view(), name='blog_single',),
]
