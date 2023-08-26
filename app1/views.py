from django.shortcuts import render,HttpResponse


# Create your views here.


def home(request):
    from app1.models import course
    courses = course.objects.all()
   
    data ={
         'courses':courses,
        
      }

    return render(request, "index.html",data)

def about(request):
   
    return render(request, "about.html")

def courses(request):
    from app1.models import course
    courses = course.objects.all()
   
    data ={
         'courses':courses,
        
      }

    return render(request, "courses.html",data)

def index(request,slug,id):
    id=id
    slug = slug
    print(id)
    from app1.models import tutorial
    tutorial = tutorial.objects.filter(course=id)
    data = {
        'slug': slug,
        'tutorial':tutorial
       
    }
    return render(request, "course-index.html",data)

def tutorial(request,course,slug,cid):
    from app1.models import tutorial,course
    
    course=course
    
    slug=slug
    cid=cid

    tutorials = tutorial.objects.filter(slug=slug)[0]
    # courseid = tutorial.course.id
  
    tutorial_list = tutorial.objects.filter(course__id=cid)

    
    
    data = {
        'tutorials':tutorials,
        'tutorial_list':tutorial_list,
        'cid':cid,
        
    }
    return render(request, "tutorial.html",data)