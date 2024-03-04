
from django.contrib import admin
from django.urls import path, include

from gameapp.apps import GameappConfig

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gameapp.urls'))
]


