from django.shortcuts import render
from requests import post
import json
import io
from rest_framework.parsers import JSONParser
from .models import studnt
from .serializers import studntSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def studnt_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = studntSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data has been created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')