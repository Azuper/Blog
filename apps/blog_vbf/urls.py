from django.conf.urls import url

from apps.blog_vbf import views

urlpatterns = [
    url(r'^$', views.postt_list, name='postt_list'),
    url(r'^new$', views.postt_create, name='postt_new'),
    url(r'^edit/(?P<pk>\d+)$', views.postt_update, name='postt_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.postt_delete, name='postt_delete'),
]
