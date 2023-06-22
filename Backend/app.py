from flask import Flask, jsonify, request
from tinydb import TinyDB, Query
from flask_cors import CORS
from type.model import Model
#from logic import initialize_model
import os
import uuid

app = Flask(__name__)
CORS(app)
current_dir = os.path.dirname(__file__)
database_path = os.path.join(current_dir, '../Database/database.json')
db = TinyDB(database_path)
modelDB = db.table('modèles')

model_test = Model(name='Modèle 1', nb_iterations=100, seed=123, type='local')

#Initialise the model at the start of the server
@app.before_request
def compute_model():
    print("compute")
    #initialize_model()


@app.route('/')
def homepage():
    return jsonify({'message': 'Page d\'accueil'})


@app.route('/add', methods=['POST'])
def add_model():
    data = request.get_json()
    
    model_id = data.get('id') if data.get('id') else None
    model_name = data.get('name')
    nb_iterations = data.get('nb_iterations')
    seed = data.get('seed')
    model_type = data.get('type')
    new_model = Model(id = model_id, name = model_name,nb_iterations = nb_iterations,seed = seed,type = model_type)
    model_dict = new_model.to_dict()

    modelDB.insert({'model': model_dict})

    return jsonify({'message': 'Model added successfully', 'model': model_dict}), 201


@app.route('/<id>', methods=['GET'])
def get_model_by_id(id):

    Model = Query()
    model = modelDB.get(Model.model.id == id)
    if model:
        return jsonify({'model': model}), 200
    else:
        return jsonify({'error': 'Model not found'}), 404
    

@app.route('/<id>', methods=['DELETE'])
def delete_model_by_id(id):
    Model = Query()
    model = modelDB.get(Model.model.id == id)
    if model:
        modelDB.remove(Model.model.id == id)
        return jsonify({'message': 'Model deleted successfully', 'model': model}), 200
    else:
        return jsonify({'error': 'Model not found'}), 404
    

@app.route('/update/<id>', methods=['PUT'])
def update_model(id):
    data = request.get_json()

    Model = Query()
    existing_model = modelDB.get(Model.model.id == id)
    if existing_model:
        model_params =  existing_model["model"]
        model_name = data.get('name') if data.get('name') != None else model_params["name"]
        nb_iterations = data.get('nb_iterations') if data.get('nb_iterations') != None else model_params["nb_iterations"]
        seed = data.get('seed') if data.get('seed') != None else model_params["seed"]
        model_type = data.get('type') if data.get('type') != None else model_params["type"]
        new_model = {"model":
                    {
                    'id': id,
                    'name': model_name,
                    'nb_iterations': nb_iterations,
                    'seed': seed,
                    'type': model_type
                    }}

        modelDB.update(new_model, Model.model.id == id)
        updated_model = modelDB.get(Model.model.id == id)
        print(updated_model)
    
        return jsonify({'message': 'Model updated successfully', 'model': updated_model['model']}), 200
    else:
        return jsonify({'error': 'Model not found'}), 404





@app.route('/test', methods=['POST'])
def test_model():
    
    my_model = Model(name='Modèle 1', nb_iterations=100, seed=123, type='local')
    
    print("Test 1", my_model)
    
    dict_data = my_model.to_dict()
    
    print("Test 2", dict_data)
    
    databack = Model.from_dict(dict_data)
 
    print("Test 3", databack)
    
    dict_data = my_model.to_dict()
    
    print("Test 4", dict_data)
 
    return jsonify({'message': 'Test Ended'})

@app.route('/list')
def list_models():
    models = modelDB.all()
    return jsonify(models)

@app.route('/train')
def entrainer_modele():
    return jsonify({'message': 'Entraînement terminé'})

@app.route('/inference', methods=['POST'])
def effectuer_inference():
    return jsonify({'message': 'Exemple non trouvé'})

if __name__ == '__main__':
    app.run(debug=True)
