from rest_framework import serializers
from .models import Language, Framework


class LanguageAPIView(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('__all__')


class FrameworkAPIView(serializers.ModelSerializer):
    class Meta:
        model = Framework
        fields = ('__all__')