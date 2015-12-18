from django.test import TestCase

from django.test import TestCase
from tree_view import TreeNode


# Tests:

# Test Case for info storing correctly in Databases
class TreeNodeTestCase(TestCase):
    def setUp(self):
        parentNode = TreeNode.objects.create(
            text='New Node!'
        )
        parentNode.save()
        TreeNode.objects.create(
            text='Other Node',
            parentNode=parentNode
        )

    def test_node_info_stored_in_db(self):
        parent = TreeNode.objects.get(
            text='New Node!'
        )
        child = TreeNode.objects.filter(
            parentNode=parent
        )
        self.assertEqual(child.text, 'Other Node')

    def tearDown(self):
        TreeNode.objects.get(text="New Node!").delete()
        TreeNode.objects.get(name="Other Node").delete()
