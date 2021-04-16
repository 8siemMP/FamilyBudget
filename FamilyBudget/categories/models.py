from django.db import models
from budgets.models import Budget


class Category(models.Model):
    budget = models.ForeignKey(Budget, related_name='categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.budget.name})"

    class Meta:
        verbose_name_plural = "Categories"
