from django.shortcuts import render
from django.views.generic import View

class TreeView(View):
    def get(self, request):
        template = 'tree_view/m-tree-view.html'
        return render(request, template)
