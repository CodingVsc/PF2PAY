from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from rest_framework import generics, permissions, status

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from .forms import SignupForm, ProfileForm
from .models import User, Reviews
from .serializers import UserSerializer, SignupSerializer, UserUpdateSerializer, ChangePasswordSerializer, ReviewSerializer
from .classes import RetrieveUpdateDestroyDS, ListCreateUpdateDestroyDS
from .permissions import IsUser


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


class EditProfileApiView(RetrieveUpdateDestroyDS):
    permission_classes = [IsUser, permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

    def perform_update(self, serializer):
        image = self.request.data['file']
        if image:
            serializer.save(avatar=image)
        else:
            serializer.save()


class ChangePasswordApiView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_object(self, queryset=None):
        obj = self.request.user
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
    permission_classes_by_action = {'update': [IsCommentAuthor],
                                    'destroy': [IsCommentAuthor]}

    def get_queryset(self):
        profile_id = self.kwargs['pk']
        return Reviews.objects.filter(user_id=profile_id)












# @api_view(['POST'])
# @authentication_classes([])
# @permission_classes([])
# def signup(request):
#     data = request.data
#     message = 'success'
#
#     form = SignupForm({
#         'email': data.get('email'),
#         'username': data.get('username'),
#         'password1': data.get('password1'),
#         'password2': data.get('password2'),
#     })
#
#     if form.is_valid():
#         user = form.save()
#         user.save()
#     else:
#         message = form.errors.as_json()
#
#     return JsonResponse({'message': message}, safe=False)
#
#
# @api_view(['POST'])
# def editprofile(request):
#     user = request.user
#     email = request.data.get('email')
#
#     if User.objects.exclude(id=user.id).filter(email=email).exists():
#         return JsonResponse({'message': 'email already exists'})
#     else:
#         form = ProfileForm(request.POST, request.FILES, instance=user)
#
#         if form.is_valid():
#             form.save()
#
#         serializer = UserSerializer(user)
#
#         return JsonResponse({'message': 'information updated', 'user': serializer.data})
#
#
# @api_view(['POST'])
# def editpassword(request):
#     user = request.user
#
#     form = PasswordChangeForm(data=request.POST, user=user)
#
#     if form.is_valid():
#         form.save()
#
#         return JsonResponse({'message': 'success'})
#     else:
#         return JsonResponse({'message': form.errors.as_json()}, safe=False)
#
#
# @api_view(['GET'])
# @authentication_classes([])
# @permission_classes([])
# @login_required
# def check_auth(request):
#     return Response({'isAuthenticated': True}, status=status.HTTP_200_OK)
#
#
# class ProfileUserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'pk'
#     #lookup_url_kwarg = 'slug'
