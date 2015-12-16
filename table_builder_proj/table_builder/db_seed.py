from table_builder.models import Account

# Function for seeding database with Account information
accounts = [
        {
            'accountName': 'Checking Account',
            'amount': 15010,
            'status': 'Active'
        },
        {
            'accountName': 'Savings Account',
            'amount': 55020,
            'status': 'Active'
        },
        {
            'accountName': 'Travel Fund Account',
            'amount': 25030,
            'status': 'Inactive'
        },
        {
            'accountName': 'Investment Account',
            'amount': 1500500,
            'status': 'Active'
        },
        {
            'accountName': 'Education Account',
            'amount': 14500,
            'status': 'Active'
        }
    ]

def seed(accounts):
    for item in accounts:
        Account.objects.create(
            name=item['accountName'],
            amount=item['amount'],
            status=item['status'],
        )
'''
Text to run seed file in terminal:
from table_builder.db_seed import accounts, seed
seed(accounts)
'''
