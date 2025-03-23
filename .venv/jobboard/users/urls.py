from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login_view, name = 'login'),
    path('register/', views.register_view, name = 'register'),
    path('logout/', views.logout_view, name = 'logout'),
    path('edit/', views.edit_view, name = 'edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


