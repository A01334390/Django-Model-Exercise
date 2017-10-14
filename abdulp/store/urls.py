from django.conf.urls import url

from .views import (
    NotebookCreation,
    NotebookDelete,
    NotebookList,
    NotebookUpdate,
    NotebookDetail,
    ClientCreation,
    ClientDelete,
    ClientList,
    ClientUpdate,
    ClientDetail,
    PageCreation,
    PageDelete,
    PageList,
    PageUpdate,
    PageDetail
)

urlpatterns = [
    url(r'^client/list/$', ClientList.as_view(), name='client_list'),
    url(r'^client/detail/(?P<pk>\d+)$', ClientDetail.as_view(), name='client_detail'),
    url(r'^client/new/$', ClientCreation.as_view(), name='client_new'),
    url(r'^client/edit/(?P<pk>\d+)$', ClientUpdate.as_view(), name='client_edit'),
    url(r'^client/delete/(?P<pk>\d+)$', ClientDelete.as_view(), name='client_delete'),
]
