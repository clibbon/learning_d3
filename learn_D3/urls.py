from django.conf.urls import patterns, include, url
from django.contrib import admin
import example.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learn_D3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', example.views.testPage.as_view(),name='test-page'),
)
