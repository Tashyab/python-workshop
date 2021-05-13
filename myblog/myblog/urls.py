
from django.contrib import admin
from django.urls import path
from . import views
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/',views.home, name='home'),
    path('posts/',views.posts, name='posts'),
    path('about/',views.about, name='about'),
    path('contactus/',views.contactus, name='contactus'),
    path('signup/',views.signup, name='signup'),
    path('terms/',views.terms, name='terms'),
    path('privacy-policy/',views.policy, name='policy'),
]
