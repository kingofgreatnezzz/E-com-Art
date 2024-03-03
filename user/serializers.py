from djoser.serializers import UserCreateSerializer
from .models import MyUser

class CustomUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = MyUser
        fields = ('id', 'email', 'username','password')