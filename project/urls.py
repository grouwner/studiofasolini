from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^project/(?P<slug>[\w-]+)-(?P<id>[\w-]+)/$', views.intervento_detail, name='intervento_detail'),
    url(r'^search/$', views.search),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)