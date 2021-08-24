"""ProjectApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from FORPWD import views
from django.conf.urls import url
from django.urls import path
from FORPWD.views import SearchView



app_name = "FORPWD"   


urlpatterns = [

    #Nav_pages

   
    path('home/', views.Home, name = 'home'),
    path('about/' ,views.aboutus, name='about/'),
    path('reg/',views.register, name='reg/'),
    url(r'^reg/register$', views.pwd, name='register'),
    
   
   
    # LoginForm
    path("register", views.register_request, name="register"),
    path('', views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"), 
    path('login', views.login_request, name="login"), 
    
    #Announcementpage
    path('news/' ,views.Announcement, name='news/'),
    url(r'^news/save$', views.commentSaving, name='savemsg'),


    #Staff_page
    path('admin/',admin.site.urls),
    path('applicants/' ,views.Adminpage, name='applicants'),
    url(r'^applicants/editinfo/(?P<id>\d+)$', views.editinfo, name='editinfo'),
    url(r'^applicants/editinfo/updateinfo/(?P<id>\d+)$', views.updateinfo, name='updateinfo'),
    url(r'^applicants/deleteinfo/(?P<id>\d+)$', views.deleteinfo, name='deleteinfo'),


    path('announce/' ,views.announce, name='post'),
    url(r'^announce/post$', views.Postii, name='post'),
    # url(r'^announce/post/updatepost/(?P<id>\d+)$', views.updatePost, name='updatepost'),
    # url(r'^post/updatepost/editpost(?P<id>\d+)$', views.editPost, name='editpost'),

    url(r'^applicants/status/(?P<id>\d+)$', views.statusurl, name='status'),
    url(r'^applicants/status/update/(?P<id>\d+)$', views.editstatus, name='editstatus'),

    # path('cashgift/', SearchView.as_view()),
    path('cashgift/', views.cashGift, name='cashgift'),
    url(r'^cashgift/received/(?P<id>\d+)$', views.cgcheker, name='received'),
    url(r'^cashgift/received/go/(?P<id>\d+)$', views.cashGiftUpdate, name='giftupdate'),



    
]
