from django.urls import path
from .views import BandListCreateView, AlbumListCreateView, IndexView, SongListCreateView, AlbumReviewListCreateView, AlbumReviewLikeListCreateView

urlpatterns = [
    path('bands/', BandListCreateView.as_view(), name='band-list-create'),
    path('albums/', AlbumListCreateView.as_view(), name='album-list-create'),
    path('songs/', SongListCreateView.as_view(), name='song-list-create'),
    path('reviews/', AlbumReviewListCreateView.as_view(), name='album-review-list-create'),
    path('likes/', AlbumReviewLikeListCreateView.as_view(), name='album-review-like-list-create'),
    path('', IndexView.as_view(), name='index'),
]
