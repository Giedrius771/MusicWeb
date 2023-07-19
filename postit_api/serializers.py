from rest_framework import serializers
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    bands = BandSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = '__all__'

class AlbumReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumReview
        fields = '__all__'

class AlbumReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumReviewComment
        fields = '__all__'

class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumReviewLike
        fields = '__all__'
