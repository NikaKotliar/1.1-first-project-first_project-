from django_filters import FilterSet, DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from api_with_restrictions.permissions import IsAutoriseOrReadOnly, IsOwnerOrReadOnly


class F(FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at','creator', 'status' ]


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    print(Advertisement.objects.all())
    serializer_class = AdvertisementSerializer
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    permission_classes = (IsAutoriseOrReadOnly, IsOwnerOrReadOnly)
    filter_backends = [DjangoFilterBackend]
    filter_class = F
    throttle_classes = [AnonRateThrottle,UserRateThrottle]

    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ["create", "update", "partial_update"]:
    #         return [IsAuthenticated()]
    #     return []
