from flask import Flask, jsonify, request
from tinydb import TinyDB, Query
from flask_cors import CORS
from type.model import Model
import json
import uuid

app = Flask(__name__)
CORS(app)
db = TinyDB('../Database/database.json')
modelDB = db.table('modèles')

model_test = Model(name='Modèle 1', nb_iterations=100, seed=123, type='local')


@app.route('/')
def homepage():
    return jsonify({'message': 'Page d\'accueil'})

@app.route('/add', methods=['POST'])
def add_model():
    data = request.get_json()
    model = data['model']
    modelDB.insert({'model': model})
    
    return jsonify({'message': 'Model added successfully'})

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
 
    return jsonify({'message': 'Model added successfully'})

@app.route('/list')
def list_models():
    models = modelDB.all()
    return jsonify(models)

@app.route('/entrainer')
def entrainer_modele():
    # Logique d'entraînement du modèle
    return jsonify({'message': 'Entraînement terminé'})

@app.route('/inference', methods=['POST'])
def effectuer_inference():
    return jsonify({'message': 'Exemple non trouvé'})

if __name__ == '__main__':
    app.run(debug=True)
