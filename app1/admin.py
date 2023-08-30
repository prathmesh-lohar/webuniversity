from django.contrib import admin
from app1.models import course,staf,blog,auther,tutorial,download_file,blogcategory

admin.site.site_header = "Web University Admin Panel"
admin.site.site_title = "Web University Admin Panel Portal"
admin.site.index_title = "Welcome to Web University Admin Panel Portal"

admin.site.register(course)
admin.site.register(staf)
admin.site.register(blog)
admin.site.register(auther)
admin.site.register(tutorial)
admin.site.register(download_file)
admin.site.register(blogcategory)





# Register your models here.
