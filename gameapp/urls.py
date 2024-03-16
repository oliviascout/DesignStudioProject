from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('game-detail/<slug:slug>/', views.game_detail, name='game_detail'),
    path('<slug:slug>/', views.review_detail, name='review_detail')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)