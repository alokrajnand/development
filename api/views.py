from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import jobline
from .serializers import joblineSerializer


# Create your views here.

class joblineList(APIView):

    # a get request to fetch all the job
    def get(self, request):
        jobs = jobline.objects.all()
        serializer = joblineSerializer(jobs, many=True)
        return Response(serializer.data)
