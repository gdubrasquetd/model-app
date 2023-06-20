import json
import uuid
from uuid import UUID

class Model:
    def __init__(self, name, nb_iterations, seed, type, id=None):
        
        self.id = id if id is not None else uuid.uuid4()
        self.name = name
        self.nb_iterations = nb_iterations
        self.seed = seed
        self.type = type
        
        
    
    def to_dict(self):
        # Convert UUID to string representation
        id_str = str(self.id) if self.id else None

        return{
            'id': id_str,
            'name': self.name,
            'nb_iterations': self.nb_iterations,
            'seed': self.seed,
            'type': self.type
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
            type=model_dict.get('type')
        )

        return model