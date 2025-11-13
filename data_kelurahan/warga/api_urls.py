from django.urls import path
from .views import WargaListAPIView, WargaDetailAPIView
from .views import PengaduanListAPIView, PengaduanDetailAPIView

urlpatterns = [
    path('warga/', WargaListAPIView.as_view(), name='api_warga_list'),
    path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='api_warga_detail'),
    
    path('pengaduan/', PengaduanListAPIView.as_view(), name='api_pengaduan_list'),
    path('pengaduan/<int:pk>/', PengaduanDetailAPIView.as_view(), name='api_pengaduan_detail'),
]