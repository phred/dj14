from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dj14.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', 'stickies.views.index')
)

