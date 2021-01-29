from django.shortcuts import render
from rest_framework import generics
from .models import Language, Framework
from .serializers import LanguageAPIView, FrameworkAPIView


class LanguageView(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageAPIView


class FrameworkView(generics.ListAPIView):
    queryset = Framework.objects.all()
    serializer_class = FrameworkAPIView
