"""
Выполняется при каждом запросе и проверяет есть ли токен у пользователя, достает его и записывает в request.
Это нужно чтобы в дальнейшем отличать пользователй по токенам
"""

from .utils import decode_token
from .models import User


class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'Authorization' in request.headers and request.headers.get('Authorization').startswith('Bearer'):
            try:
                token = request.headers.get('Authorization').split(' ')[1]
                user_id = decode_token(token)['user_id']
                request.auth_user = User.objects.get(id=user_id)
            except Exception:
                request.auth_user = None
        else:
            request.auth_user = None

        response = self.get_response(request)
        return response
