from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from . models import  oxygensuppliers
from . serializer import oxysupSerializer

class oxyList(APIView):

    def get(self,request):
        oxy1 = oxygensuppliers.objects.all()
        serializer = oxysupSerializer(oxy1,many=True)
        return Response(serializer.data)

    def post(self):
        pass


def home(request):
    return render(request,"home.html")