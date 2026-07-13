from typing import Callable

def compute_hessian(f: Callable[[list[float]], float], point: list[float], h: float = 1e-5) -> list[list[float]]:
	
	"""
	Compute the Hessian matrix of function f at the given point using finite differences.
	
	Args:
		f: A scalar function that takes a list of floats and returns a float
		point: The point at which to compute the Hessian (list of coordinates)
		h: Step size for finite differences (default: 1e-5)
		
	Returns:
		The Hessian matrix as a list of lists (n x n where n = len(point))
	"""
	f0 = f(point)
	n = len(point)

	hessian_matrix = [[0.0 for _ in range(n)] for _ in range(n)]

	for j in range(n):
		# Point perturbed in the j-th direction
		point_j = point.copy()
		point_j[j] += h
		f_j = f(point_j)

		# First derivative with respect to x_j
		g0 = (f_j - f0) / h

		for i in range(n):
			# Point perturbed in both i-th and j-th directions
			point_ij = point_j.copy()
			point_ij[i] += h
			f_ij = f(point_ij)

			# Point perturbed only in the i-th direction
			point_i = point.copy()
			point_i[i] += h
			f_i = f(point_i)

			# First derivative with respect to x_j at point_i
			g_new = (f_ij - f_i) / h

			# Second derivative
			hessian_matrix[i][j] = (g_new - g0) / h

	return hessian_matrix
