from django_filters import FilterSet, DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.permissions import IsAutoriseOrReadOnly, IsOwnerOrReadOnly



class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    print(Advertisement.objects.all())
    serializer_class = AdvertisementSerializer

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAutoriseOrReadOnly, IsOwnerOrReadOnly)
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filter_class = AdvertisementFilter

    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ["create", "update", "partial_update"]:
    #         return [IsAuthenticated()]
    #     return []
