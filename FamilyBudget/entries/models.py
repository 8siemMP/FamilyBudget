from django.db import models

from budgets.models import Budget
from categories.models import Category


class Entry(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    amount = models.FloatField(default=0.)
    budget = models.ForeignKey(Budget, related_name='entries', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='entries', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} {self.amount} ({self.budget.name})'\
               + (f' [{self.category.name}]' if self.category else '')

    class Meta:
        verbose_name_plural = "Entries"
