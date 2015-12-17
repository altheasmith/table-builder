import unittest
from django.test import Client
from bs4 import BeautifulSoup

class HTMLTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def extract_table_data(table):
        soup = BeautifulSoup(table)
        td = soup.find_all('td')
        th = soup.find_all('th')
        data_list = td + th
        data = []
        for d in data_list:
            data.append(d.string)
        return data


    def test_html_of_original_page(self):
        table = '<tbody><tr><th>Name</th><th>Amount</th><th>Status</th></tr><tr><td>CheckingAccount</td><td>15010</td><td>Active</td></tr><tr><td>EducationAccount</td><td>14500</td><td>Active</td></tr><tr><td>InvestmentAccount</td><td>1500500</td><td>Active</td></tr><tr><td>SavingsAccount</td><td>55020</td><td>Active</td></tr><tr><td>TravelFundAccount</td><td>25030</td><td>Inactive</td></tr><trclass="total"><td>Total</td><td>1610060</td><td></td></tr></tbody>'
        table_orig = "<tbody><tr><td>Name</td><td>Amount</td><td>Status</td></tr><tr><td>CheckingAccount</td><td>15010</td><td>active</td></tr><tr><td>SavingsAccount</td><td>55020</td><td>active</td></tr><tr><td>TravelFundAccount</td><td>25030</td><td>inactive</td></tr><tr><td>InvestmentAccount</td><td>1500500</td><td>active</td></tr><tr><td>EducationAccount</td><td>14500</td><td>active</td></tr><tr><td><strong>Total</strong></td><td><strong>1610060</strong></td><td></td></tr></tbody>"
        soup = BeautifulSoup(table)
        soup_orig = BeautifulSoup(table_orig)

        self.AssertHTMLEqual(table1, table2)


def extract_table_data(table):
    soup = BeautifulSoup(table)
    td = soup.find_all('td')
    th = soup.find_all('th')
    data_list = td + th
    data = []
    for d in data_list:
        data.append(d.string)
    return data


'''
from django.test import Client
from bs4 import BeautifulSoup
from table_builder.tests.tests_html import extract_table_data
table = '<tbody><tr><th>Name</th><th>Amount</th><th>Status</th></tr><tr><td>CheckingAccount</td><td>15010</td><td>Active</td></tr><tr><td>EducationAccount</td><td>14500</td><td>Active</td></tr><tr><td>InvestmentAccount</td><td>1500500</td><td>Active</td></tr><tr><td>SavingsAccount</td><td>55020</td><td>Active</td></tr><tr><td>TravelFundAccount</td><td>25030</td><td>Inactive</td></tr><trclass="total"><td>Total</td><td>1610060</td><td></td></tr></tbody>'
table_orig = "<tbody><tr><td>Name</td><td>Amount</td><td>Status</td></tr><tr><td>CheckingAccount</td><td>15010</td><td>active</td></tr><tr><td>SavingsAccount</td><td>55020</td><td>active</td></tr><tr><td>TravelFundAccount</td><td>25030</td><td>inactive</td></tr><tr><td>InvestmentAccount</td><td>1500500</td><td>active</td></tr><tr><td>EducationAccount</td><td>14500</td><td>active</td></tr><tr><td><strong>Total</strong></td><td><strong>1610060</strong></td><td></td></tr></tbody>"
data = extract_table_data(table)
data_orig = extract_table_data(table_orig)
data = data_orig
'''
