from django.contrib import admin
from django.urls import path,include
from app1 import views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from app1.sitemap import BlogSiteMap,StaticSitemap,HightPrioritySitemap

from django.views.generic.base import TemplateView

app_name = "app1"

sitemaps = {
    'HightPrioritySitemap': HightPrioritySitemap,
    'static': StaticSitemap,
    'blog':BlogSiteMap,
    
}

urlpatterns = [
    
    path("", views.home , name="home"),
    path("about", views.about , name="about"),
    path("courses", views.courses , name="courses"),

    path("tutorial/<str:course>/<str:slug>/<int:cid>", views.tutorial, name="tutorial"),
    
    path("course/<str:slug>/index/<int:id>", views.index , name="index"),




    path("sitemap.xml", sitemap, {"sitemaps":sitemaps}, name="django.contrib.sitemaps.view.sitemap"),
    path("robots.txt", TemplateView.as_view(template_name="app1/robots.txt",content_type="text/plain")),


    
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 