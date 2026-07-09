import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
    """
    Compute the Jacobian matrix using numerical differentiation.

    Args:
        f: Function that takes a list and returns a list
        x: Point at which to evaluate the Jacobian
        h: Step size for finite differences

    Returns:
        Jacobian matrix as list of lists
    """
    f0 = f(x)
    m = len(f0)      # Number of outputs
    n = len(x)       # Number of inputs

    J = [[0.0 for _ in range(n)] for _ in range(m)]

    for j in range(n):
        # Create a perturbed copy of x
        x_new = x.copy()
        x_new[j] += h

        # Evaluate function at perturbed point
        f_new = f(x_new)

        # Compute the j-th column of the Jacobian
        for i in range(m):
            J[i][j] = (f_new[i] - f0[i]) / h

    return J

