from django.test import TestCase
from tree_view.models import TreeNode


# Tests:

# Test Case for info storing correctly in Databases
class TreeNodeTestCase(TestCase):
    def setUp(self):
        parentNode = TreeNode.objects.create(
            text='New Node!'
        )
        parentNode.save()
        childNode = TreeNode.objects.create(
            text='Other Node',
            parentNode=parentNode
        )
        childNode.save()

    def test_node_info_stored_in_db(self):
        parent = TreeNode.objects.get(
            text='New Node!'
        )
        child = TreeNode.objects.get(
            parentNode=parent
        )
        self.assertEqual(child.text, 'Other Node')
