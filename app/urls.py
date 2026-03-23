from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("ourphilosophy/", views.ourphilosophy, name="ourphilosophy"),
    path("ourprograms/", views.ourprograms, name="ourprograms"),

    path("nurseryprogram/", views.nurseryprogram, name="nurseryprogram"),
    path("nurseryprogram2/", views.nurseryadvanced, name="nurseryprogram2"),
    path("toddlersprogram/", views.toddlersprogram, name="toddlersprogram"),
    path("toddlersprogram2/", views.toddlersadvanced, name="toddlersprogram2"),
    path("prekinderprogram/", views.prekinderprogram, name="prekinderprogram"),
    path("kindergartenprogram/", views.kindergartenprogram, name="kindergartenprogram"),

    path("ourfacilities/", views.ourfacilities, name="ourfacilities"),
    path("bushgarden/", views.bushgarden, name="bushgarden"),
    path("chefkitchen/", views.chefkitchen, name="chefkitchen"),

    path("gallery/", views.gallery, name="gallery"),

    path("kinder/", views.kinder, name="kinder"),
    path("kindergarten/", views.kindergarten, name="kindergarten"),
    path("kitchen/", views.kitchen, name="kitchen"),

    path("nurseryone/", views.nurseryone, name="nurseryone"),
    path("nurserytwo/", views.nurserytwo, name="nurserytwo"),
    path("nursery/", views.nursery, name="nursery"),
    path("prekinder/", views.prekinder, name="prekinder"),
    

    path("toddlerone/", views.toddlerone, name="toddlerone"),
    path("toddlertwo/", views.toddlertwo, name="toddlertwo"),
    path("toddlers/", views.toddlers, name="toddlers"),

    path("getintouch/", views.getintouch, name="getintouch"),
    path("ourcentre/", views.ourcentre, name="ourcentre"),
    path("workwithus/", views.workwithus, name="workwithus"),

    path("enrollnow/", views.enrollnow, name="enrollnow"),

    path("enrol-submit/", views.enrol_submit, name="enrol_submit"),
    path("contact-submit/", views.contact_submit, name="contact_submit"),
]

# ✅ PUT THIS OUTSIDE LIST
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)