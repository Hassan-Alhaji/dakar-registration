from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    IndexView, RegistrationCreateView, RegistrationSuccessView,
    DashboardView, RegistrationListView, RegistrationDetailView,
    ExportExcelView,
    RegistrationViewSet, StatsViewSet
)

router = DefaultRouter()
router.register(r'registrations', RegistrationViewSet)
router.register(r'stats', StatsViewSet)

urlpatterns = [
    # UI Routes
    path('', IndexView.as_view(), name='index'),
    path('register/', RegistrationCreateView.as_view(), name='register'),
    path('register/success/', RegistrationSuccessView.as_view(), name='registration_success'),
    
    # Admin UI Routes
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/registrations/', RegistrationListView.as_view(), name='registration_list'),
    path('dashboard/registrations/<int:pk>/', RegistrationDetailView.as_view(), name='registration_detail'),
    path('dashboard/export/', ExportExcelView.as_view(), name='export_excel'),

    # API Routes
    path('api/', include(router.urls)),
]
