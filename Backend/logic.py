import tensorflow as tf
import numpy as np

def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation='relu', input_shape=(1,)),
        tf.keras.layers.Dense(1)
    ])
    return model


def train_model(X, y, model, epochs=100):
    X = np.array(X).reshape(-1, 1)  # Reshape X to have shape (None, 1)
    y = np.array(y).reshape(-1, 1)  # Reshape y to have shape (None, 1)
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(X, y, epochs=epochs, verbose=1)
    return model

def predict_model(model, X):
    predicted_price = model.predict(np.array([[X]]))
    print(f'Prix prédit : {predicted_price[0][0]:.2f}')
    return predicted_price
