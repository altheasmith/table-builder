import unittest
from django.test import Client
from django.test import TestCase
from bs4 import BeautifulSoup

# Function for extracting data from table
def extract_table_data(table):
    soup = BeautifulSoup(table)
    # All table data is contained in the <td> cells and <th> table headers
    td = soup.find_all('td')
    th = soup.find_all('th')
    data_list = td + th
    # This converts the cells to their string vales
    data_strings = [d.string for d in data_list]
    data = []
    for d in data_strings:
        # Necessary due to the last cell in the Totals row, which contains None
        # and thus can't be sorted
        if d != None:
            # Converting to lowercase as the statuses in the original page were
            # lowercase but they are uppercase in the new page
            data.append(d.lower())
    # Sorting the list of strings alphabetically so they can be properly compared
    data.sort()
    return data

class HTMLTest(unittest.TestCase):
    def test_html_of_original_page(self):
        # Table pulled from JQuery selector after new page was run with spaces removed
        # Ideally this would be pulled dynamically
        table = '<tbody><tr><th>Name</th><th>Amount</th><th>Status</th></tr><tr><td>CheckingAccount</td><td>15010</td><td>Active</td></tr><tr><td>EducationAccount</td><td>14500</td><td>Active</td></tr><tr><td>InvestmentAccount</td><td>1500500</td><td>Active</td></tr><tr><td>SavingsAccount</td><td>55020</td><td>Active</td></tr><tr><td>TravelFundAccount</td><td>25030</td><td>Inactive</td></tr><trclass="total"><td>Total</td><td>1610060</td><td></td></tr></tbody>'
        # Table pulled from JQuery selector after original page was run with spaces removed
        # Ideally this would be pulled dynamically
        table_orig = "<tbody><tr><td>Name</td><td>Amount</td><td>Status</td></tr><tr><td>CheckingAccount</td><td>15010</td><td>active</td></tr><tr><td>SavingsAccount</td><td>55020</td><td>active</td></tr><tr><td>TravelFundAccount</td><td>25030</td><td>inactive</td></tr><tr><td>InvestmentAccount</td><td>1500500</td><td>active</td></tr><tr><td>EducationAccount</td><td>14500</td><td>active</td></tr><tr><td><strong>Total</strong></td><td><strong>1610060</strong></td><td></td></tr></tbody>"
        # Extracting data from HTML
        data = extract_table_data(table)
        data_orig = extract_table_data(table_orig)
        # Assertion of equal data values
        self.assertEqual(data, data_orig)



'''
Code to run in Python shell to test the same functionality
from django.test import Client
from bs4 import BeautifulSoup
from table_builder.tests.tests_html import extract_table_data
table = '<tbody><tr><th>Name</th><th>Amount</th><th>Status</th></tr><tr><td>CheckingAccount</td><td>15010</td><td>Active</td></tr><tr><td>EducationAccount</td><td>14500</td><td>Active</td></tr><tr><td>InvestmentAccount</td><td>1500500</td><td>Active</td></tr><tr><td>SavingsAccount</td><td>55020</td><td>Active</td></tr><tr><td>TravelFundAccount</td><td>25030</td><td>Inactive</td></tr><trclass="total"><td>Total</td><td>1610060</td><td></td></tr></tbody>'
table_orig = "<tbody><tr><td>Name</td><td>Amount</td><td>Status</td></tr><tr><td>CheckingAccount</td><td>15010</td><td>active</td></tr><tr><td>SavingsAccount</td><td>55020</td><td>active</td></tr><tr><td>TravelFundAccount</td><td>25030</td><td>inactive</td></tr><tr><td>InvestmentAccount</td><td>1500500</td><td>active</td></tr><tr><td>EducationAccount</td><td>14500</td><td>active</td></tr><tr><td><strong>Total</strong></td><td><strong>1610060</strong></td><td></td></tr></tbody>"
data = extract_table_data(table)
data_orig = extract_table_data(table_orig)
data == data_orig
'''
