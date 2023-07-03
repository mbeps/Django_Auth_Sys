from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Extending the `ModelSerializer` class to create a serializer for the User model.
    This serializer will be used to convert the User model to and from JSON.

    Args:
        serializers (serializers.ModelSerializer): The ModelSerializer class to extend.
    """
    class Meta(object):
        """Meta class to define the model and fields to serialize."""
        model: User = User 
        fields: list[str] = ['id', 'username', 'password', 'email']