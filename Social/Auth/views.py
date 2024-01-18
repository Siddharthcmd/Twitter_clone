from django.shortcuts import render
from .serializer import SignUpSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .token import create_jwt_pair


# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class=SignUpSerializer
    permission_classes=[]
    def post(self,request:Request):
        data=request.data
        serializer=SignUpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response={
                "message":"User Created Successfully",
                "data":serializer.data}
            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    
    serializer_class=SignUpSerializer
    permission_classes=[]
    
    def post(self, request: Request):
        email=request.data.get('email')
        password=request.data.get('password')
        user=authenticate(email=email,password=password)
        
        if user: 
            tokens=(create_jwt_pair(user))
            response = {"message":"User Logged In Successfully",
                             "token":tokens}
            return Response(data=response,status=status.HTTP_200_OK)
        
        return Response(data={"message":"Invalid Credentials"},status=status.HTTP_401_UNAUTHORIZED)
    
    def get(self,request: Request):
        content={"user":str(request.user),"auth":str(request.auth)}
        return Response(content,status=status.HTTP_200_OK)    
