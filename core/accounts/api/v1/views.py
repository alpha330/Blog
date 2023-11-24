from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from jwt.exceptions import ExpiredSignatureError,InvalidSignatureError
from django.conf import settings
from accounts.api.v1.serializer import ( 
                                        RegistrationSerializer, 
                                        CustomAuthTokenSerializer, 
                                        CustomTokenObtainPairSerializer, 
                                        ChangePasswordSerializer, 
                                        ProfileSerializer, 
                                        ReconfirmationApiSerializer, 
                                        ResetPasswordSerializer, 
                                        PasswordResetLinkSerializer
                                        )
from django.contrib.auth import get_user_model
from accounts.models import Profile
from django.shortcuts import get_object_or_404
from mail_templated import EmailMessage
from ..utils import EmailThread
from rest_framework_simplejwt.tokens import RefreshToken
import jwt


User = get_user_model()

class RegistrationApiView(generics.GenericAPIView):
    
    serializer_class = RegistrationSerializer
    
    def post(self,request,*args,**kwargs):
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data["email"]
            data = {
                "email":email                
            }
            user_obj = get_object_or_404(User,email = email)
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage('email/activation_email.tpl', {'token': token}, 'admin@admin.com', [email])
            EmailThread(email_obj).run()
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    
class CustomAuthToken(ObtainAuthToken):
    
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        
class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
class ChangePasswordApiView(generics.GenericAPIView):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    def get_object(self,queryset=None):
        obj = self.request.user
        return obj
    def put(self,request,*args,**kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password":["wrong_password"]},status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({'detail':'password changes successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class ProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset,user=self.request.user)
        return obj
    
class TestEmailSend(generics.GenericAPIView):
    
    
    
    def get(self,request,*args,**kwarg):
        self.email = "alimahmoodi22@gmail.com"
        user_obj = get_object_or_404(User,email = self.email)
        token = self.get_tokens_for_user(user_obj)
        email_obj = EmailMessage('email/hello.tpl', {'token': token}, 'admin@admin.com', ['alimahmoodi22@gmail.com'])
        EmailThread(email_obj).run()
        return Response("Email has been Send")
    
    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

class ActivationApiView(APIView):
    
    def get(self, request,token,*args,**kwargs):
        try:
            token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id= token.get("user_id")
            
        except ExpiredSignatureError:
            return Response({"details":"Token has been Expire"},status=status.HTTP_400_BAD_REQUEST)
        except InvalidSignatureError:
            return Response({"details":"Invalid Token Signature"},status=status.HTTP_400_BAD_REQUEST)
        user_obj = User.objects.get(pk = user_id)
        if user_obj.is_verified:
            return Response({"detail":"Account Verified before"})
        user_obj.is_verified = True
        user_obj.save()
        return Response({"detail":"Activated Successfully"})
        return Response("OK")
        
class ReconfirmationApiView(generics.GenericAPIView):
    
    serializer_class = ReconfirmationApiSerializer
    def post(self, request,*args,**kwargs):
        serializer = ReconfirmationApiSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data["user"]
        token = self.get_tokens_for_user(user_obj)
        email_obj = EmailMessage('email/activation_email.tpl', {'token': token}, 'admin@admin.com', to=[user_obj.email])
        EmailThread(email_obj).run()
        return Response ({"detail":"User Activation Resend Successfully"},status=status.HTTP_200_OK)
    
    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    
class ResetLinkPasswordSendApiView(generics.GenericAPIView):
    """
    This API view is used to send reset password link to user
    """
    serializer_class = PasswordResetLinkSerializer
    def post(self,request,*args,**kwargs):
        serializer = PasswordResetLinkSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data["user"]
        token = self.get_tokens_for_user(user_obj)
        email_obj = EmailMessage('email/reset_password.tpl', {'token': token}, 'admin@admin.com', to=[user_obj.email])
        EmailThread(email_obj).run()
        return Response ({"detail":"Reset Password Link send Successfully"},status=status.HTTP_200_OK)

    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    
class ResetPasswordApiView(generics.GenericAPIView):
    """
     This API View is used for resetting the password of a user
    """
    model = User
    serializer_class = ResetPasswordSerializer
    def put(self,request,token,*args,**kwargs):
        try:
            token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id= token.get("user_id")
        except ExpiredSignatureError:
            return Response({"details":"Token has been Expire"},status=status.HTTP_400_BAD_REQUEST)
        except InvalidSignatureError:
            return Response({"details":"Invalid Token Signature"},status=status.HTTP_400_BAD_REQUEST)
        
        self.object = User.objects.get(pk = user_id)
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({'detail':'new password has been set successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)