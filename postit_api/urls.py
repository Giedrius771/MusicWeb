from django.urls import path
from .views import BandListCreateView, AlbumListCreateView, IndexView, SongListCreateView, AlbumDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Add the index view URL pattern
    path('bands/', BandListCreateView.as_view(), name='band-list'),
    path('albums/', AlbumListCreateView.as_view(), name='album-list'),
    path('songs/', SongListCreateView.as_view(), name='song-list'),
    path('albums/<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),
]
