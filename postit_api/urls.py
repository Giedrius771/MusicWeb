from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import (
    BandListCreateView, BandDetailView, BandCommentListView, AlbumListCreateView, AlbumDetailView, AlbumCommentListView,
    SongListCreateView, AlbumReviewListCreateView, AlbumReviewLikeListCreateView,
    AlbumReviewDeleteView, SongDeleteView, LikeDeleteView, CommentList, AllCommentList, SongLikeListCreateView, login_user, logout_user
)
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='api-index'),  # Redirect to index.html
    path('bands/', views.BandListView.as_view(), name='band-list'),
    path('bands/create/', views.BandCreateView.as_view(), name='band-list-create'),
    path('bands/', BandListCreateView.as_view(), name='band-list-create'),
    path('bands/<int:band_id>/', BandDetailView.as_view(), name='band-detail'),
    path('bands/<int:band_id>/comments/', BandCommentListView.as_view(), name='band-comment-list-create'),
    path('albums/', AlbumListCreateView.as_view(), name='album-list-create'),
    path('albums/<int:album_id>/', AlbumDetailView.as_view(), name='album-detail'),
    path('albums/<int:album_id>/comments/', AlbumCommentListView.as_view(), name='album-comment-list-create'),
    path('songs/', SongListCreateView.as_view(), name='song-list-create'),
    path('reviews/', AlbumReviewListCreateView.as_view(), name='album-review-list-create'),
    path('likes/', AlbumReviewLikeListCreateView.as_view(), name='album-review-like-list-create'),
    path('reviews/<int:review_id>/', AlbumReviewDeleteView.as_view(), name='album-review-delete'),
    path('songs/<int:pk>/', SongDeleteView.as_view(), name='song-delete'),
    path('likes/<int:pk>/', LikeDeleteView.as_view(), name='like-delete'),
    path('songs/<int:song_id>/comments/', CommentList.as_view(), name='song-comment-list-create'),
    path('comments/', AllCommentList.as_view(), name='all-comment-list'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('songs/likes/', SongLikeListCreateView.as_view(), name='song-like-list-create'),
    # Add other URL patterns for your API paths here
    path('api-auth/', include('rest_framework.urls')),  # Include DRF authentication URLs
]
