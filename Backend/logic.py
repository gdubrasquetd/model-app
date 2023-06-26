import tensorflow as tf
import numpy as np

def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation='relu', input_shape=(1,)),
        tf.keras.layers.Dense(1)
    ])
    return model


def train_model(X, y, epochs = 100):
    model = create_model()
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(X, y, epochs=epochs, verbose=1)

    test_input = np.array([[150.0]])
    predicted_price = model.predict(test_input)
    print(f'Prix prédit : {predicted_price[0][0]:.2f}')
    return predicted_price

if __name__ == '__main__':
    superficie = np.random.rand(100, 1) * 200
    price = 50 + 4 * superficie + np.random.randn(100, 1) * 10

    train_model(25, 650)