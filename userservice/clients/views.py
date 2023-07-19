import requests

from django.http import JsonResponse

from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

import os

from .classes import ListCreateUpdateDestroyDS
from .models import User, Reviews
from .permissions import IsUser, IsReviewAuthor
from .serializers import (UserSerializer, SignupSerializer,
                          UserUpdateSerializer, ChangePasswordSerializer,
                          ReviewSerializer)


@api_view(['GET'])
def me(request):
    """Using for get and refresh jwt token on frontend."""
    return JsonResponse({
        'id': request.user.id,
        'username': request.user.username,
        'email': request.user.email,
        'avatar': request.user.get_avatar()
    })


class SignUpApiView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SignupSerializer

    def perform_create(self, serializer):
        serializer.save()
        user_id = serializer.instance.id

        data = {
            'user_id': user_id,
        }
        create_account_url = os.environ.get('CREATE_ACCOUNT_API_URL')
        response = requests.post(create_account_url, data=data)

        if response.status_code != 200:
            return Response({'error': 'Failed to create account'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'message': 'Account created successfully'}, status=status.HTTP_201_CREATED)


class EditProfileApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUser]
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.queryset, pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_update(self, serializer):
        if 'file' in self.request.data:
            image = self.request.data['file']
            serializer.save(avatar=image)
        else:
            serializer.save()


class ChangePasswordApiView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [IsUser]

    def get_object(self, queryset=None):
        obj = self.request.user
        self.check_object_permissions(self.request, obj)
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailApiView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ReviewsEntryGroup(ListCreateUpdateDestroyDS):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    permission_classes_by_action = {'update': [IsReviewAuthor],
                                    'destroy': [IsReviewAuthor]}

    def get_queryset(self):
        profile_id = self.kwargs['pk']
        return Reviews.objects.filter(user_id=profile_id)
