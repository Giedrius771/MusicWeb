from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike, Comment
from .serializers import BandSerializer, AlbumSerializer, SongSerializer, AlbumReviewSerializer, AlbumReviewCommentSerializer, AlbumReviewLikeSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer


class BandListCreateView(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class AlbumReviewListCreateView(generics.ListCreateAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer

class AlbumReviewCommentListCreateView(generics.ListCreateAPIView):
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer

class AlbumReviewLikeListCreateView(generics.ListCreateAPIView):
    queryset = AlbumReviewLike.objects.all()
    serializer_class = AlbumReviewLikeSerializer

class AlbumReviewDeleteView(generics.DestroyAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user == request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'You do not have permission to delete this review.'}, status=status.HTTP_403_FORBIDDEN)

class SongDeleteView(generics.DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class LikeDeleteView(generics.DestroyAPIView):
    queryset = AlbumReviewLike.objects.all()
    serializer_class = AlbumReviewLikeSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user == request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'You do not have permission to delete this like.'}, status=status.HTTP_403_FORBIDDEN)


class SongCommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        song_id = self.kwargs['song_id']
        return Comment.objects.filter(song_id=song_id)

    def perform_create(self, serializer):
        song_id = self.kwargs['song_id']
        serializer.save(user=self.request.user, song_id=song_id)

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        song_id = self.kwargs['song_id']
        song = Song.objects.get(pk=song_id)
        return Comment.objects.filter(song=song)

    def perform_create(self, serializer):
        song_id = self.kwargs['song_id']
        song = Song.objects.get(pk=song_id)
        serializer.save(user=self.request.user, song=song)


class AllCommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
