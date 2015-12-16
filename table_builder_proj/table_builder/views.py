from django.shortcuts import render
from django.views.generic import View
from table_builder.models import Account


class AccountView(View):
    def get(self, request):
        template = 'table_builder/table-builder.html'
        return render(request, template)
