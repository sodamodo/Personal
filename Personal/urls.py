from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'Personal.views.home', name='home'),
    url(r'^$', include('life.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
