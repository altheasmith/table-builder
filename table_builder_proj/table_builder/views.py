from django.shortcuts import render
from django.views.generic import View
from table_builder.models import Account
from django.forms.models import model_to_dict
from django.http import JsonResponse


class MainView(View):
    def get(self, request):
        template = 'table_builder/table-builder.html'
        accounts = [model_to_dict(a) for a in Account.objects.all()]
        print(accounts)
        context = {'accounts': accounts}
        return render(request, template, context)

class AllAccounts(View):
    def get(self, request):
        accounts = [model_to_dict(a) for a in Account.objects.all()]
        print(accounts)
        context = {'accounts': accounts}
        JsonResponse(context)
