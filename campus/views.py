from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Detail, Measure, KPI, Control
from .serializers import DetailSerializer, MeasureSerializer, KPISerializer, ControlSerializer


@api_view(['GET'])
def campus_data_view(request):
    campus_data = {
        "company_name": "",
        "logo": "",
        "plane": "",
        "details": {
            "label": "Details",
            "icon": "file",
            "url": "http://127.0.0.1:8000/campus/api/details/"
        },
        "measures": {
            "label": "Measures",
            "icon": "chart",
            "url": "http://127.0.0.1:8000/campus/api/measures/"
        },
        "kpis": {
            "label": "KPIS",
            "icon": "chart-line",
            "url": "http://127.0.0.1:8000/campus/api/kpis/"
        },
        "control": {
            "label": "Control",
            "icon": "shield",
            "url": "http://127.0.0.1:8000/campus/api/controls/"
        }
    }
    return Response(campus_data, status=status.HTTP_200_OK)


class DetailViewSet(viewsets.ModelViewSet):
    serializer_class = DetailSerializer

    def get_queryset(self):
        return Detail.objects.all().order_by('-created_at')[:1]


class MeasureViewSet(viewsets.ModelViewSet):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer


class KPIViewSet(viewsets.ModelViewSet):
    queryset = KPI.objects.all()
    serializer_class = KPISerializer


class ControlViewSet(viewsets.ModelViewSet):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
