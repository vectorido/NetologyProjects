from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        queryset = Stock.objects.all()
        search = self.request.query_params.get('search', None)
        products = self.request.query_params.get('products', None)
        if search is not None:
            queryset = queryset.filter(positions__product__title__icontains=search)
        if products is not None:
            queryset = queryset.filter(positions__product__id=products)
        return queryset.distinct()

    pagination_class = LimitOffsetPagination
