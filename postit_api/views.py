from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.response import Response
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike
from .serializers import BandSerializer, AlbumSerializer, SongSerializer, AlbumReviewSerializer, AlbumReviewCommentSerializer, AlbumReviewLikeSerializer
from django.shortcuts import render

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

class IndexView(TemplateView):
    template_name = 'index.html'
