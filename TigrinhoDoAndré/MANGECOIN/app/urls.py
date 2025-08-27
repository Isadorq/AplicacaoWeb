from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'user',UserView)
router.register(r'token',TokenView)

urlpatterns = router.urls