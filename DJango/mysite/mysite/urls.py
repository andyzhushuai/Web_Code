from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.http import HttpResponse
def hello(request):
	return HttpResponse('hello, world!')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
		url(r'^$', hello),
)
