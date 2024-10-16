from django.shortcuts import render
from information.models import Course
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    mymembers = Course.objects.all().values()
    context = {'lastname' : 'Aryan FIrazz',
               'mymembers': mymembers,
               'greeting' : 1,}
    return render (request,"index.html",context)

def course(request):
    if request.method == 'POST':
        c_code = request.POST['code' ]
        c_desc = request.POST[ 'desc' ]
        data=Course(code=c_code, description=c_desc)
        data.save()
        allcourse = Course.objects.all().values()
        dict = {
        'message' : 'Data Save',
        'allcourse': allcourse,
    }
    else:
        allcourse = Course.objects.all().values()
        dict = {
    'message':'Unsuccess',
    'allcourse': allcourse,
    }
        
    return render (request , "course.html", dict)

def search_course(request):
    if request.method == 'GET':
        # Retrieve the 'c_code' parameter and check if it's not None
        c_code = request.GET.get('c_code')

        if c_code:
            # Apply .upper() to ensure uppercase comparison
            data = Course.objects.filter(code=c_code.upper())
        else:
            data = None

        # Use a different name for the context dictionary
        context = {
            'data': data
        }
        
        return render(request, "search_course.html", context)
    
    # In case of non-GET requests (e.g., POST), return an empty template
    return render(request, "search_course.html")


def update_course(request,code):
    data=Course.objects.get(code=code)
    mymembers = Course.objects.all().values()
    dict = {
    'data':data,
    'mymembers': mymembers,}
    return render (request , "update_course.html", dict)

def save_update_course(request, code):
    c_desc= request.POST ['desc']
    data=Course.objects.get(code=code)
    data.description = c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))

def delete_course(request, code):
    data = Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse("course"))
    
def getvalue(request):
    return render (request, ('get_value.html'), {'product':product})

def view(request):
     context = {'lastname' : 'Your NAME',}
     return render (request, ('view.html'), context)

def database(request):
    mymembers = Course.objects.all().values()
    context = {'mymembers': mymembers,}
    return render (request,"database.html",context)


def save_data(request):
    if request.method == 'POST' :
        p_id = request.POST['prod_id' ]
        p_qty = request.POST ['prod_qty' ]

    for value in product:
        if value[0] == p_id:
            total = float(p_qty) * value[2]

            dict = {'p_code': p_id,'quantity': p_qty,'total' : total}
                    
    return render (request, ('save_data.html'), dict)

product = [ ["P001", "Pen", 2.50,8],["P002", "Ruler",1.50,10] ]