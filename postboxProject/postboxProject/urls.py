from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
]

handler404 = views.page_not_found