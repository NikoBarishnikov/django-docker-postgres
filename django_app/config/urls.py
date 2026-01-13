from django.contrib import admin
from django.urls import path, include
from person.views import index  # импортируем index

urlpatterns = [
    path('', index, name='home'),  # корневой путь
    path('admin/', admin.site.urls),
    path('api/', include('person.urls')),
]




