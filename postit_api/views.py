from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.response import Response
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike
from .serializers import BandSerializer, AlbumSerializer, SongSerializer, AlbumReviewSerializer, AlbumReviewCommentSerializer, AlbumReviewLikeSerializer
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework.generics import ListCreateAPIView
from .models import Band
from .serializers import BandSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class BandListCreateView(ListCreateAPIView):
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

class IndexView(TemplateView):
    template_name = 'index.html'

@login_required
def index(request):
    return render(request, 'index.html', {'user': request.user})



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            message = 'Invalid login credentials. Please try again.'
            return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')
