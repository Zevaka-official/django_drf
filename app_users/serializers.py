from rest_framework import serializers

from app_users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('password', 'is_superuser')
