from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token 
from django.contrib.auth import  authenticate,login 
from django.db.models import Q 
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class Jobview(APIView):
    """
    GET or  POST Job...
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        try:
            job = Job.objects.all()
            serializer = JobSerializer(job, many=True)
            return Response({"status":True,"message":"All job data fetched successfully",
            "data":serializer.data},status=status.HTTP_200_OK)
        except Exception:
                return Response({"status":False,"message":"Something went wrong",
                "errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST) 

    def post(self, request, format=None):
        try:
            serializer = JobSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":True,"message":"Job created successfully",
                "data":serializer.data},status=status.HTTP_201_CREATED)
        except Exception:
            return Response({"status":False,"message":"Something went wrong",
            "errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST) 


class JobDetail(APIView):
    """
    Retrieve, update or delete a Job instance.
    """
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            job = self.get_object(pk)
            serializer = JobSerializer(job)
            return Response({"status":True,"message":"Job data fetched successfully",
            "data":serializer.data},status=status.HTTP_200_OK)
        except Exception:
            return Response({"status":False,"message":"Something went wrong",
            "errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST) 

    def put(self,request,pk=None):
        # try:
        params=request.data 
        snippet=Job.objects.get(id=pk)
        print("snippet",snippet)
        serializer=JobSerializer(snippet,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status":True,"message":"Job updated successfully","data":serializer.data},status=status.HTTP_200_OK)
        # except Exception:
        #     return Response({"status":False,"message":"OOPS,Something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
    def delete(self, request, pk):
        try:
            job = self.get_object(pk)
            job.delete()
            return Response({"status":True,"message":"Job removed successfully"},status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response({"status":False,"message":"OOPS,Something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
