from django.shortcuts import render, redirect
from .models import Enquiry, Contact
from .models import Gallery

def home(request):
    return render(request,"index.html")


def about(request):
    return render(request,"get-to-know-us.html")


def ourphilosophy(request):
    return render(request,"our-philosophy.html")


def ourprograms(request):
    return render(request,"our-programs.html")


def nurseryprogram(request):
    return render(request,"our-programs/nursery.html")


def toddlersprogram(request):
    return render(request,"our-programs/toddlers.html")


def prekinderprogram(request):
    return render(request,"our-programs/pre-kinder.html")


def kindergartenprogram(request):
    return render(request,"our-programs/kindergarten.html")


def ourfacilities(request):
    return render(request,"our-facilities.html")


def bushgarden(request):
    return render(request,"our-facilities/bush-garden.html")


def chefkitchen(request):
    return render(request,"our-facilities/chef-kitchen.html")


def gallery(request):
    return render(request,"gallery.html")


def kinder(request):
    return render(request,"gallery/kinder.html")


def kindergarten(request):
    return render(request,"gallery/kindergarten.html")


def kitchen(request):
    return render(request,"gallery/kitchen.html")


def nurseryone(request):
    return render(request,"gallery/nursery-one.html")


def nurserytwo(request):
    return render(request,"gallery/nursery-two.html")


def nursery(request):
    return render(request,"gallery/nursery.html")


def prekinder(request):
    return render(request,"gallery/pre-kinder.html")


def toddlerone(request):
    return render(request,"gallery/toddler-one.html")


def toddlertwo(request):
    return render(request,"gallery/toddler-two.html")


def toddlers(request):
    return render(request,"gallery/toddlers.html")


def getintouch(request):
    return render(request,"get-in-touch.html")


def ourcentre(request):
    return render(request,"get-in-touch/our-centre-ballarat.html")


def workwithus(request):
    return render(request,"get-in-touch/work-with-us.html")


def enrollnow(request):
    return render(request,"enrol-now.html")


# ✅ FORM SUBMIT VIEW (CLEAN & WORKING)
def enrol_submit(request):
    if request.method == "POST":
        print(request.POST)  # DEBUG

        Enquiry.objects.create(
            child_name=request.POST.get('child_name'),
            child_dob=request.POST.get('child_dob'),
            program=request.POST.get('program'),
            start_date=request.POST.get('start_date'),

            parent_name=request.POST.get('parent_name'),
            parent_phone=request.POST.get('parent_phone'),
            parent_email=request.POST.get('parent_email'),

            message=request.POST.get('message'),
        )

        return redirect('enrollnow')

    return redirect('enrollnow')



def contact_submit(request):
    if request.method == "POST":
        print(request.POST)  # DEBUG

        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )

        return redirect('getintouch')

    return redirect('getintouch')
def gallery(request):
    images = Gallery.objects.all()
    featured_images = Gallery.objects.filter(is_featured=True)

    return render(request, "gallery.html", {
        "images": images,
        "featured_images": featured_images
    })
