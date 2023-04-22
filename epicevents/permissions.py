from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from users.models import MANAGEMENT, SALES, SUPPORT
from .models import Client


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.team.name == MANAGEMENT:
            return request.method in permissions.SAFE_METHODS


class ClientPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.team.name == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        return request.user.team.name == SALES

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return (
                request.user == obj.support_contact or request.user == obj.sales_contact
            )
        return request.user == obj.sales_contact


class ContractPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.team.name == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        return request.user.team.name == SALES

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return (
                request.user == obj.support_contact or request.user == obj.sales_contact
            )
        return request.user == obj.sales_contact


class EventPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.team.name == SUPPORT:
            return request.method in ("GET", "PUT")
        return request.user.team.name == SALES

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return (
                request.user == obj.support_contact or request.user == obj.sales_contact
            )
        else:
            if obj.event_status is True:
                raise PermissionDenied("You cannot update a finished event.")
            if request.user.team.name == SUPPORT:
                return request.user == obj.support_contact
            return request.user == obj.sales_contact
