from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token
class SignUpSerializer(serializers.ModelSerializer):
    
    email=serializers.EmailField(required=True, max_length=100)
    username=serializers.CharField(required=True,max_length=40)
    first_name=serializers.CharField(required=True,max_length=40)
    last_name=serializers.CharField(required=True,max_length=40)
    dob=serializers.DateField(required=True)
    password=serializers.CharField(required=True, max_length=100, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email','username','password','first_name','last_name','dob']
        extra_kwargs = {'password':{'write_only':True}}
    
    def validate(self, attrs):
        email = attrs.get('email','')
        username = attrs.get('username','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('Email is already in use')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':('Username is already in use')})
        return super().validate(attrs)
    
    def create(self, validated_data):
        password=validated_data.pop('password',None)
        user=super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user