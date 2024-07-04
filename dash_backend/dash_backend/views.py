from .models import Report
from .serializers import ReportSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET'])
def reportlist(request,format=None):
    if request.method == 'GET':
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)

        return JsonResponse(serializer.data,safe=False)
@api_view(['GET'])
def filter_end_year(request,year):
    if request.method == 'GET':
        reports = Report.objects.filter(end_year = year)
        serializer = ReportSerializer(reports, many=True)

        return JsonResponse(serializer.data,safe=False)
@api_view(['GET'])
def filter_topic(request,topic_name):
    if request.method == 'GET':
        reports = Report.objects.filter(topic = topic_name)
        serializer = ReportSerializer(reports, many=True)

        return JsonResponse(serializer.data,safe=False)
@api_view(['GET'])
def filter_sector(request,sec):
    if request.method == 'GET':
        reports = Report.objects.filter(sector = sec)
        serializer = ReportSerializer(reports, many=True)

        return JsonResponse(serializer.data,safe=False)
@api_view(['GET'])
def filter_region(request,reg):
    if request.method == 'GET':
        reports = Report.objects.filter(region = reg)
        serializer = ReportSerializer(reports, many=True)

        return JsonResponse(serializer.data,safe=False)
@api_view(['GET'])
def filter_pestle(request,pest):
    if request.method == 'GET':
        reports = Report.objects.filter(pestle = pest)
        serializer = ReportSerializer(reports, many=True)

        return JsonResponse(serializer.data,safe=False)
@api_view(['GET'])
def filter_source(request,src):
    if request.method == 'GET':
        reports = Report.objects.filter(source = src)
        serializer = ReportSerializer(reports, many=True)

        return JsonResponse(serializer.data,safe=False)
@api_view(['GET'])
def filter_country(request,country_name):
    if request.method == 'GET':
        reports = Report.objects.filter(country = country_name)
        serializer = ReportSerializer(reports, many=True)

        return JsonResponse(serializer.data,safe=False)