from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, permissions

from .classes import RetrieveUpdateDestroyDS
from .filter import ProductFilter
from .models import Game, ProductBase
from .permissions import IsAuthor
from .serializers import GameSerializer, ProductSerializer


class ListGameApiView(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.AllowAny]


class ListProductApiView(generics.ListAPIView):
    """Return all products connected with Game object."""
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        game_id = self.kwargs['pk']

        queryset = ProductBase.objects.filter(game_id=game_id).filter(is_active=True)

        filter_instance = self.filterset_class(data=self.request.GET, queryset=queryset)
        queryset = filter_instance.qs

        return queryset


class ProductDetailEntryGroupView(RetrieveUpdateDestroyDS):
    permission_classes = [permissions.AllowAny]
    permission_classes_by_actions = {'update': [IsAuthor],
                                     'destroy': [IsAuthor]}

    queryset = ProductBase.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()


class ProductCreateApiView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
