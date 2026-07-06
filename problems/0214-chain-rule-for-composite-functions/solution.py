import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# Your code here
	def derivative(func, y):
		if func == 'square':
			return 2*y
		elif func == 'sin':
			return np.cos(y)
		elif func == 'exp':
			return np.exp(y)
		elif func == 'log':
			return 1/y

	def func_def(func, y):
		if func == 'square':
			return y**2
		elif func == 'sin':
			return np.sin(y)
		elif func == 'exp':
			return np.exp(y)
		elif func == 'log':
			return np.log(y)

	val_func = func_def(functions[-1], x)
	sol = derivative(functions[-1], x)

	for j in range(-2, -len(functions)-1, -1):
		
		sol = sol* derivative(functions[j], val_func)
		val_func = func_def(functions[j], val_func)

	return sol