"""
URL configuration for cops_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from cops_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('register',views.register),
    path('police_register',views.police_register,name='police_register'),
    path('login',views.my_login,name='login'),
    path('log_out',views.log_out,name='log_out'),
    path('edit_police/<int:id>',views.edit_police,name='edit_police'),
    path('edit_user/<int:id>',views.edit_user,name='edit_user'),
    path('my_profile/<int:id>',views.my_profile,name='my_profile'),
    path('file_complaint/<int:id>',views.file_complaint,name='file_complaint'),
    path('show_complaint',views.show_complaint,name='show_complaint'),
    path('view_feedback/<int:id>',views.view_feedback,name='view_feedback'),
    path('my_case',views.my_case,name='my_case'),
    path('history',views.history,name='history'),
    path('edit_status/<int:id>',views.edit_status,name='edit_status'),
    path('police_profile',views.police_profile,name='police_profile'),
    path('notification',views.my_notification,name='notification'),
    path('police_notification',views.police_notification,name='police_notification'),
    path('redir_complaint',views.redir_complaint,name='redir_complaint'),
    path('redir_police',views.redir_police,name='redir_police'),
    path('add_feedback/<int:id>',views.add_feedback,name='add_feedback'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)