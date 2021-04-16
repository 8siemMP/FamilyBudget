from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_delete

User = get_user_model()


class Budget(models.Model):
    name = models.CharField(max_length=100, blank=False, default='New Budget')
    owner = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    privileges = models.JSONField(default=dict)

    PERMISSION = {
        'O': 'Owner',
        'E': 'Editor',
        'R': 'Read-Only',
        'N': 'None'
    }

    def permission(self, user_pk):
        if self.owner.pk == user_pk:
            return 'Owner'
        try:
            return self.PERMISSION[self.privileges[f'{user_pk}']]
        except KeyError:
            return 'None'

    @property
    def summary(self):
        return self.entries.aggregate(Sum('amount'))['amount__sum']

    def __str__(self):
        return self.name


def clear_privileges(sender, instance, **kwargs):
    to_update = Budget.objects.filter(privileges__has_key=f"{instance.id}")
    for b in to_update:
        del b.privileges[f"{instance.id}"]
        b.save()


post_delete.connect(clear_privileges, sender=User)
