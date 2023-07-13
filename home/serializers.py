from rest_framework import serializers
from home.models import ShortURL


class URLSerializer(serializers.ModelSerializer):

    original_url = serializers.URLField(required=True)

    class Meta:
        model = ShortURL
        fields = ('original_url', )





