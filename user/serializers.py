from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    session_cookie = serializers.SerializerMethodField()

    class Meta:
        model = User
        extra_kwargs = {
            "password": {"write_only": True},
        }
        fields = "__all__"

    def get_session_cookie(self, instance):
        request = self.context.get('request')
        return request.session.session_key

    def create(self, validated_data):
        user = User(**validated_data)
        # Hash the user's password.
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, user_instance, validated_data):
        new_password = validated_data.pop('password', None)

        if new_password:
            user_instance.set_password(new_password)

        return super().update(user_instance, validated_data)