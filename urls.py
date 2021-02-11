from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet,UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profile',UserProfileViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
]