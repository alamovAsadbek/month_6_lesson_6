from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', include('forms.urls', namespace="form")),
    path('', include('news.urls', namespace="news")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('users/', include('users.urls', namespace="users")),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('form/', include('forms.urls', namespace="form")),
    path('', include('news.urls', namespace="news"))
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
