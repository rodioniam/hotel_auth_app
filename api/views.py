from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Role, AccessRoleRule
from .serializers import RoleSerializer, AccessRoleRuleSerializer
from .permissions import check_permission
from .utils import unauthorized, forbidden


class RoleListView(APIView):
    def get(self, request):
        if request.auth_user is None:
            return unauthorized()

        if not check_permission(request.auth_user, Role.BUSINESS_ELEMENT, 'read_all'):
            return forbidden()

        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)

        return Response(serializer.data)

    def post(self, request):
        if request.auth_user is None:
            return unauthorized()

        if not check_permission(request.auth_user, Role.BUSINESS_ELEMENT, 'create'):
            return forbidden()

        serializer = RoleSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data

            Role.objects.create(
                name=validated_data['name'],
                description=validated_data['description']
            )
            return Response({'message': 'Role created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleDetailView(APIView):
    def patch(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        # скорее всего позже надо будет обновить действие на edit_all
        if not check_permission(request.auth_user, Role.BUSINESS_ELEMENT, 'edit'):
            return forbidden()
        try:
            role = Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            return Response({'error': 'Role not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer_update = RoleSerializer(data=request.data)

        if serializer_update.is_valid():
            update_data = serializer_update.validated_data
            for k, v in update_data.items():
                setattr(role, k, v)
            role.save()

            serializer = RoleSerializer(role)
            return Response(serializer.data)
        return Response(serializer_update.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Role.BUSINESS_ELEMENT, 'delete'):
            return forbidden()
        try:
            role = Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            return Response({'error': 'Role not found'}, status=status.HTTP_404_NOT_FOUND)

        role.delete()

        return Response({'message': f'Role {role.name} deleted'}, status=status.HTTP_200_OK)


class AccessRoleListView(APIView):
    def get(self, request):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, AccessRoleRule.BUSINESS_ELEMENT, 'read_all'):
            return forbidden()

        role_rules = AccessRoleRule.objects.all()
        serializer = AccessRoleRuleSerializer(role_rules, many=True)

        return Response(serializer.data)


class AccessRoleDetailView(APIView):
    def patch(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        # скорее всего позже надо будет обновить действие на edit_all
        if not check_permission(request.auth_user, AccessRoleRule.BUSINESS_ELEMENT, 'edit'):
            return forbidden()
        try:
            role_rule = AccessRoleRule.objects.get(pk=pk)
        except AccessRoleRule.DoesNotExist:
            return Response({'error': 'Role rule not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer_update = AccessRoleRuleSerializer(data=request.data)

        if serializer_update.is_valid():
            update_data = serializer_update.validated_data
            for k, v in update_data.items():
                setattr(role_rule, k, v)
            role_rule.save()

            serializer = AccessRoleRuleSerializer(role_rule)
            return Response(serializer.data)
        return Response(serializer_update.errors, status=status.HTTP_400_BAD_REQUEST)
