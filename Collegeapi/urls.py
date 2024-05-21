from django.contrib import admin
from django.urls import path, include
from .views import home_page  # This line is needed if you have a home_page view to include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include('api.urls')),  # Correct the module name to 'api.urls'
    path("", home_page, name="home"),  # Optional: Add this if you have a home_page view
]
