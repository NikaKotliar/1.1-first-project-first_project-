from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

from logistic.views import ProductViewSet, StockViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)
# router.register('stocks-products', StockProductViewSet)


urlpatterns = [
                  path('admin/', admin.site.urls),
              ] + router.urls
