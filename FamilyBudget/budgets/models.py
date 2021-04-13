from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Budget(models.Model):
    name = models.CharField(max_length=100, blank=False, default='New Budget')
    privileges = models.ManyToManyField(User, related_name='budgets', through='Privilege')

    def __str__(self):
        return self.name


OWNER = 'O'
EDITOR = 'E'
READ_ONLY = 'R'


class Privilege(models.Model):
    ROLES = (
        (OWNER, 'Owner'),
        (EDITOR, 'Editor'),
        (READ_ONLY, 'Read-only')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=ROLES)

    class Meta:
        order_with_respect_to = 'budget'
        unique_together = [
            ('user', 'budget'),
        ]
