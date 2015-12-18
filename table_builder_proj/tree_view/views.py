from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from tree_view.models import TreeNode

class TreeView(View):
    def get(self, request):
        template = 'tree_view/m-tree-view.html'
        return render(request, template)

# View for creating a new account
class TreeNodeCreate(CreateView):
    model = TreeNode
    fields = ['text','parentNode']

# View for updating TreeNode information
class TreeNodeUpdate(UpdateView):
    model = TreeNode
    fields = ['text','parentNode']
    template_name_suffix = '_update_form'

# View for updating TreeNode information
class TreeNodeDelete(DeleteView):
    model = TreeNode
    success_url = reverse_lazy('treenode-list')
