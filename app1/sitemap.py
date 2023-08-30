from django.contrib.sitemaps import Sitemap
from app1.models import course,blog,tutorial,course
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

        return ['app1:courses','app1:about',]

        # return ['main:about', 'main:contact']

    def location(self, item):
        return reverse(item)

#dyanamic


class CourseIndexSiteMap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8
    protocol = 'http'

    def items(self):
        return course.objects.all()
    
    def location(self, obj):
        return '/course/%s/index' % (obj.slug)
    
# do it for all course
class pyTutSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.8
    protocol = 'http'

    def items(self):
        return tutorial.objects.filter(course__slug="python")
    
    def lastmod(self, obj):
        return obj.date_of_publish
    
    def location(self, obj):
        return '/tutorial/python/%s' % (obj.slug)

class cTutSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.8
    protocol = 'http'

    def items(self):
        return tutorial.objects.filter(course__slug="c_programming")
    
    def lastmod(self, obj):
        return obj.date_of_publish
    
    def location(self, obj):
        return '/tutorial/c_programming/%s' % (obj.slug)
    
class BlogSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.8
    protocol = 'http'

    def items(self):
        return blog.objects.all()
    
    def lastmod(self, obj):
        return obj.date_of_publish
    
    def location(self, obj):
        return '/blog/%s' % (obj.slug)

