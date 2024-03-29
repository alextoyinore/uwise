from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import status


class IsStudent(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='Student').exists():
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Student').exists():
            return True
        return False


class IsUwiseAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='UwiseAdmin').exists():
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='UwiseAdmin').exists():
            return True
        return False


class IsFacilitator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Facilitator').exists():
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Facilitator').exists():
            return True
        return False

