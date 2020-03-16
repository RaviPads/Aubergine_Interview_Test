from django.urls import path, include
from .views import Users, UserVerification, Images, ImagesCompressPath
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', Users)
router.register(r'images', Images)
urlpatterns = [
    path('', include(router.urls)),
    path('verification/<str:VerStr>/', UserVerification.as_view()),
    path('image_path/<int:pk>/', ImagesCompressPath.as_view()),
]
