from .utils import decode_token
from .models import User


class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'Authorization' in request.headers and request.headers.get('Authorization').starstwith('Bearer'):
            try:
                token = request.headers.get('Authorization').split(' ')[1]
                user_id = decode_token(token)['user_id']
                request.user = User.objects.get(id=user_id)
            except Exception:
                request.user = None
        else:
            request.user = None

        response = self.get_response(request)
        return response
