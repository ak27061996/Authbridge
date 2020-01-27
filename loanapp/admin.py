from django.contrib import admin
from loanapp.models import LoanApplication

@admin.register(LoanApplication, site=admin.site)
class TransactionDetailsAdmin(admin.ModelAdmin):
    """
    """
    # list_display = ['id', 'title', 'plateform', 'editor_choice']
    list_per_page = 10



