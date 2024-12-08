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
git clone https://github.com/yourusername/adaptive-power-neurons.git
cd adaptive-power-neurons
pip install adaptive-power-neurons

# Example Usage for Adaptive Power Neurons

from adaptive_power_neurons import AdaptivePowerNeuron, AdaptivePowerNeurons, Optimizer
import numpy as np

# Sample data (X: input features, y: target labels)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([0, 0, 1, 1, 1])

# Create an adaptive power neuron
neuron = AdaptivePowerNeuron(input_dim=1, max_power=3, learning_rate=0.001, indexing_rate=0.01)

# Create a neural network with 2 layers (each using the adaptive power neuron)
model = AdaptivePowerNeurons()
model.add_layer(num_perceptrons=1, input_dim=1, max_power=3, learning_rate=0.001, indexing_rate=0.01)
model.add_layer(num_perceptrons=1, input_dim=1, max_power=3, learning_rate=0.001, indexing_rate=0.01)

# Create an optimizer for the model
optimizer = Optimizer(learning_rate=0.001, max_power=3, indexing_rate=0.01)

# Set the optimizer for the model
model.set_optimizer(optimizer)

# Train the model for 20 epochs
model.fit(X, y, epochs=20)

# Test prediction
test_input = np.array([[3]])  # New test input
prediction = model.predict(test_input)

print(f"Prediction for input {test_input}: {prediction}")



