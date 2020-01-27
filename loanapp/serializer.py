from rest_framework import serializers
from loanapp.models import LoanApplication


class LoanApplicationSerializer(serializers.ModelSerializer):
    """
    Serializer class for email template
    """

    class Meta:
        """meta class"""
        model = LoanApplication
        fields = (
            'id', 'name', 'phone', 'amount', 'email', 'status')