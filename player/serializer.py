from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Player
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id','playname']