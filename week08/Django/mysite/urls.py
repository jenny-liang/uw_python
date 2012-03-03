# This also imports the include function
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),
    url(r'^books/', include('books.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


