from django.test import TestCase
from table_builder.models import Account

class AccountTestCase(TestCase):
    def setUp(self):
        Account.objects.create(
            name="BoA",
            amount=20,
            status='Inactive'
        )
        Account.objects.create(
            name="CitiBank",
            amount=250,
            status='Active'
        )

    def test_account_info_stored_in_db(self):
        BoA = Account.objects.get(name="BoA")
        CitiBank = Account.objects.get(name="CitiBank")
        self.assertEqual(BoA.amount, 20)
        self.assertEqual(CitiBank.status, 'Active')

    def tearDown(self):
        Account.objects.get(name="BoA").delete()
        Account.objects.get(name="CitiBank").delete()
