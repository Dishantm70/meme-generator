from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.permissions import UserPermission
from user.serializers import UserSerializer

class UserView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission, ]

    def get(self, request):
        user_instance = request.user
        serializer = self.serializer_class(user_instance, context={"request": request})

        return Response(serializer.data)


    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def put(self, request):
        user_instance = request.user

        serializer = self.serializer_class(user_instance, data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def patch(self, request):
        user_instance = request.user

        serializer = self.serializer_class(user_instance, data=request.data, partial=True, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class LoginView(APIView):
    permission_classes = []
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user_instance = authenticate(username=username, password=password, context={"request": request})

        if user_instance is not None:
            if user_instance.is_active:
                login(request, user_instance)
                return Response(status=status.HTTP_200_OK)
            else:
                message = {"message": "User account is inactive"}
                return Response(message, status=status.HTTP_404_NOT_FOUND)
        else:
            message = {"message": "incorrect username or password"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    def get(self, request):
        logout(request)
        request.session.flush()
        return Response({"success": True})