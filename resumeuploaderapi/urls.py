
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume/', ProfileView.as_view(),name='resume'),
    path('sahilget/', ProfileView.as_view(),name='sahilget'),
    path('sahildelete/<int:id>/', ProfileView.as_view(),name='sahildelete'),
    path('sahilupdate/<int:id>/', ProfileView.as_view(),name='sahilupdate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
