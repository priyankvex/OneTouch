from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import onetouch.views
from onetouch.views import appRequest

#from onetouch.views import appRequest

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^request/', 'onetouch.views.appRequest'),
)
