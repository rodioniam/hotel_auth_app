from django.db import models
from django.utils import timezone
from api.models import Role


class User(models.Model):
    BUSINESS_ELEMENT = 'user'

    email = models.EmailField(unique=True)
    password_hash = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()

    role_id = models.ForeignKey(
        'api.Role',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='role_id'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
