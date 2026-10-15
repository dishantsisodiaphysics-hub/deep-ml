import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    if norm_type == "l1":
        # Entrywise L1 norm: sum of absolute values
        result = np.sum(np.abs(arr))
        return float(result.item())
        
    elif norm_type == "l2":
        # Entrywise L2 norm: square root of sum of squares
        result = np.sqrt(np.sum(arr**2))
        return float(result.item())
        
    elif norm_type == "linf":
        # Entrywise L-infinity norm: maximum absolute value
        result = np.max(np.abs(arr))
        return float(result.item())
        
    elif norm_type == "frobenius":
        # Check if the array is specifically 2-dimensional
        if len(arr.shape) != 2:
            raise ValueError(
                f"Frobenius norm requires a 2D matrix. Got a {len(arr.shape)}D array with shape {arr.shape}."
            )
        
        result = np.linalg.norm(arr, 'fro')
        return result.item()
        
    else:
        raise ValueError(
            f"Unsupported norm_type '{norm_type}'. Choose from 'l1', 'l2', 'linf', or 'frobenius'."
        )
