from django.conf.urls import url

from . import views

app_name = 'download'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^info$', views.info, name='info'),
    url(r'^download$', views.download, name='download'),
]