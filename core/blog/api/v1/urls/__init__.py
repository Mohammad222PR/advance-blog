from django.urls import include
from django.urls import path

app_name = 'api-v1'

urlpatterns = [
    path('post/', include('blog.api.v1.urls.post')),
    path('category/', include('blog.api.v1.urls.category')),
    path('tag/', include('blog.api.v1.urls.tag'))

]