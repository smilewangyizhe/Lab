from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

#from django.conf.urls import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_PATH}),
    url(r'^welcome/','library_online.views.welcome'),
    url(r'^search/','library_online.views.search'), 
    url(r'^add_author/','library_online.views.add_author'),
    url(r'^add_book/','library_online.views.add_book'),
    url(r'^detail/','library_online.views.detail'),
    url(r'^update/','library_online.views.update'),
    url(r'^delete_author/','library_online.views.delete_author'),
    url(r'^delete_book/','library_online.views.delete_book'),
    )
