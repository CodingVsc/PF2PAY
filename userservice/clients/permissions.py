from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('PUT', 'PATCH'):
            return request.user and request.user.id == obj.id
        return True


class IsReviewAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('PUT', 'PATCH'):
            return request.user and request.user.id == obj.user_id
        return True
