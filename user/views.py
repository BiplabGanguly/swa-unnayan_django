from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user import AdminSignupSerializer,AdminLoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from . import models


class AdminRegistration(APIView):

    def post(self, req):
        user_serializer = AdminSignupSerializer.UserSignupSerializer(data=req.data)
        if user_serializer.is_valid():
            user_serializer.save()
            user = User.objects.get(username=user_serializer.validated_data['username'])
            token_obj, _ = Token.objects.get_or_create(user=user)
            response_data = user_serializer.data
            response_data['token'] = token_obj.key
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class AdminLoginView(APIView):
    
    def post(self,req):
        admin_login = AdminLoginSerializer.AdminLoginSerializer(data = req.data)
        if admin_login.is_valid():
            user = authenticate(username = admin_login.validated_data['username'], password = admin_login.validated_data['password'])
            if user.email == admin_login.validated_data['email']:
                user_data = models.User_Data.objects.get(user = user)
                token_obj, _ = Token.objects.get_or_create(user=user)
                login(req,user)
                # dictionary data
                response_data = {"token":token_obj.key}
                response_data['admin_id'] = user.id
                response_data['admin_username'] = user.username
                response_data['admin_permission'] = user_data.permission
                return Response(response_data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
class DataCountAdminDashboard(APIView):
    def get(self,req):
            total_faculty = models.User_Data.objects.filter(profile = 'faculty').count()
            responce_data = {'total_faculty':total_faculty}
            return Response(responce_data,status=status.HTTP_201_CREATED)