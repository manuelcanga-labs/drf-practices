from rest_framework import permissions


class EsPropietario(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.propietario:
            return True

        return False