from django.contrib import admin
from django.urls import path
from root import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('user/', views.user,name="user"),
    path('skill/', views.skill,name="skill"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('employer/', views.employer,name="employer"),
    path('circular/', views.circular,name="circular"),
    path('register/', views.register, name="register"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('admin/', admin.site.urls),

    path('addpsc/', views.addpsc,name="addpsc"),
    path('addjsc/', views.addjsc,name="addjsc"),
    path('addssc/', views.addssc,name="addssc"),
    path('addhsc/', views.addhsc,name="addhsc"),
    path('addhonours/', views.addhonours, name="addhonours"),
    path('addmasters/', views.addmasters,name="addmasters"),
    path('addphd/', views.addphd,name="addphd"),
    path('results/', views.results,name="results"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
