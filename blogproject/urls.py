"""blogproject URL Configuration

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
from blog import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout_page'),
    path('signup', views.signup_page, name='signup_page'),
    path('blogform', views.blogform, name='blogform'),
    path('search', views.search, name='search'),
    path('blogview/<slug:slug>', views.blogview, name='blogview'),
    path('profile', views.profile, name='profile'),
    path('delete/<int:pk>/', views.delete_blog, name='delete_blog'),
    

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



