from django.conf.urls import url

from .views import (
    PluralList,
    PluralDetail,
    PluralCreation,
    PluralUpdate,
    PluralDelete
)

urlpatterns = [

    url(r'^$', PluralList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', PluralDetail.as_view(), name='detail'),
    url(r'^nuevo$', PluralCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', PluralUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', PluralDelete.as_view(), name='delete'),

]