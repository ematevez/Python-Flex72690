from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('AppCoder.urls')),
    path('blog/',include('AppBlog.urls')),
    path('nuevo/', include('AppNuevo.urls')),
]
