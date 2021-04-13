from django.contrib import admin
from budgets.models import Budget, Privilege


class PrivilegeInline(admin.TabularInline):
    model = Privilege
    extra = 1


class BudgetAdmin(admin.ModelAdmin):
    inlines = (PrivilegeInline,)


admin.site.register(Budget, BudgetAdmin)
