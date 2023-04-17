from rest_framework import permissions
from users.models import MANAGEMENT, SALES, SUPPORT


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.team.name == MANAGEMENT:
            return request.method in permissions.SAFE_METHODS


class ClientPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.team.name == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        return request.user.team.name == SALES


class ContractPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.team.name == SUPPORT:
            return False
        return request.user.team.name == SALES


class EventPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.team.name == SUPPORT:
            return request.method in ("GET", "PUT")
        return request.user.team.name == SALES
