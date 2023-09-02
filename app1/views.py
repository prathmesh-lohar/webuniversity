from django.shortcuts import render,HttpResponse
from django.db.models import Q
from django.contrib import messages
# Create your views here.
from django.core.paginator import Paginator

def home(request):
    from app1.models import course,blog,staf
    courses = course.objects.all()
    featured_blogs = blog.objects.filter(is_featured=True)
    staf = staf.objects.all()
    data ={
         'courses':courses,
         'featured_blogs':featured_blogs,
         'staf':staf

      }

    return render(request, "index.html",data)

def about(request):
    from app1.models import staf
    staf = staf.objects.all()
    data = {
        'staf':staf
    }
    return render(request, "about.html",data)

def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')

        body = "Name :" + " "+ fname + " " +lname + "\n" + "Phone :" + " " +phone +"\n" +"message : " + msg

        from app1.mail import sendmail
        sendmail(body)
        messages.success(request, "Your Response Saved Successfully")
        return render(request, "contact.html")

    return render(request, "contact.html")

def courses(request):
    from app1.models import course
    courses = course.objects.all()
   
    data ={
         'courses':courses,
        
      }

    return render(request, "courses.html",data)

def course_index(request,slug):
 
    slug = slug

    from app1.models import tutorial
    tutorial = tutorial.objects.filter(course__slug=slug)
    data = {
        'slug': slug,
        'tutorial':tutorial
       
    }
    return render(request, "course-index.html",data)

def tutorial(request,course,slug):
    from app1.models import tutorial,course
    
    course=course
    
    slug=slug
 
   
    tutorials = tutorial.objects.filter(slug=slug)[0]
  
    # courseid = tutorial.course.id
  
    # tutorial_list = tutorial.objects.filter(course__id=cid)
    tutorial_list = tutorial.objects.filter(course=tutorials.course)
    
    tt = tutorial.objects.get(slug=slug)    
    next = tutorial.objects.filter(id__gt=tt.id,course=tutorials.course).order_by('id').first()
    prev = tutorial.objects.filter(id__lt=tt.id, course=tutorials.course).order_by('id').last()
   
    # next = tutorial.objects.filter(id__gt=tt.id,course__id=cid).order_by('id').first()
    # prev = tutorial.objects.filter(id__lt=tt.id, course__id=cid).order_by('id').last()
   

    data = {
        'tutorials':tutorials,
        'tutorial_list':tutorial_list,
        # 'cid':cid,
        'next':next,
        "prev":prev

    }
    return render(request, "tutorial.html",data)

def blog_filter(request,category):
    category=category
    from app1.models import blog,blogcategory
    blogs = blog.objects.filter(category__name__contains=category)
    cats = blogcategory.objects.all()
    p = Paginator(blogs,24)
    page = request.GET.get("page")
    pages = p.get_page(page)
 
    data = {
        'blogs':blogs,
        'cats':cats,
        'category':category,
        'pages':pages
    }
    return render(request, "all_blog.html",data)

def all_blog(request):
    from app1.models import blog,blogcategory

    blogs = blog.objects.all()
    cats = blogcategory.objects.all()
    p = Paginator(blogs,24)
    page = request.GET.get("page")
    pages = p.get_page(page)
    data = {
        'blogs':blogs,
        'cats':cats,
        'pages':pages
    }
    return render(request, "all_blog.html",data)

def blog(request,slug):
    slug=slug

    from app1.models import blog

    blogobj = blog.objects.filter(slug=slug)[0]

    next = blog.objects.filter(id__gt=blogobj.id).order_by('id').first()
    prev = blog.objects.filter(id__lt=blogobj.id).order_by('id').last()
   
   
    data ={
        'blogobj':blogobj,
        'next':next,
        'prev':prev
        
    }

    return render(request,"single-blog.html",data)

def search(request):
 
    from app1.models import blog,tutorial,course
    if request.method == 'POST':
        search = request.POST.get('search')
        course = course.objects.filter(Q(name__icontains=search) | Q(short_description__icontains=search) | Q(description__icontains=search))
        tutorial = tutorial.objects.filter(Q(title__icontains=search) | Q(body__icontains=search) | Q(meta_description=search)| Q(meta_keywords=search))
        blog = blog.objects.filter(Q(title__icontains=search) | Q(body__icontains=search) | Q(meta_description=search)| Q(meta_keywords=search))
        print(blog)
        data = {
            'course':course,
            'tutorial':tutorial,
            'blog':blog
        }

    return render(request,"search_result.html",data)