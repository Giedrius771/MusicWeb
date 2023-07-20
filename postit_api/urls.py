from django.urls import path, include
from .views import BandListCreateView, AlbumListCreateView, IndexView, SongListCreateView, AlbumReviewListCreateView, AlbumReviewLikeListCreateView, login_view, logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('bands/', BandListCreateView.as_view(), name='band-list-create'),
    path('bands/', BandListCreateView.as_view(), name='band-list'),
    path('albums/', AlbumListCreateView.as_view(), name='album-list-create'),
    path('songs/', SongListCreateView.as_view(), name='song-list-create'),
    path('reviews/', AlbumReviewListCreateView.as_view(), name='album-review-list-create'),
    path('likes/', AlbumReviewLikeListCreateView.as_view(), name='album-review-like-list-create'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', IndexView.as_view(), name='index'),
]
