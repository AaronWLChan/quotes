from random import choice
from rest_framework import viewsets
from quotes.quotes_api.serializers import QuoteSerializer, TVShowSerializer, CharacterSerializer
from quotes.quotes_api.models import Quote, Character, TVShow
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class QuoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows quotes to be viewed or edited.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    # permission_classes = [permissions.IsAdmin]

    @action(detail=False, methods=['GET'], name="Get random")
    def random(self, request):
        
        try:
            pks = self.queryset.values_list('pk', flat=True)
            random_pk = choice(pks)
            random_obj = self.queryset.get(pk=random_pk)

            serializer = self.serializer_class(random_obj, context={'request':request})

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows characters to be viewed or edited.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    # permission_classes = [permissions.IsAdminUser]

class TVShowViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows characters to be viewed or edited.
    """
    queryset = TVShow.objects.all()
    serializer_class = TVShowSerializer
    # permission_classes = [permissions.IsAdminUser]
