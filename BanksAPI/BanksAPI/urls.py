# Main URL Configuration


from django.contrib import admin
from django.urls import path, include
from banking import urls as api_v1_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_v1_urls))
]
