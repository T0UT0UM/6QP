import tensorflow as tf

def create_q_network(input_shape, num_actions):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=input_shape)) # Input layer
    model.add(tf.keras.layers.Dense(64, activation='relu'))  # Hidden layer
    model.add(tf.keras.layers.Dense(num_actions, activation='linear'))  # Output layer

    # Compile the model
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                  loss='mean_squared_error')

    # Print model summary
    model.summary()

    return model

# Example usage:
input_shape = (30,)  # 30 inputs for the game state
num_actions = 2  # Replace with the actual number of possible actions
q_network = create_q_network(input_shape, num_actions)
