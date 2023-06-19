from flask import Flask, jsonify, request
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('database.json')
examples_table = db.table('examples')

@app.route('/')
def homepage():
    return jsonify({'message': 'Page d\'accueil'})

@app.route('/ajouter', methods=['POST'])
def ajouter_exemple():
    data = request.get_json()
    x = data['x']
    y = data['y']
    examples_table.insert({'x': x, 'y': y})
    return jsonify({'message': 'Exemple ajouté avec succès'})

@app.route('/lister')
def lister_exemples():
    exemples = examples_table.all()
    return jsonify(exemples)

@app.route('/entrainer')
def entrainer_modele():
    # Logique d'entraînement du modèle
    return jsonify({'message': 'Entraînement terminé'})

@app.route('/inference', methods=['POST'])
def effectuer_inference():
    data = request.get_json()
    x = data['x']
    exemple = examples_table.search(Query().x == x)
    if exemple:
        y = exemple[0]['y']
        return jsonify({'prediction': y})
    else:
        return jsonify({'message': 'Exemple non trouvé'})

if __name__ == '__main__':
    app.run(debug=True)
