from django.urls import path
from .views import BandListCreateView, AlbumListCreateView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Add the index view URL pattern
    path('bands/', BandListCreateView.as_view(), name='band-list-create'),
    path('albums/', AlbumListCreateView.as_view(), name='album-list-create'),
]
