from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index, name='index'),
    path('history', views.history, name="history"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('songpost/', views.songpost),
    path('songs/', views.songs, name='songs'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('watchlater', views.watchlater, name="watchlater"),
    path('logout_user', views.logout_user, name="logout_user"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)