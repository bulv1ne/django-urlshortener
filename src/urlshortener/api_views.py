from rest_framework import mixins, serializers, viewsets

from .models import ShortUrl, Word


class ShortUrlSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    def validate(self, data):
        if Word.objects.unused_words().first() is None:
            raise serializers.ValidationError("No more words available")
        return data

    def get_short_url(self, instance):
        return self.context["request"].build_absolute_uri(instance.get_absolute_url())

    def create(self, validated_data):
        return ShortUrl.create_shorturl(validated_data["url"])

    class Meta:
        model = ShortUrl
        fields = ("url", "short_url")


class CreateShortUrlViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer
