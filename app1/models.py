from django.db import models
from tinymce import models as tinymce_models 
# Create your models here.

class course(models.Model):
    name = models.CharField(max_length=50,default="")
    slug = models.SlugField(help_text="link of page ex /blog/tutorial1")
    short_description = models.CharField(max_length=150,default="")
    description = models.TextField(null=True,blank=True)
    price = models.CharField(max_length=50,default="")
    thumb = models.ImageField(upload_to="courses/thumb", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return str(self.name)
    

class staf(models.Model):
    name = models.CharField(max_length=50,default="")
    role = models.CharField(max_length=50,default="")
    profile_picture = models.ImageField(upload_to="staf/profile_picture", height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return str(self.name)
    
class blogcategory(models.Model):
    name = models.CharField(max_length=50,default="")
    def __str__(self):  
        return str(self.name)

class blog(models.Model):
    
    title = models.CharField(max_length=150,default="")
    slug = models.SlugField(help_text="link of page ex /tutorial1")
    date_of_publish = models.DateField(auto_now=False, auto_now_add=False)
    thumb = models.ImageField(upload_to="blog/thumb", height_field=None, width_field=None, max_length=None,help_text="640*426")
    
    summary = models.TextField()

    body = tinymce_models.HTMLField()


    meta_description = models.TextField(default="",blank=True,null=True)
    meta_keywords = models.CharField(max_length=250,default="", blank=True,null=True)
    author = models.ForeignKey("app1.auther", on_delete=models.CASCADE, default=1)
    category = models.ManyToManyField("app1.blogcategory")

    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.title)
    

class tutorial(models.Model):

    title = models.CharField(max_length=150,default="")
    slug = models.SlugField(help_text="link of page ex /tutorial1")
    date_of_publish = models.DateField(auto_now=False, auto_now_add=False)
    
    body = tinymce_models.HTMLField()

    meta_description = models.TextField(default="",blank=True,null=True)
    meta_keywords = models.CharField(max_length=250,default="", blank=True,null=True)

    author = models.ForeignKey("app1.auther",  on_delete=models.CASCADE)

    course =  models.ForeignKey('app1.course', on_delete=models.CASCADE)
    # QNA =
    # Downloads 

    def __str__(self):
        return str(self.title)

class auther(models.Model):
    name = models.CharField(max_length=100,default="")
    role = models.CharField(max_length=100,default="")
 
    def __str__(self):
        return str(self.name)
    
class download_file(models.Model):
    name = models.CharField(max_length=100,default="")
    file = models.FileField(upload_to="tutorials/download-dat")
    tutorial = models.ForeignKey("app1.tutorial", on_delete=models.CASCADE)
 
    def __str__(self):
        return str(self.name)


    name = models.CharField(max_length=50,default="")
    short_description = models.CharField(max_length=150,default="")
    profile_pic = models.ImageField(upload_to="Tutor/profile_pic", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return str(self.name)
    