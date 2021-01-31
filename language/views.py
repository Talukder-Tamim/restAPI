from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Language, Framework
from .serializers import LanguageAPIView, FrameworkAPIView


class LanguageView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Language.objects.all()
    serializer_class = LanguageAPIView


class FrameworkView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Framework.objects.all()
    serializer_class = FrameworkAPIView


class FrameworkAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Framework.objects.all()
    serializer_class = FrameworkAPIView


class FrameworkNewView(generics.ListCreateAPIView):
    queryset = Framework.objects.all().order_by('-id')[:2]
    serializer_class = FrameworkAPIView