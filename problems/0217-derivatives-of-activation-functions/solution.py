import numpy as np

def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	def sigmoid(x):
		return 1/(1 + np.exp(-x))

	def tanh(x):
		return np.tanh(x)

	def relu_der(x):
		if x>0:
			return 1.0
		else:
			return 0.0


	d = {}
	d["sigmoid"] = sigmoid(x)*(1 - sigmoid(x))
	d["tanh"] = 1 - np.tanh(x)**2
	d["relu"] = relu_der(x)
	return d