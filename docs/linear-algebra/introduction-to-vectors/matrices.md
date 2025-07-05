# Matrices

## Properties

Properties of matrix operations:

- **Addition:** If $A$ and $B$ are matrices of the same size $m×n$, then their sum $A+B$ is also an $m×n$ matrix.
- **Multiplication by scalars:** If $A$ is an $m×n$ matrix and $c$ is a scalar, then $cA$ is an $m×n$ matrix.
- **Matrix multiplication:** If $A$ is an $m×n$ matrix and $B$ is an $n×p$ matrix, then the product $AB$ is an $m×p$ matrix.
- **Vectors:** A vector of length $n$ can be treated as an $n×1$ matrix. Vector addition, scalar multiplication, and matrix-vector multiplication follow the same rules as matrix operations.
- **Transpose:** For an $m×n$ matrix $A$, its transpose $A^T$ is an $n×m$ matrix.
- **Identity matrix:** $I_n$ is the $n×n$ identity matrix, with 1's on the diagonal and 0's elsewhere.
- **Zero matrix:** Denoted by 0, it is a matrix of all zeroes with appropriate size.
- **Inverse:** For a square matrix $A$, its inverse $A^{-1}$ is a matrix of the same size such that $AA^{-1} = A^{-1}A = I_n$. Not all matrices have inverses; those that do are called invertible.

Key properties (assuming scalars $r, s$ and appropriately sized matrices $A, B, C$):

**Properties of matrix addition:**

$$
\begin{aligned}
& A + B = B + A && \text{(Commutativity)} \\
& (A + B) + C = A + (B + C) && \text{(Associativity)} \\
& A + 0 = A, && \text{(Additive identity)} \\
& r(A + B) = rA + rB && \text{(Distributivity of scalar over addition)} \\
& (r + s)A = rA + sA && \text{(Distributivity of addition over scalar)} \\
& r(sA) = (rs)A && \text{(Associativity of scalar multiplication)} \\
\end{aligned}
$$

**Properties of matrix multiplication:**

$$
\begin{aligned}
& A(BC) = (AB)C && \text{(Associativity)} \\
& A(B + C) = AB + AC && \text{(Left distributivity)} \\
& (B + C)A = BA + CA && \text{(Right distributivity)} \\
& r(AB) = (rA)B = A(rB) && \text{(Scalar multiplication compatibility)} \\
& I_m A = A = A I_n && \text{(Identity matrix)} \\
\end{aligned}
$$

**Properties of the transpose operation:**

$$
\begin{aligned}
& (A^T)^T = A, && \text{(Double transpose)} \\
& (A + B)^T = A^T + B^T && \text{(Transpose of sum)} \\
& (rA)^T = r A^T && \text{(Transpose of scalar multiple)} \\
& (AB)^T = B^T A^T && \text{(Transpose of product reverses order)} \\
& (I_n)^T = I_n && \text{(Transpose of identity)} \\
\end{aligned}
$$

**Properties of the inverse operation (for invertible matrices):**

$$
\begin{aligned}
& A A^{-1} = A^{-1} A = I_n, && \text{(Inverse definition)} \\
& (rA)^{-1} = r^{-1} A^{-1} \quad r \neq 0, && \text{(Inverse of scalar multiple)} \\
& (AB)^{-1} = B^{-1} A^{-1} && \text{(Inverse of product reverses order)} \\
& (I_n)^{-1} = I_n && \text{(Inverse of identity)} \\
& (A^T)^{-1} = (A^{-1})^T && \text{(Transpose and inverse commute)} \\
& (A^{-1})^{-1} = A && \text{(Inverse of inverse)} \\
\end{aligned}
$$

**Additional Properties**

$$
\begin{aligned}
& A = A^T \quad \text{(Symmetric matrix)} \\
& Q^T Q = I_n \quad \text{(Orthogonal matrix)} \\
& \mathrm{tr}(A + B) = \mathrm{tr}(A) + \mathrm{tr}(B) \quad \text{(Trace linearity)} \\
& \mathrm{tr}(AB) = \mathrm{tr}(BA) \quad \text{(Trace cyclic property)} \\
& \det(AB) = \det(A) \det(B) \quad \text{(Determinant multiplicative)} \\
& \det(A^T) = \det(A) \quad \text{(Determinant transpose)} \\
& \det(A^{-1}) = \frac{1}{\det(A)} \quad \text{(Determinant inverse)} \\
& \operatorname{rank}(A) \leq \min(m, n) \quad \text{for } A \in \mathbb{R}^{m \times n} \\
& \operatorname{rank}(AB) \leq \min(\operatorname{rank}(A), \operatorname{rank}(B)) \\
& \text{If } A \text{ is invertible and } AB = AC \text{ then } B = C \quad \text{(Cancellation law)} \\
& \text{In general, } AB \neq BA \quad \text{(Non-commutativity)} \\
& (A + B)(A - B) = A^2 - B^2 \quad \text{only if } AB = BA \quad \text{(Difference of squares)} \\
& \text{If } A \text{ is symmetric and positive definite, } \exists \text{ Cholesky factorization } A = LL^T \\
& \text{Eigenvalues of } A^T = \text{Eigenvalues of } A \\
& \text{Eigenvalues of } A^{-1} = \frac{1}{\text{Eigenvalues of } A}
\end{aligned}
$$

Differences from regular number operations:

- Matrix multiplication is generally **not commutative**; in general, $AB \neq BA$.
- The transpose of a product reverses order: $(AB)^T = B^T A^T$.
- The inverse of a product reverses order: $(AB)^{-1} = B^{-1} A^{-1}$.
- To conclude $B = C$ from $AB = AC$, matrix $A$ must be invertible.
- If $AB = 0$, it does not imply $A = 0$ or $B = 0$. For example,

$$
A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \quad
B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}, \quad
AB = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}
$$

<aside>
💡

A square matrix is invertible if and only if its determinant is non-zero.

</aside>

## Types

Matrices come in many forms depending on their size, elements, and special properties. Below is a detailed overview of the most common types of matrices used in linear algebra.

### 1. Square Matrix

A matrix with the same number of rows and columns.

$$
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{bmatrix}
$$

Example: $\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}$

### 2. Rectangular Matrix

A matrix where the number of rows is not equal to the number of columns.

$$
B = \begin{bmatrix}
b_{11} & b_{12} & \cdots & b_{1p} \\
b_{21} & b_{22} & \cdots & b_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
b_{m1} & b_{m2} & \cdots & b_{mp}
\end{bmatrix}
$$

with $m\neq n$ .

### 3. Row Matrix

A matrix with only one row $1 \times n$.

$$
R = \begin{bmatrix} r_1 & r_2 & \cdots & r_n \end{bmatrix}
$$

### 4. Column Matrix

A matrix with only one column $m \times 1$.

$$
C = \begin{bmatrix} c_1 \\ c_2 \\ \vdots \\ c_m \end{bmatrix}
$$

### 5. Zero Matrix (Null Matrix)

A matrix in which all elements are zero.

$$
O = \begin{bmatrix}
0 & 0 & \cdots & 0 \\
0 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 0
\end{bmatrix} 
$$

### 6. Identity Matrix

A square matrix with ones on the main diagonal and zeros elsewhere.

$$
I_n = \begin{bmatrix}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 1
\end{bmatrix}
$$

### 7. Diagonal Matrix

A square matrix where all off-diagonal elements are zero.

$$
D = \begin{bmatrix}
d_1 & 0 & \cdots & 0 \\
0 & d_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & d_n
\end{bmatrix}
$$

### 8. Scalar Matrix

A diagonal matrix where all diagonal entries are equal.

$$
S = \lambda I_n = \begin{bmatrix}
\lambda & 0 & \cdots & 0 \\
0 & \lambda & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda
\end{bmatrix}
$$

### 9. Symmetric Matrix

A square matrix that is equal to its transpose: $A = A^T$

### 10. Skew-Symmetric (Antisymmetric) Matrix

A square matrix whose transpose equals its negative: $A^T = -A$

### 11. Orthogonal Matrix

A square matrix $Q$ with real entries whose transpose is its inverse: 

$$
Q^T = Q^{-1}
\\\text{OR}\\
Q^T Q = Q Q^T = I_n
$$

Example: A  rotation matrix $Q = \begin{bmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{bmatrix}$

### 12. Singular Matrix

A square matrix that does not have an inverse. Its determinant is zero: $\det(A) = 0$

### 13. Invertible (Nonsingular) Matrix

A square matrix $A$ that has an inverse: $A^{-1} = A^{-1} A = I_n$

### 14. Positive Definite Matrix

A symmetric matrix $A$ such that for all **nonzero** vectors $x$, $x^T A x > 0$

Its eigenvalues are strictly positive. If the quadratic form is strictly greater than zero for all non-zero vectors x, then the matrix is called positive definite.

### 15. Positive Semi-Definite (PSD) Matrix

A symmetric matrix $A$ is **positive semi-definite** if for all vectors $x$, $x^T A x \geq 0$

Its eigenvalues are non-negative. This means the quadratic form is never negative, but it can be zero for some nonzero $x$.

### 16. Hermitian Matrix

A square matrix $A$ with complex entries is **Hermitian** if it equals its own conjugate transpose: $A = A^H = \overline{A}^T$

This means $A_{ij} = \overline{A_{ji}}$ for all $i,j$.

**Example:** $A = \begin{bmatrix}
2 & 2 + i \\
2 - i & 3
\end{bmatrix}$Here, $A = A^H$.

### 17. Skew-Hermitian Matrix

A square matrix A is **skew-Hermitian** if it satisfies: $A = -A^H = -\overline{A}^T$(i.e. if and only if it is equal to the negative of its conjugate matrix).

This means $A_{ij} = -\overline{A_{ji}}$.

**Example:** $A = \begin{bmatrix}
0 & 2 + i \\
-2 + i & 0
\end{bmatrix}$Here, $A = -A^H$.

---

### 18. Idempotent Matrix

A square matrix A is **idempotent** if: $A^2 = A$ or $A^n = A$, for every $n ≥ 2$

This means multiplying the matrix (not element-wise) by itself returns the same matrix.

### 19. Nilpotent Matrix

A square matrix $A$ of order $n$ is **nilpotent** if there exists an integer $k \leq n$ such that: $A^k = 0$where $0$ is the zero matrix.

### 20. Involutory Matrix

A square matrix $A$ is **involutory** if it is its own inverse: $A^{-1} = A$

For example, an identity matrix is involutory as it is equal to its inverse.

## Resources

1. [https://math.mit.edu/~dyatlov/54summer10/matalg.pdf](https://math.mit.edu/~dyatlov/54summer10/matalg.pdf)