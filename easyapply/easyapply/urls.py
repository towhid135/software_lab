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
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('register/', views.register, name="register"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('admin/', admin.site.urls),
    path('addpsc/', views.addpsc),
    path('addjsc/', views.addjsc),
    path('addssc/', views.addssc),
    path('addhsc/', views.addhsc),
    path('addmasters/', views.addmasters),
    path('addphd/', views.addphd),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)