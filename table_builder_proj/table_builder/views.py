from django.shortcuts import render
from django.views.generic import View
from table_builder.models import Account
from django.forms.models import model_to_dict


class AccountView(View):
    def get(self, request):
        template = 'table_builder/table-builder.html'
        accounts = [model_to_dict(a) for a in Account.objects.all()]
        total = 0
        for account in accounts:
            total += account['amount']
        print(total)
        context = {'accounts':accounts,'total':total}
        return render(request, template)
