import json
import uuid
from uuid import UUID

class Model:
    def __init__(self, name, nb_iterations, seed, type, data, last_prediction, id=None):
        
        self.id = id if id is not None else uuid.uuid4()
        self.name = name
        self.nb_iterations = nb_iterations
        self.seed = seed
        self.type = type
        self.data = data
        self.last_prediction = last_prediction
        
        
    
    def to_dict(self):
        # Convert UUID to string representation
        id_str = str(self.id) if self.id else None

        return{
            'id': id_str,
            'name': self.name,
            'nb_iterations': self.nb_iterations,
            'seed': self.seed,
            'type': self.type,
            'data': self.data,
            'last_prediction': self.last_prediction
        }
    
    @classmethod
    def from_dict(cls, model_dict):
        # Convert the ID from string to UUID if present
        id_str = model_dict.get('id')
        id = UUID(id_str) if id_str else None

        # Create a new instance of Model using the dictionary values
        model = cls(
            id=id,
            name=model_dict.get('name'),
            nb_iterations=model_dict.get('nb_iterations'),
            seed=model_dict.get('seed'),
            type=model_dict.get('type'),
            data=model_dict.get('data'),
            last_prediction=model_dict.get('last_prediction')
        )

        return model