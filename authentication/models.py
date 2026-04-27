from django.db import models


class User(models.Model):
    BUSINESS_ELEMENT = 'user'

    email = models.EmailField(unique=True)
    password_hash = models.CharField()
    first_name = models.CharField()
    middle_name = models.CharField(null=True, blank=True)
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


class BlackListedToken(models.Model):
    token = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
