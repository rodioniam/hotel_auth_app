from .models import BusinessElement, AccessRoleRule


def check_permission(user, element_name, action):
    """
    Выполняет проверку доступа у пользователя к ресурсу.
    Берет role_id из user, определяет BusinessElement по element_name и
    action из AccessRoleRule
    """
    try:
        business_element = BusinessElement.objects.get(name=element_name)
        access_rule = AccessRoleRule.objects.get(
            role_id=user.role_id,
            element_id=business_element.id
        )
    except (BusinessElement.DoesNotExist, AccessRoleRule.DoesNotExist):
        return False

    action_map = {
        'read': 'can_read',
        'read_all': 'can_read_all',
        'edit': 'can_edit',
        'edit_all': 'can_edit_all',
        'create': 'can_create',
        'delete': 'can_delete',
        'delete_all': 'can_delete_all'
    }

    return getattr(access_rule, action_map[action])
