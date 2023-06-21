import tensorflow as tf

def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    return model

def initialize_model(X=None, y=None):
    global model
    model = create_model()
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    _, accuracy = model.evaluate(X, y)  # Remplacez X et y par vos données d'entraînement et d'étiquettes
    print("Précision du modèle :", accuracy)
    
    return accuracy

