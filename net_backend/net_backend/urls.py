
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # remember to include the slash in the url path 
    
    path('api/', include('accounts.urls')),
    path('api/search/', include('search.urls')),
    path('api/post/', include('post.urls')),
    path('admin/', admin.site.urls),
   
]
