from django.urls import path
from .views import BandListCreateView, AlbumListCreateView, SongListCreateView, AlbumReviewListCreateView, AlbumReviewLikeListCreateView, AlbumReviewDeleteView, SongDeleteView, LikeDeleteView, CommentList, AllCommentList

urlpatterns = [
    path('bands/', BandListCreateView.as_view(), name='band-list-create'),
    path('albums/', AlbumListCreateView.as_view(), name='album-list-create'),
    path('songs/', SongListCreateView.as_view(), name='song-list-create'),
    path('reviews/', AlbumReviewListCreateView.as_view(), name='album-review-list-create'),
    path('likes/', AlbumReviewLikeListCreateView.as_view(), name='album-review-like-list-create'),
    path('reviews/<int:review_id>/', AlbumReviewDeleteView.as_view(), name='album-review-delete'),
    path('songs/<int:pk>/', SongDeleteView.as_view(), name='song-delete'),
    path('likes/<int:pk>/', LikeDeleteView.as_view(), name='like-delete'),
    path('songs/<int:song_id>/comments/', CommentList.as_view(), name='song-comment-list-create'),
    path('comments/', AllCommentList.as_view(), name='all-comment-list'),
]
