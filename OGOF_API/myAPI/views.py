
# views.py
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from .serializers import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# from  django import filter

# Create your views here.

class DevSearch(generics.ListCreateAPIView):
	search_fields = ['name','developer_category','country']
	filter_backends = (filters.SearchFilter,)
	queryset = DeveloperContacts.objects.all()
	serializer_class = DeveloperSerializer


@csrf_exempt
def developer_contacts(request):
    """
    List all code developers, or create a new developer.
    """
    if request.method == 'GET':
        developer = DeveloperContacts.objects.all()
        serializer = DeveloperSerializer(developer, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DeveloperSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def developer_detail(request, id):
    """
    Retrieve, update or delete a developer.
    """
    # print(dc)
    try:
        developer = DeveloperContacts.objects.get(id=id)
    except DeveloperContacts.DoesNotExist:
    	#pass
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DeveloperSerializer(developer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DeveloperSerializer(developer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        developer.delete()
        return HttpResponse(status=204)

