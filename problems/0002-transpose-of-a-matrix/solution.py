def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    row_a = len(a)
    col_a = len(a[0])
    transposed = [[] for _ in range(col_a)]
    for i in range(col_a):
        for j in range(row_a):
            transposed[i].append(a[j][i])

    return transposed
    pass