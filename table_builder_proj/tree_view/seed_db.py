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

def AddChildNode(nodes):
    childNodes = []
    for node in nodes:
        childNode = TreeNode.objects.create(
            text=node['text']
        )
        childNode.save()
        childNodes.append(childNode)
        if 'nodes' in node.keys():
            childNodes = AddChildNode(node['nodes'])
    return childNodes

def AddNodes_Recursive(nodes):
    parentNodes = []
    for node in nodes:
        newNode = TreeNode.objects.create(
            text=node['text']
        )
        newNode.save()
        print(newNode, 'created')
        parentNodes.append(newNode)
        if 'nodes' in node.keys():
            childNodes = AddNodes_Recursive(node['nodes'])
            print(newNode, childNodes)
            for childNode in childNodes:
                childNode.parentNode = newNode
                print(childNode, 'parent saved as', newNode)
                childNode.save()
    print('childNodes returned', parentNodes)
    return parentNodes


'''
from tree_view.seed_db import items, tree, AddNodes_Recursive, AddChildNode
AddNodes_Recursive(items)

from tree_view.models import TreeNode
nodes = TreeNode.objects.all()
for node in nodes:
    print(node.parentNode, node.text)
'''
