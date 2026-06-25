import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    #f = np.array(f_coeffs)
    #g = np.array(g_coeffs)
    N = len(f_coeffs)
    M = len(g_coeffs)

    pol_prod = []

    for k in range(N + M - 1):
        coeff = 0
        for i in range(max(0, k-M+1), min(N, k+1)):
            coeff += f_coeffs[i] * g_coeffs[k-i]
        pol_prod.append(coeff)
    
    final_der = [round(j * pol_prod[j],4) for j in range(1, len(pol_prod))]

    if len(final_der) == 0:
        return [0.0]
    else:
        return final_der

