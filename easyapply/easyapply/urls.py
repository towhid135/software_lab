from django.contrib import admin
from django.urls import path
from root import views


urlpatterns = [
    path('user/',views.user),
    path('admin/', admin.site.urls),
    path('addpsc/', views.addpsc),
    path('addjsc/', views.addjsc),
    path('addssc/', views.addssc),
    path('addhsc/', views.addhsc),
    path('addmasters/', views.addmasters),
    path('addphd/', views.addphd),
]
