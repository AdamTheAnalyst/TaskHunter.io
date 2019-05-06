from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id',
                  'email',
                  'password',
                  'first_name',
                  'last_name'
                  ]

    def __str__(self):
        return "{}".format(self.username)

    def create(self, validated_data):
        validated_data['username'] = validated_data["email"]
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user