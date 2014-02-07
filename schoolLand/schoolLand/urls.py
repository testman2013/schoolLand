from django.conf.urls import patterns, include, url

from django.contrib import admin
from schoolLand import views
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name="index"),
    url(r'^signUp/$', views.signUp, name="signUp"),
    url(r'^signIn/$', views.signIn, name="signIn"),
    url(r'^signOut/$', views.signOut, name="signOut"),
    url(r'^message/$', views.message, name="message"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
