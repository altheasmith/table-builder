from django.shortcuts import render
from django.views.generic import View
from table_builder.models import Account
from django.forms.models import model_to_dict


# View for rendering main page
class AccountView(View):
    def get(self, request):
        template = 'table_builder/table-builder.html'
        return render(request, template)

# View for rendering original table-builder page
class TestOriginalView(View):
    def get(self, request):
        template = 'table_builder/table-builder-orig.html'
        return render(request, template)

class TableData(View):
    def post(self, request, *args, **kwargs):
        print(*args)
        return
