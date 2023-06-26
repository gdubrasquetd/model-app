import json
import sys, os
import unittest
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from app import app



class CRUDTests(unittest.TestCase):
            
    model_dict = {
                'id' : '1',
                'name': 'Test Model',
                'nb_iterations': 100,
                'seed': 123,
                'type': 'local',
                'data': [25, 56],
                'last_prediction': 46
                }

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        # Clear Database if needed 
        pass

    def test1_add_model(self):
        print("test_add_model")
        response = self.app.post('/add', json=self.model_dict)
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data['message'], 'Model added successfully')
        print(response_data)        
        self.assertEqual(response_data['model']['name'], self.model_dict['name'])

    def test2_get_model_by_id(self):
        print("test_get_model_by_id")
        response = self.app.get('/1')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        print(response_data)
        self.assertIn('model', response_data)

    def test3_get_model_by_invalid_id(self):
        print("test_get_model_by_invalid_id")
        response = self.app.get('/100')
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data['error'], 'Model not found')

    def test4_update_model(self):
        print("test_update_model")
        data = {
            'name': 'Updated Model',
            'nb_iterations': 200,
            'seed': 456,
            'type': 'mixte',
            'data': [25, 56],
            'last_prediction': 46
        }
        response = self.app.put('/update/1', json=data)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data['message'], 'Model updated successfully')
        print(response_data['model']['name'], data['name'])
        self.assertEqual(response_data['model']['name'], data['name'])

    def test5_update_model_with_invalid_id(self):
        print("test_update_model_with_invalid_id")
        data = {
            'name': 'Updated Model',
            'nb_iterations': 200,
            'seed': 456,
            'type': 'mixte',
            'data': [25, 56],
            'last_prediction': 46
        }
        response = self.app.put('/update/100', json=data)
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data['error'], 'Model not found')
        
    def test6_delete_model_by_id(self):
        response = self.app.delete('/1')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data['message'], 'Model deleted successfully')

    def test7_delete_model_by_invalid_id(self):
        response = self.app.delete('/100')
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data['error'], 'Model not found')
    


if __name__ == '__main__':
    unittest.main()
