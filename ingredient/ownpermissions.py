from rest_framework import permissions


def has_object_permission(request, view, obj):
    # SAFE_METHODでGET,POSTのみ許容
    if request.method in permissions.SAFE_METHODS:
        return True
    return False


class OwnPermission(permissions.BasePermission):
    pass
