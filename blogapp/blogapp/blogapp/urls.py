from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

urlpatterns = [
    path('admin/', admin.site.urls),
]

sitemaps = {
'posts': PostSitemap,
}

urlpatterns  += [
    url(r'^blog/', include('blog.urls',namespace='blog')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
]




