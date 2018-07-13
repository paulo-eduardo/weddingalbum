from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from pictures.serializers import PicturesSerializer
from pictures.models import Pictures
import tinify
import boto3
import json

class PicturesList(APIView):
    permission_classes = (AllowAny, )

    def post(self, request, format=None):
        picture = request.FILES['img']
        serializer = PicturesSerializer(data= {
            'name' : picture.name
        })

        tinify.key = 'u1QV4IRunMT64XkAZdBg99xSqflppWjd'

        source = tinify.from_file(picture)
        resized = source.resize(
            method="cover",
            width=400,
            height=280
        ).to_buffer()

        if serializer.is_valid():

            serializer.save()
            s3 = boto3.resource('s3')
            s3.Bucket('albumcasamento').put_object(Key=str(serializer.data['id']) + picture.name, Body=resized)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, format=None):
        pictures = Pictures.objects.all()
        serializer = PicturesSerializer(pictures, many=True)
        return Response(serializer.data)

class PicturesToApprove(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, format=None):
        pictures = Pictures.objects.filter(status=None)
        s3 = boto3.client('s3')

        for item in pictures:
            url = s3.generate_presigned_url('get_object',
                                Params={
                                    'Bucket': 'albumcasamento',
                                    'Key': str(item.id) + item.name,
                                },                                  
                                ExpiresIn=3600)
            item.url = url

        serializer = PicturesSerializer(pictures, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        picture = Pictures.objects.get(pk=request.data['id'])
        serializer = PicturesSerializer(picture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PicturesApproved(APIView):
    permission_classes = (AllowAny, )

    def get(self, format=None):
        pictures = Pictures.objects.filter(status=True)
        s3 = boto3.client('s3')

        for item in pictures:
            url = s3.generate_presigned_url('get_object',
                                Params={
                                    'Bucket': 'albumcasamento',
                                    'Key': str(item.id) + item.name,
                                },                                  
                                ExpiresIn=3600)
            item.url = url

        serializer = PicturesSerializer(pictures, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        picture = Pictures.objects.get(pk=request.data['id'])
        serializer = PicturesSerializer(picture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)