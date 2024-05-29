from django.urls import path, include
from rest_framework.routers import DefaultRouter
from campus import views

router = DefaultRouter()
router.register('details', views.DetailViewSet, basename='detail')
router.register('measures', views.MeasureViewSet, basename='measure')
router.register('kpis', views.KPIViewSet, basename='kpi')
router.register('controls', views.ControlViewSet, basename='control')

urlpatterns = [
    path('index', views.campus_data_view, name='campus_data'),
    path('api/', include(router.urls)),
]
