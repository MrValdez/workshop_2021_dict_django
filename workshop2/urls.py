from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('forum.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]

handler404 = "forum.views.handle_404"
handler403 = "forum.views.handle_403"