from rest_framework import permissions


class IsAuthorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return (
            user.is_authenticated
            or request.method in permissions.SAFE_METHODS
        )

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )


class IsAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated
                and request.user.is_admin)

    def has_object_permission(self, request, view, obj):
        return (request.user and request.user.is_authenticated
                and request.user.is_admin)


class IsModeratorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return (
            user.is_authenticated and user.is_moderator
        )

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (
            user.is_authenticated and user.is_moderator
        )


class ReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
