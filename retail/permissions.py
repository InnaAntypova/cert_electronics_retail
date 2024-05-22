from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):
    """ Проверка на владельца или модератора """
    def has_object_permission(self, request, view, obj):
        return (obj.owner == request.user and request.user.is_active) or request.user.is_staff or \
            request.user.is_superuser
