import unittest
from django.test import Client

class ClientTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        # api = 'b'{"Account":"http://testserver/api/v1/Account/"}''
        # api_account = 'b'[{"name":"Checking Account","amount":15010,"status":"Active"},{"name":"Education Account","amount":14500,"status":"Active"},{"name":"Investment Account","amount":1500500,"status":"Active"},{"name":"Savings Account","amount":55020,"status":"Active"},{"name":"Travel Fund Account","amount":25030,"status":"Inactive"}]''

    def test_main_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api_function(self):
        response = self.client.get('/api/v1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"Account":"http://testserver/api/v1/Account/"}')

    def test_api_account(self):
        response = self.client.get('/api/v1/Account/')
        self.assertEqual(response.status_code, 200)


# For Running Client Tests in Django Shell

# HTML From Main Page
'''
from django.test import Client
c = Client()
response = c.get('/')
response.content
'''

# HTML From Original Page
'''
from django.test import Client
c = Client()
response = c.get('/orig/')
response.content
'''

# API is functioning: should return True
'''
from django.test import Client
c = Client()
response = c.get('/api/v1/')
response.content
response.content == b'{"Account":"http://testserver/api/v1/Account/"}'
'''

# API Account Data: should return True
'''
from django.test import Client
c = Client()
response = c.get('/api/v1/Account/')
response.content
response.content == b'[{"name":"Checking Account","amount":15010,"status":"Active"},{"name":"Education Account","amount":14500,"status":"Active"},{"name":"Investment Account","amount":1500500,"status":"Active"},{"name":"Savings Account","amount":55020,"status":"Active"},{"name":"Travel Fund Account","amount":25030,"status":"Inactive"}]'
'''
