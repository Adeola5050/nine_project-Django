# from django.shortcuts import render
from rest_framework import viewsets, fields
from rest_framework.decorators import action
from rest_framework.response import Response

from natives.models import Cohort, Native
from natives.serializers import CohortSerializer, NativeSerializer

# Create your views here.
class NativeViewSet(viewsets.ModelViewSet):
    serializer_class= NativeSerializer
    queryset= Native.objects.all()
    @action(detail=False , methods=['get'])
    def call_adeola(self, request):
        return Response({})

        @action(detail=False, methods=['get'] )
        def show_name(self, request):
            return Response({"name":"John Doe"})


class CohortViewSet(viewsets.ModelViewSet):
    serializer_class = CohortSerializer
    queryset = Cohort.objects.all()
    @action(detail=False, methods=['get'])
    def get_cohort_by_name(self, request):
        cohort_name=self.request.query_params.get('cohort_name')
        print(cohort_name)
        cohort= Cohort.objects.get(name=cohort_name)
        serializer= CohortSerializer(cohort)
        return Response(serializer.data)
