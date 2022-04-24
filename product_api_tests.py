import re
import requests as req
import sys, json, pprint, unittest

api_ver = 1
url = "https://public.cdr.tyro.com/cds-au/v1/banking/products"
business_loan_id = "b5ee1091-e3af-4517-8f8f-8cc52434472b"

pp = pprint.PrettyPrinter()

header_params = {"x-v": str(api_ver)}
bad_header_params = {"x-v": str(-1)}

def get_term_deposits(products):
    return list(filter(lambda product: 'Term Deposit' in product['name'], products))


class TestProductApi(unittest.TestCase):
    def test_get_products(self):
        r = req.get(url, headers=header_params)

        self.assertEqual(r.status_code, 200)

        products = json.loads(r.text)['data']['products']
        term_deposits = get_term_deposits(products)

        print('\nterm deposit products\n')
        pp.pprint(term_deposits)

    def test_get_product_detail(self):
        r = req.get(f'{url}/{business_loan_id}', headers=header_params)

        self.assertEqual(r.status_code, 200)

        data = json.loads(r.text)['data']
        eligibility = data['eligibility']
        
        print('\neligibility of business loan\n')
        pp.pprint(eligibility)

    def test_get_products_invalid_headers(self):
        r = req.get(f'{url}/{business_loan_id}', headers=bad_header_params)

        self.assertEqual(r.status_code, 400)
    
    def test_get_product_detail_missing_headers(self):
        r = req.get(url, headers={})

        self.assertEqual(r.status_code, 400)

if __name__ == '__main__':
    unittest.main()