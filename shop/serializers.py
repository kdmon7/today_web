from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'last_login', 'date_joined', 'is_staff')


class N_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = n_Product
        fields = '__all__'


class D_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = d_Product
        fields = '__all__'