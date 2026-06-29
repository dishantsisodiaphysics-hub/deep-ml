import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	mag_sq = 0
	
	for j in range(len(gradient)):
		mag_sq = mag_sq + gradient[j]**2

	mag = np.sqrt(mag_sq)

	direction = np.array(gradient)

	if mag == 0:
		direction = np.zeros((len(gradient)))
	else:
		direction = direction/mag

	des_direction = direction*-1

	dir_list = direction.tolist()
	des_list = des_direction.tolist()

	sol = {
    "magnitude": mag,
    "direction": dir_list,
    "descent_direction": des_list
	}
	
	return sol