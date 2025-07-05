# Vectors and Linear Combinations

## What is a Linear Combination?

A linear combination of two vectors means multiplying them by numbers (called scalars) and adding the results. For example:

$$
3v+5w
$$

This is a typical linear combination of the vectors **v** and **w**.

If

$$
\mathbf{v} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}, \quad \mathbf{w} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

then

$$
3\mathbf{v} + 5\mathbf{w} = 3\begin{bmatrix} 1 \\ 2 \end{bmatrix} + 5\begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 6 \end{bmatrix} + \begin{bmatrix} 0 \\ 5 \end{bmatrix} = \begin{bmatrix} 3 \\ 11 \end{bmatrix}
$$

This means we move 3 units across (in x direction) and 11 units up (in y direction).

## Visualizing Vectors

A vector like $\begin{bmatrix} 2 \\ 3 \end{bmatrix}$goes 2 steps in x and 3 steps in y. It points to the location (2, 3) in the xy-plane.

All combinations like $\mathbf{v} + d\mathbf{w}$ (fill in every point in the plane) if **v** and **w** point in different directions. They cover the whole 2D space.

In 3D space, a combination like 

$$
c\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + d\begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}
$$

fills a plane in xyz space (but not the full space unless we add a third independent vector).

## Vector Operations

A vector has multiple components, like:

$$
\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix}
$$

We treat **v** as a single object, not two separate numbers.

### Vector Addition

Add corresponding parts:

$$
\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix}, \quad \mathbf{w} = \begin{bmatrix} w_1 \\ w_2 \end{bmatrix}
$$

Then:

$$
\mathbf{v} + \mathbf{w} = \begin{bmatrix} v_1 + w_1 \\ v_2 + w_2 \end{bmatrix}
$$

### Vector Subtraction

Same idea:

$$
\mathbf{v} - \mathbf{w} = \begin{bmatrix} v_1 - w_1 \\ v_2 - w_2 \end{bmatrix}
$$

### Scalar Multiplication

Multiply every part of a vector by a number:

$$
\mathbf{v} = 2\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 2v_1 \\ 2v_2 \end{bmatrix}, \quad -\mathbf{v} = \begin{bmatrix} -v_1 \\ -v_2 \end{bmatrix}
$$

A scalar is just a number like 2 or -1.

The sum of a vector and its negative gives the **zero vector**:

$$
\mathbf{v} + (-\mathbf{v}) = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

<aside>
💡
This is different from the number zero! It is a vector with all components equal to zero.

</aside>


## Linear Combinations in Practice

A linear combination means: $c\mathbf{v} + d\mathbf{w}$

You can also get:

- **Sum**: $1v+1w$
- **Difference**: $1v−1w$
- **Zero vector**: $0v+0w$
- Vector $cv$ in the direction of $v$: $cv+0wc$

All of these are valid linear combinations.

## Representing Vectors

There are three main ways to describe a vector **v**:

- By its components: (4, 2)
- As an arrow from (0, 0) to (4, 2)
- As a point at (4, 2) in the plane

You can visualize **v + w** as going along **v**, then along **w**, or directly along the diagonal from start to finish.

## Vectors in 3D

A 3D vector looks like: $\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix}$This points from $(0, 0, 0)$ to $(v₁, v₂, v₃)$ in 3D space.

Writing $\mathbf{v} = (1, 1, -1)$ is a shortcut for the column vector$\begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix}$It is not a row vector which is the **transpose**.

Addition in 3D works the same way: $\mathbf{v} + \mathbf{w} = \begin{bmatrix} v_1 + w_1 \\ v_2 + w_2 \\ v_3 + w_3 \end{bmatrix}$