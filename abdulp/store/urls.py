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
    #Views for clients
    url(r'^client/list/$', ClientList.as_view(), name='client_list'),
    url(r'^client/detail/(?P<pk>\d+)$', ClientDetail.as_view(), name='client_detail'),
    url(r'^client/new/$', ClientCreation.as_view(), name='client_new'),
    url(r'^client/edit/(?P<pk>\d+)$', ClientUpdate.as_view(), name='client_edit'),
    url(r'^client/delete/(?P<pk>\d+)$', ClientDelete.as_view(), name='client_delete'),

    #Views for Notebooks
    url(r'^notebook/list/$', NotebookList.as_view(), name='notebook_list'),
    url(r'^notebook/detail/(?P<pk>\d+)$', NotebookDetail.as_view(), name='notebook_detail'),
    url(r'^notebook/new/$', NotebookCreation.as_view(), name='notebook_new'),
    url(r'^notebook/edit/(?P<pk>\d+)$', NotebookUpdate.as_view(), name='notebook_edit'),
    url(r'^notebook/delete/(?P<pk>\d+)$', NotebookDelete.as_view(), name='notebook_delete'),

    #Views for Pages
    url(r'^page/list/$', PageList.as_view(), name='page_list'),
    url(r'^page/detail/(?P<pk>\d+)$', PageDetail.as_view(), name='page_detail'),
    url(r'^page/new/$', PageCreation.as_view(), name='page_new'),
    url(r'^page/edit/(?P<pk>\d+)$', PageUpdate.as_view(), name='page_edit'),
    url(r'^page/delete/(?P<pk>\d+)$', PageDelete.as_view(), name='page_delete'),
]
