# import requests
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


class HomeView(LoginRequiredMixin,TemplateView):
    template_name = "core/dashboard.html"


# ! Function to Access API from 3rd part Android App
# def home(request):
#     url = "endpoint"

#     headers = {}

#     response = requests.request("GET", url, headers=headers)
#     data = response.json()
#     return render(request, 'core/home.html',{'data':data})

# class API_Objects(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class API_Objects_details(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# def get_data(request):
#     labels = []
#     data = []

#     queryset = Post.objects.all()
#     for item in queryset:
#         labels.append(item.name)
#         data.append(item.author)

#         context = {
#             "labels": labels,
#             "data": data,
#         }
#     return render(request, 'core/index.html', context)

# class ChartData(APIView):
#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, format=None):
#         queryset=Post.objects.all()
        
#         labels = []
#         default_items = []

#         for item in queryset:
#             labels.append(item.name)
#             default_items.append(item.author)

#         data = {
#                 "labels": labels,
#                 "default": default_items,
#         }
#         return Response(data)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        labels = ["Blue","Yellow", "Green", "Purple", "Orange"]
        default_items = [23, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

