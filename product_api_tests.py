"""
TYRO Product API test cases
Author: Mingxuan Fu
"""

import requests as req
import json, pprint, unittest

# set consts
API_VER = 1
URL = "https://public.cdr.tyro.com/cds-au/v1/banking/products"
BUSINESS_LOAN_ID = "b5ee1091-e3af-4517-8f8f-8cc52434472b"

pp = pprint.PrettyPrinter()

header_params = {"x-v": str(API_VER)}
invalid_header_params = {"x-v": str(-1)}

def get_term_deposits(products):
    """
    Helper function to get term deposit products from list of products
    """
    return list(filter(lambda product: 'Term Deposit' in product['name'], products))

class TestProductApi(unittest.TestCase):
    def test_get_products(self):
        r = req.get(URL, headers=header_params)

        self.assertEqual(r.status_code, 200)

        # Get term deposit products
        products = json.loads(r.text)['data']['products']
        term_deposits = get_term_deposits(products)

        # Print term deposit products to terminal
        print('\nterm deposit products\n')
        pp.pprint(term_deposits)

    def test_get_product_detail(self):
        r = req.get(f'{URL}/{BUSINESS_LOAN_ID}', headers=header_params)

        self.assertEqual(r.status_code, 200)

        # Get Business loan eligibility
        data = json.loads(r.text)['data']
        eligibility = data['eligibility']
        
        # Print eligibility to terminal
        print('\neligibility of business loan\n')
        pp.pprint(eligibility)

    def test_get_products_invalid_headers(self):
        r = req.get(f'{URL}/{BUSINESS_LOAN_ID}', headers=bad_header_params)

        # invalid header should result in status 400
        self.assertEqual(r.status_code, 400)
    
    def test_get_product_detail_missing_headers(self):
        r = req.get(URL, headers={})

        # missing header x-v value should result in status 400
        self.assertEqual(r.status_code, 400)

if __name__ == '__main__':
    unittest.main()