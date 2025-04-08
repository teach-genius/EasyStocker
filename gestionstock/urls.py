from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts.views import logout_user,login_user
from . import settings
urlpatterns = [
    path("admin/", admin.site.urls),
    path("logout/", logout_user, name="logout"),
    path("login/", login_user, name="login"),
    path("", login_user),
    path("home/", include(("easygestion.urls", "easygestion"), namespace="home"),name="home"),  
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
