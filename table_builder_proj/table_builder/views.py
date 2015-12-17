from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from table_builder.models import Account
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse_lazy


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


# View for creating a new account
class AccountCreate(CreateView):
    model = Account
    fields = ['name','amount','status']

# View for updating account information
class AccountUpdate(UpdateView):
    model = Account
    fields = ['name','amount','status']
    template_name_suffix = '_update_form'

# View for updating account information
class AccountDelete(DeleteView):
    model = Account
    success_url = reverse_lazy('account-list')
