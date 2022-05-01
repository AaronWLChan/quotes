from rest_framework import serializers
from quotes.quotes_api.models import Quote, Character, TVShow

class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quote
        fields = ['quote', 'said_by', 'season_number', 'episode_number', 'tv_show']

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name']

class TVShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = ['name']