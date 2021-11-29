from rest_framework import routers
from .viewsets import *

router = routers.DefaultRouter()
router.register('users', UsersViewSet)

router = routers.DefaultRouter()
router.register('product', ProductViewSet)

router = routers.DefaultRouter()
router.register('shop', ShopViewSet)

router = routers.DefaultRouter()
router.register('shopitem', ShopItemViewSet)