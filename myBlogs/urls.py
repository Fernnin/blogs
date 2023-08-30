from django.contrib import admin
from django.urls import path
from blogs import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('write/', views.write),
    path('blog/', views.blog_read),
    path('about/', views.about),
    path('portfolio/', views.portfolio),
    path('specific/<int:id>/', views.view_specific),
    path('read/<int:id>/', views.read_specific)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)