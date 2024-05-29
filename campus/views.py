from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Detail, Measure, KPI, Control
from .serializers import DetailSerializer, MeasureSerializer, KPISerializer, ControlSerializer


@api_view(['GET'])
def campus_data_view(request):
    campus_data = {
        "company_name": "campus",
        "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSRNrFZy3HZqtvOQaM94XeGnIKNVVC0tge0g&s",
        "plane": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTR14oasNG0ZjQt14aB4HBrP4peIfgcEvqIzZIQ8B4mIA&s",
        "data": [
            {
                "key": "details",
                "label": "Details",
                "icon": "DescriptionIcon",
                "url": "/details"
            },
            {
                "key": "measures",
                "label": "Measures",
                "icon": "BarChartIcon",
                "url": "/measures"
            },
            {
                "key": "kpis",
                "label": "KPIS",
                "icon": "TrendingUpIcon",
                "url": "/kpis"
            },
            {
                "key": "control",
                "label": "Control",
                "icon": "SecurityIcon",
                "url": "/controls"
            }
        ]
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
