
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseNotFound
from loanapp.models import LoanApplication
import os
import json
import csv
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from django.core.cache import cache
from loanapp.serializer import LoanApplicationSerializer
from django.contrib.auth.decorators import login_required



class loanApply(TemplateView):
    template_name = 'abc.html'
    # login_url = '/'
    
    def post(self, request):
        data = request.POST
        data = LoanApplication(
            amount=data.get('amount'),
            name=data.get('name'),
            dob=data.get('dob'),
            email=data.get('email'),
            phone=data.get('phone'))
        data.save()
        return HttpResponse("succesfully saved")


class loanfilter(TemplateView):
    template_name = 'loan.html'

    # @login_required
    def get_context_data(self):
        context = {}
        context['data'] = LoanApplication.objects.all()
        return context
    
    def post(self, request):
        id = request.POST.get('id', 0)
        if id:
            id = int(id)
            LoanApplication.objects.get(id=id).update(status=True)
        return HttpResponse("succesfully updated")
    







# class loanApplier(APIView):
#     """

#     Method: GET
#     Browser Test URL: http://127.0.0.1:8000/data/id
#     """

#     # def get(self, request, *args, **kwargs):
#     #     """handles get request"""
#     #     loanapplier = LoanApplication.objects.get(id=id)
#     #     serializer = LoanApplicationSerializer(loanapplier)
#     #     return Response(serializer.data)