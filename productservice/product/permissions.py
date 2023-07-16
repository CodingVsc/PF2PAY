from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('PUT', 'PATCH', 'DELETE'):
            return request.user and request.user.id == obj.user_id
        return False

