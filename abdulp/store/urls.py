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
    url(r'^$', ClientList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', ClientDetail.as_view(), name='detail'),
    url(r'^nuevo$', ClientCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', ClientUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', ClientDelete.as_view(), name='delete'),
]
