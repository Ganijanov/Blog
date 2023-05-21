from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from . import serializers
from main.models import Blog

@api_view(['GET'])
def blglst(request):
    blogs = Blog.objects.all()
    ser = serializers.BlogLiSer(blogs, many=True)
    return Response({'data':ser.data})

@api_view(['GET'])
def blgdl(request, id):
    blog = Blog.objects.get(id=id)
    ser = serializers.BlogDetSer(blog)
    return Response({'data':ser.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def mblg(request):
    blog = Blog.objects.filter(author=request.user)
    ser = serializers.BlogLiSer(blog, many=True)
    return Response({'data':ser.data})

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def crtblg(request):
    title = request.data['title']
    body = request.data['body']
    blog = Blog.objects.create(
        author = request.user,
        body = body,
        title = title
    )
    serializer = serializers.BlogDetSer(blog)
    return Response({'data':serializer.data})

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def updblg(request, id):
    title = request.data['title']
    body = request.data['body']
    blog = Blog.objects.get(id=id)
    if blog.author == request.user:
        blog.title = title
        blog.body = body
        blog.save()
        serializer = serializers.BlogDetSer(blog)
        return Response({'data':serializer.data})
    return Response({'data':'Sizning huquqingiz yoq'})

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def delblg(request, id):
    blog = Blog.objects.get(id=id)
    if blog.author == request.user:
        blog.delete()
        stats = True
    else:
        stats = False
    return Response({'success':stats})