from flask import Flask, jsonify, request
from tinydb import TinyDB, Query
from flask_cors import CORS
from type.model import Model
from logic import create_model, train_model, predict_model
import numpy as np
import os
import uuid

app = Flask(__name__)
CORS(app)
current_dir = os.path.dirname(__file__)
database_path = os.path.join(current_dir, '../Database/database.json')
db = TinyDB(database_path)
modelDB = db.table('modèles')
initialized_model = None


model_test = Model(name='Modèle 1', nb_iterations=100, seed=123, type='local', data=[0.0], input=5, prediction=0)


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
    model_data = data.get('data')
    prediction = data.get('prediction')
    model_input = data.get('input')
    new_model = Model(id = model_id, name = model_name,nb_iterations = nb_iterations,seed = seed,type = model_type, data=model_data, input=model_input, prediction=prediction)
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
        model_data = data.get('data') if data.get('data') != None else model_params["data"]
        model_input = data.get('input') if data.get('input') != None else model_params["input"]
        prediction = data.get('prediction') if data.get('prediction') != None else model_params["prediction"]
        new_model = {"model":
                    {
                    'id': id,
                    'name': model_name,
                    'nb_iterations': nb_iterations,
                    'seed': seed,
                    'type': model_type,
                    'data': model_data,
                    'input': model_input,
                    'prediction': prediction
                    }}

        modelDB.update(new_model, Model.model.id == id)
        updated_model = modelDB.get(Model.model.id == id)
    
        return jsonify({'message': 'Model updated successfully', 'model': updated_model['model']}), 200
    else:
        return jsonify({'error': 'Model not found'}), 404


@app.route('/train/<id>', methods=['GET'])
def train(id):

    Model = Query()
    model = modelDB.get(Model.model.id == id)
    if model:
        model_params =  model["model"]
        data1 = np.array([[model_params.get('data')[0]]])
        data2 = np.array([[model_params.get('data')[1]]])
        app.config['trained_model'] = train_model(data1, data2, initialized_model)
        return jsonify({'message': 'Entraînement terminé.'}), 200
    else:
        return jsonify({'error': 'Model not found'}), 404
    
    
@app.route('/predict/<id>', methods=['GET'])
def predict(id):
    Model = Query()
    model = modelDB.get(Model.model.id == id)
    if model:
        model_params =  model["model"]
        print(app.config['trained_model'])
        predict = predict_model(app.config['trained_model'], 1500)
        model_params["last_prediction"] = predict.tolist()[0]
        new_model = {"model":
            {
            'id': model_params.get('id'),
            'name': model_params.get('name'),
            'nb_iterations': model_params.get('nb_iteration'),
            'seed': model_params.get('seed'),
            'type': model_params.get('type'),
            'data': model_params.get('data'),
            'input': model_params.get('input'),
            'prediction': predict.tolist()[0]

            }}
        modelDB.update(new_model, Model.model.id == id)
        return jsonify({'message': 'Entraînement terminé.', 'result': predict.tolist()[0]}), 200
    else:
        return jsonify({'error': 'Model not found'}), 404
    

@app.route('/list')
def list_models():
    models = modelDB.all()
    return jsonify(models)


@app.route('/inference', methods=['POST'])
def effectuer_inference():
    return jsonify({'message': 'Exemple non trouvé'})

if __name__ == '__main__':
    initialized_model = create_model()
    app.run(debug=True)
