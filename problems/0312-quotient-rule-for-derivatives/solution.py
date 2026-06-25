import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    g = np.array(g_coeffs[::-1])
    h = np.array(h_coeffs[::-1])

    hofx = sum(h[j]*x**j for j in range(len(h)))
    gofx = sum(g[j]*x**j for j in range(len(g)))

    gprime = np.array([i*g[i] for i in range(1,len(g))])
    hprime = np.array([k*h[k] for k in range(1,len(h))])

    hprimeofx = sum(hprime[j]*x**j for j in range(len(hprime)))
    gprimeofx = sum(gprime[j]*x**j for j in range(len(gprime)))

    fprimeofx = (hofx*gprimeofx - gofx*hprimeofx)/hofx**2
    final = float(fprimeofx)

    return(final)    