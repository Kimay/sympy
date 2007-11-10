"""
Convergence acceleration / extrapolation methods for series and
sequences.

References:
Carl M. Bender & Steven A. Orszag, "Advanced Mathematical Methods for
Scientists and Engineers: Asymptotic Methods and Perturbation Theory",
Springer 1999. (Shanks transformation: pp. 368-375, Richardson
extrapolation: pp. 375-377.)
"""

from sympy import Symbol, factorial, pi, Integer, E, Sum2


def richardson(A, k, n, N):
    """
    Calculate an approximation for lim k->oo A(k) using Richardson
    extrapolation with the terms A(n), A(n+1), ..., A(n+N+1).
    Choosing N ~= 2*n often gives good results.

    A simple example is to calculate exp(1) using the limit definition.
    This limit converges slowly; n = 100 only produces two accurate
    digits:

        >>> n = Symbol('n')
        >>> e = (1 + 1/n)**n
        >>> e.subs(n, 100).evalf()
        2.704813829421526093267194711

    Richardson extrapolation with 11 appropriately chosen terms gives
    a value that is accurate to the indicated precision:

        >>> richardson(e, n, 10, 20).evalf()
        2.718281828459045235360287471
        >>> E.evalf()
        2.718281828459045235360287471

    Another useful application is to speed up convergence of series.
    Computing 100 terms of the zeta(2) series 1/k**2 yields only
    two accurate digits:

        >>> k = Symbol('k'); n = Symbol('n')
        >>> A = Sum2(k**-2, (k, 1, n))
        >>> A.subs(n, 100).evalf()
        1.634983900184892865077169498

    Richardson extrapolation performs much better:

        >>> richardson(A, n, 10, 20).evalf()
        1.644934066848226436472414853
        >>> ((pi**2)/6).evalf()     # Exact value
        1.644934066848226436472415167

    """
    s = Integer(0)
    for j in range(0, N+1):
        s += A.subs(k, Integer(n+j)) * (n+j)**N * (-1)**(j+N) / \
            (factorial(j) * factorial(N-j))
    return s


def shanks(A, k, n, m=1):
    """
    Calculate an approximation for lim k->oo A(k) using the n-term Shanks
    transformation S(A)(n). With m > 1, calculate the m-fold recursive
    Shanks transformation S(S(...S(A)...))(n).

    The Shanks transformation is useful for summing Taylor series that
    converge slowly near a pole or singularity, e.g. for log(2):

        >>> n = Symbol('n')
        >>> k = Symbol('k')
        >>> A = Sum2(Integer(-1)**(k+1) / k, (k, 1, n))
        >>> A.subs(n, 100).evalf()
        0.6881721793101952032446458827
        >>> shanks(A, n, 25).evalf()
        0.6931396564055737564958186845
        >>> shanks(A, n, 25, 5).evalf()
        0.6931471805599451716132607039

    The correct value is 0.6931471805599453094172321215.
    """
    table = [A.subs(k, Integer(j)) for j in range(n+m+2)]
    table2 = table[:]

    for i in range(1, m+1):
        for j in range(i, n+m+1):
            x, y, z = table[j-1], table[j], table[j+1]
            table2[j] = (z*x - y**2) / (z + x - 2*y)
        table = table2[:]
    return table[n]

