from django.contrib import admin
from django.urls import path
from root import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('user/',views.user),
    path('employer/',views.employer),
    path('circular/',views.circular),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)