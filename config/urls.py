from django.contrib import admin
from django.urls import path, include          #追加（アプリ）
from django.conf import settings               #追加（静的ファイル）
from django.conf.urls.static import static     #追加（静的ファイル）


urlpatterns = [
path('admin/', admin.site.urls),
path('account/', include('allauth.urls')),
path('', include('mainapp.urls')),               #追加（アプリ）

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)          #追加（静的ファイル）