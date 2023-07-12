from django.http import JsonResponse

from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import api_view

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import GameSerializer, ProductSerializer, ReviewSerializer
from .models import Game, ProductBase, Review

from .filter import ProductFilter
from .classes import ListCreateUpdateDestroyDS, RetrieveUpdateDestroyDS
from .permissions import IsAuthor


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

        queryset = ProductBase.objects.filter(game_id=game_id)

        filter_instance = self.filterset_class(data=self.request.GET, queryset=queryset)
        queryset = filter_instance.qs

        return queryset


class ProductDetailEntryGroupView(RetrieveUpdateDestroyDS):
    permission_classes = [permissions.AllowAny]
    permission_classes_by_actions = {'update': [permissions.IsAdminUser, IsAuthor],
                                     'destroy': [permissions.IsAdminUser, IsAuthor]}

    queryset = ProductBase.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()


class ProductCreateApiView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer




#
# class ProductDetailView(viewsets.ModelViewSet):
#
#
# class GameParamRetrieveApiView(generics.RetrieveAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameParamSerializer
#
#
# class GameNameRetrieveApiView(generics.RetrieveAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer
#
#
# @api_view(['GET'])
# def get_user_avatar(request, slug):
#     return JsonResponse({
#         'avatar': request.product.get_user_avatar()
#     })
#
#
# class AllProductApiView(generics.ListAPIView):
#     """Return all products that connected with user."""
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         user_id = self.kwargs['slug_field']
#         queryset = ProductBase.objects.filter(user_id=user_id)
#         return queryset
#
#
# @api_view(['POST']) # некоректная
# def product_create(request):
#     form = ProductForm(data=request.data)
#     if form.is_valid():
#         product = form.save(commit=False)
#         product.save()
#         serializer = ProductSerializer(product)
#         return JsonResponse(serializer.data, safe=False)
#     else:
#         return JsonResponse({'message': form.errors.as_json()}, safe=False)
