from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from articleapp.views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),  # ✅ 원래 홈으로 복구
    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),
    path('subscribe/', include('subscribeapp.urls')),
    path('likes/', include('likeapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
