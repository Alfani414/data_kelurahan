from django.urls import path, include


# from .views import WargaListAPIView, WargaDetailAPIView
# from .views import PengaduanListAPIView, PengaduanDetailAPIView
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet

# urlpatterns = [
#     path('warga/', WargaListAPIView.as_view(), name='api_warga_list'),
#     path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='api_warga_detail'),

#     path('pengaduan/', PengaduanListAPIView.as_view(), name='api_pengaduan_list'),
#     path('pengaduan/<int:pk>/', PengaduanDetailAPIView.as_view(), name='api_pengaduan_detail'),
# ]

router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='warga')
router.register(r'pengaduan', PengaduanViewSet, basename='pengaduan')

urlpatterns = [
    path('', include(router.urls)),
]