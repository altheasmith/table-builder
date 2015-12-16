from django.shortcuts import render
from django.views.generic import View
from table_builder.models import Account
from django.forms.models import model_to_dict


# View for rendering main page
class AccountView(View):
    def get(self, request):
        template = 'table_builder/table-builder.html'
        return render(request, template)
