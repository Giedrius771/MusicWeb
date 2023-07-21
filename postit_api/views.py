from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike, Comment
from .serializers import BandSerializer, AlbumSerializer, SongSerializer, AlbumReviewSerializer, AlbumReviewCommentSerializer, AlbumReviewLikeSerializer, CommentSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView



class BandListCreateView(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class BandCreateView(APIView):
    def post(self, request, format=None):
        serializer = BandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BandListView(ListView):
    model = Band
    serializer_class = BandSerializer
    template_name = 'bands.html'
    context_object_name = 'bands'

    def get_queryset(self):
        return Band.objects.all()

class BandDetailView(generics.RetrieveAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

# Rename BandCommentListCreateView to BandCommentListView
class BandCommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        band_id = self.kwargs['band_id']
        return Comment.objects.filter(band_id=band_id)

    def perform_create(self, serializer):
        band_id = self.kwargs['band_id']
        serializer.save(user=self.request.user, band_id=band_id)

class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetailView(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

# Rename AlbumCommentListCreateView to AlbumCommentListView
class AlbumCommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        album_id = self.kwargs['album_id']
        return Comment.objects.filter(album_id=album_id)

    def perform_create(self, serializer):
        album_id = self.kwargs['album_id']
        serializer.save(user=self.request.user, album_id=album_id)

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
    permission_classes = [permissions.IsAuthenticated]

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
    permission_classes = [permissions.IsAuthenticated]

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

def logout_user(request):
    logout(request)
    return redirect('login')


class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('song-list-create')  # Redirect to song list after successful login
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'login.html')


class SongLikeListCreateView(generics.ListCreateAPIView):
    queryset = AlbumReviewLike.objects.all()
    serializer_class = AlbumReviewLikeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        song_id = self.request.query_params.get('song_id', None)
        if song_id is not None:
            return AlbumReviewLike.objects.filter(song_id=song_id)
        return AlbumReviewLike.objects.all()

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('Jūs jau palikote patiktuką šiai dainelei!')
        song = Song.objects.get(pk=self.kwargs['song_id'])
        serializer.save(user=self.request.user, song=song)


from .views import logout_user, login_user, SongLikeListCreateView