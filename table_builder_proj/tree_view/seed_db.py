from tree_view.models import TreeNode

items = [{
    'text': 'Node Label',
    'nodes': [{'text': 'Child Node Label',
                'nodes': [{'text': 'Child Node Label',
                            'nodes':[{'text': 'Child Node Label',
                                        'nodes': []},
                                        {'text': 'Child Node Label'},
                                        {'text': 'Leaf Node Label'}
                                    ]
                }]
            },
    {'text': 'Leaf Node Label'}
    ]
}]


tree = [
  {
    'text': "Parent 1",
    'nodes': [
      {
        'text': "Child 1",
        'nodes': [
          {
            'text': "Grandchild 1"
          },
          {
            'text': "Grandchild 2"
          }
        ]
      },
      {
        'text': "Child 2"
      }
    ]
  },
  {
    'text': "Parent 2"
  },
  {
    'text': "Parent 3"
  },
  {
    'text': "Parent 4"
  },
  {
    'text': "Parent 5"
  }
];

def AddNodes_Recursive(nodes):
    parentNodes = []
    for node in nodes:
        newNode = TreeNode.objects.create(
            text=node['text']
        )
        newNode.save()
        parentNodes.append(newNode)
        if 'nodes' in node.keys():
            childNodes = AddNodes_Recursive(node['nodes'])
            for childNode in childNodes:
                childNode.parentNode = newNode
                childNode.save()
    return parentNodes


'''
from tree_view.seed_db import items, tree, AddNodes_Recursive
AddNodes_Recursive(items)

from tree_view.models import TreeNode
nodes = TreeNode.objects.all()
for node in nodes:
    print(node.parentNode, node.text)
'''
