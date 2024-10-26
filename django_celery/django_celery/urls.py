from django.contrib import admin
from django.urls import path, include
from publish.views import view_post
from main.views import verify

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<slug:slug>/', view_post, name='view_post'),
    path('verify/<uuid>', verify, name='verify'),
]