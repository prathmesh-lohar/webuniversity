from django.contrib.sitemaps import Sitemap
from app1.models import course,blog
from django.urls import reverse

#static 

class HightPrioritySitemap(Sitemap):
    changefreq = "monthly"
    priority = 1.0
    protocol = 'http'

    def items(self):

        return ['app1:home']

        # return ['main:about', 'main:contact']

    def location(self, item):
        return reverse(item)

class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'

    def items(self):

        return ['app1:about','app1:courses']

        # return ['main:about', 'main:contact']

    def location(self, item):
        return reverse(item)

#dyanamic

# class CourseSiteMap(Sitemap):
#     changefreq = 'weekly'
#     priority = 0.8
#     protocol = 'http'


class BlogSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.8
    protocol = 'http'

    def items(selft):
        return blog.objects.all()
    
    def lastmod(self, obj):
        return obj.date_of_publish
    
    def location(selft, obj):
        return '/blog/%s' % (obj.slug)

