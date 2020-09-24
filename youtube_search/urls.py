from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import accounts.views
import search.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('search.urls')),
    path('accounts/', include('accounts.urls')),
    path('mylist/', include('mylist.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)