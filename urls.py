from django.conf.urls.defaults import *
from AARRV.views import home

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    ('^home/$', home),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
