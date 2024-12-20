# **Adaptive Power Neurons**

**Adaptive Power Neurons** is a Python library for building machine learning models using adaptive power perceptrons. These perceptrons dynamically adjust their polynomial feature power and input indices, enabling the model to learn complex patterns effectively. 

The library is designed for both regression and classification tasks and supports multi-layer neural networks with adaptive neurons.

---

## **Features**

- **Dynamic Adaptation**: Perceptrons adjust their polynomial degree (power) and input index bias during training.
- **Polynomial Feature Expansion**: Supports automatic polynomial feature generation up to a specified degree.
- **Index Bias Adjustment**: Incorporates adjustable input bias for feature shifts.
- **Multi-Layer Support**: Create flexible, multi-layer neural networks.
- **Customizable Optimizer**: Fine-tune hyperparameters like learning rate, polynomial power, and indexing rate dynamically.

---

## **Mathematical Overview**

### 1. **Polynomial Feature Expansion**
Each perceptron transforms the input into a polynomial feature vector:
\[
\phi(x) = [x^1, x^2, \dots, x^p]
\]
Where \( p \) is the maximum power specified for the perceptron.

### 2. **Weighted Output**
The perceptron computes a weighted sum of the polynomial features:
\[
z = w_1 \phi(x_1) + w_2 \phi(x_2) + \dots + w_n \phi(x_n) + b
\]

### 3. **Loss Function**
The library uses **Mean Squared Error (MSE)** for regression:
\[
\text{MSE} = \frac{1}{N} \sum_{i=1}^{N} \left( y_i - \hat{y}_i \right)^2
\]

For classification, a step function is used:
\[
\hat{y} = 
\begin{cases} 
1 & \text{if } z \geq 0 \\
0 & \text{if } z < 0
\end{cases}
\]

### 4. **Index Bias Adjustment**
An adjustable index bias \( \delta \) shifts the input features:
\[
x_{\text{adjusted}} = x + \delta
\]

### 5. **Weight Updates**
Weights, biases, and index bias are updated using gradient descent:
\[
w_i = w_i - \eta \cdot \frac{\partial \text{MSE}}{\partial w_i}, \quad 
b = b - \eta \cdot \frac{\partial \text{MSE}}{\partial b}, \quad
\delta = \delta - \eta \cdot \frac{\partial \text{MSE}}{\partial \delta}
\]

---

## **Installation**

To install the library, clone the repository and install it locally:
```bash
pip install adaptive-power-neurons

# Example Usage for Adaptive Power Neurons

import numpy as np
from adaptive_power_neurons import AdaptivePowerModel, SGD, DenseLayer

# Hyperparameters
input_dim = 3  # Number of input features
output_dim = 2  # Number of output neurons
max_power = 2  # Max power for the neurons
learning_rate = 0.001  # Learning rate for the optimizer
indexing_rate = 0.01  # Indexing rate

# Create SGD optimizer
optimizer = SGD(learning_rate)

# Create AdaptivePowerModel and add layers
model = AdaptivePowerModel()
model.add(DenseLayer(input_dim, 1, max_power, optimizer, indexing_rate, activation="relu"))
model.add(DenseLayer(1, output_dim, max_power, optimizer, indexing_rate, activation="sigmoid"))

# Dummy dataset
x = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])  # Input features
y = np.array([[0.5, 1.0], [1.0, 0.0], [0.0, 1.0]])  # Target labels

# Train the model
model.train(x, y, epochs=100, batch_size=1)

model.predict_(np.array([[1, 2, 3]]))

