from django.conf.urls import patterns, include, url
from life import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Personal import settings
from django.conf.urls.static import static
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'life.views.hello', name='hello'),


) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

