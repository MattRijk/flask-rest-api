import os
import unittest

from main.app import app

class StoreTestCase(unittest.TestCase):

    def setUp(self):
        """Set up a blank temp database before each test"""
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index_page_text(self):
        client = app.test_client(self)
        response = client.get('/', content_type='html/text')
        self.assertIn(b'Hello, World', response.data)

    def test_store_request(self):
        client = app.test_client(self)
        response = client.get('/store', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_store_request_item_has_data(self):
        client = app.test_client(self)
        response = client.get('/store/product-1', content_type='html/text')
        self.assertIn(b'product-1', response.data)
        self.assertEqual(response.status_code, 200)

    def test_store_has_data(self):
        client = app.test_client(self)
        response = client.get('/store/product-1/item', content_type='html/text')
        self.assertIn(b'product-1', response.data)
        self.assertEqual(response.status_code, 200)

    def test_store_create_item(self):
        client = app.test_client(self)
        response = client.post('/store/product-1/item', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_store_endpoint(self):
        client = app.test_client(self)
        response = client.post('/store/product-1/item', content_type='html/text')
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
