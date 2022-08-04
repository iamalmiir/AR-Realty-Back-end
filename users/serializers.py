from rest_framework import serializers

from users.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("full_name", "email", "user_name", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        registered_user = self.Meta.model(**validated_data)
        
        if password is not None:
            registered_user.set_password(password)

        registered_user.save()
        return registered_user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "avatar", "default_avatar", "full_name", "email", "user_name", "password")
        extra_kwargs = {"password": {"write_only": True}}
