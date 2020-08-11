from django.contrib import admin
from django.urls import path
from root import views


urlpatterns = [
    path('user/',views.user),
    path('admin/', admin.site.urls),
]
