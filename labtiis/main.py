# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Load the dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

# Define the model architecture
model = Sequential()
model.add(Dense(4, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=1000, batch_size=4)

# Evaluate the model
loss, accuracy = model.evaluate(X, y)
print("Accuracy: ", accuracy)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
