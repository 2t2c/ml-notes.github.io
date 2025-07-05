# Lengths and Dot Products

## Length/Magnitude

An important case of the dot product is when a vector is dotted with itself. In this case, we have $v = w$.

For example, if $v=(1,2,3)$, then the dot product with itself is: $\mathbf{v} \cdot \mathbf{v} = \|\mathbf{v}\|^2 = 1^2 + 2^2 + 3^2 = 14$

This value is known as the **dot product** $\mathbf{v} \cdot \mathbf{v}$, which also equals the **squared length** of the vector. There is no angle between a vector and itself; we can think of this angle as $0^\circ$, not $90^\circ$. The result is not zero because a vector is never perpendicular to itself.

The dot product $\mathbf{v} \cdot \mathbf{v}$ gives the **length squared** of the vector.

**Definition**: The **length** (or norm) $\|\mathbf{v}\|$ of a vector $\mathbf{v}$ is the square root of the dot product of the vector with itself:

$$
length = \|\mathbf{v}\| = \sqrt{\mathbf{v} \cdot \mathbf{v}} = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}
$$

where $n$ is the number of dimensions.

### Unit Vector

The word **"unit"** always indicates that some measurement equals one. For example:

- A **unit price** is the price for one item.
- A **unit cube** has sides of length one.
- A **unit circle** is a circle with radius one.
- 

**Definition**: A **unit vector** $u$ is a vector whose length equals one. This implies: $u⋅u=1$

An example in four dimensions is: $\mathbf{u} = \left( \tfrac{1}{2}, \tfrac{1}{2}, \tfrac{1}{2}, \tfrac{1}{2} \right).$

Then the dot product is: $\mathbf{u} \cdot \mathbf{u} = \left( \tfrac{1}{2} \right)^2 + \left( \tfrac{1}{2} \right)^2 + \left( \tfrac{1}{2} \right)^2 + \left( \tfrac{1}{2} \right)^2 = \tfrac{1}{4} + \tfrac{1}{4} + \tfrac{1}{4} + \tfrac{1}{4} = 1$.

We obtained this unit vector by dividing the vector $\mathbf{v} = (1, 1, 1, 1)$ by its length: $\|\mathbf{v}\| = \sqrt{1^2 + 1^2 + 1^2 + 1^2} = \sqrt{4} = 2$

so the unit vector is: $\mathbf{u} = \frac{\mathbf{v}}{\|\mathbf{v}\|} = \left( \tfrac{1}{2}, \tfrac{1}{2}, \tfrac{1}{2}, \tfrac{1}{2} \right)$.

### Inequalities

No matter the angle between the vectors, the dot product of $\frac{\mathbf{v}}{\|\mathbf{v}\|}$ with $\frac{\mathbf{w}}{\|\mathbf{w}\|}$ never exceeds one.

This fact is captured by the **Cauchy–Schwarz inequality**, also known historically as the **Schwarz inequality** or the **Cauchy–Schwarz–Bunyakovsky inequality**. It was discovered independently in France, Germany, and Russia. This inequality is one of the most important in all of mathematics.

Since $\cos \theta| \leq 1$, the cosine formula for the dot product implies two foundational inequalities:

**Schwarz Inequality**: $|\mathbf{v} \cdot \mathbf{w}| \leq \|\mathbf{v}\| \, \|\mathbf{w}\|$

**Triangle Inequality**: $\|\mathbf{v} + \mathbf{w}\| \leq \|\mathbf{v}\| + \|\mathbf{w}\|$

These inequalities hold for any vectors $v$ and $w$ in Euclidean space. These inequalities are essential in proving orthogonality, estimating angles, and ensuring numerical stability in computations.

## Dot Product

The **dot product** (also called scalar product) takes two vectors and gives a number (a scalar), not a vector.

### Formula

If

$$
\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix}, \quad \mathbf{w} = \begin{bmatrix} w_1 \\ w_2 \end{bmatrix}
$$

then:The dot product w · v equals v · w. The order of v and w makes no difference.

$$
\mathbf{v} \cdot \mathbf{w} = v_1 w_1 + v_2 w_2
$$

In 3D:

$$
\mathbf{v} \cdot \mathbf{w} = v_1 w_1 + v_2 w_2 + v_3 w_3
$$

<aside>
💡

The dot product $w \cdot v$ equals $v \cdot w$. The order of v and w makes no difference.

</aside>

### Geometric Meaning

The dot product also equals:

$$
\mathbf{v} \cdot \mathbf{w} = \|\mathbf{v}\| \|\mathbf{w}\| \cos(\theta)
$$

where **θ** is the angle between the vectors.

This tells us:

- If the dot product is **positive**, the angle is **acute** (< 90°) (~same direction)
- If it is **zero**, the vectors are **perpendicular (orthogonal)**
- If it is **negative**, the angle is **obtuse** (> 90°) (~opposite direction)

### Example

Let

$$
\mathbf{v} = \begin{bmatrix} 1 \\ 3 \end{bmatrix}, \quad \mathbf{w} = \begin{bmatrix} 4 \\ -2 \end{bmatrix}
$$

Then:

$$
\mathbf{v} \cdot \mathbf{w} = 1 \cdot 4 + 3 \cdot (-2) = 4 - 6 = -2
$$

The result is a number: **-2**.

### Working

- The dot product helps project one vector onto another.
- It measures how much one vector extends in the direction of another.
- Used to find angles between vectors and to project one vector onto another.
- In physics, **work = force ⋅ displacement**.

## Cross Product

The **cross product** is only defined in 3D. It takes two vectors and gives a **new vector**, not a number.

### Formula

If

$$
\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix}, \quad \mathbf{w} = \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix}
$$

then:

$$
\mathbf{v} \times \mathbf{w} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{vmatrix}
\\
\mathbf{v} \times \mathbf{w} = (v_2 w_3 - v_3 w_2)\mathbf{i} - (v_3 w_1 - v_1 w_3)\mathbf{j} + (v_1 w_2 - v_2 w_1)\mathbf{k}
\\
\mathbf{v} \times \mathbf{w} = \begin{bmatrix} 
v_2 w_3 - v_3 w_2 \\
v_3 w_1 - v_1 w_3 \\
v_1 w_2 - v_2 w_1
\end{bmatrix}
$$

This new vector is perpendicular to both **v** and **w**.

### Geometric Meaning

The **length** of the cross product is:

$$
||\mathbf{v} \times \mathbf{w}\| = \|\mathbf{v}\| \|\mathbf{w}\| \sin(\theta)
$$

This is the area of the parallelogram formed by the two vectors.

### Right-Hand Rule

To find the direction of the cross product:

1. Point your right-hand fingers along **v**
2. Curl toward **w**
3. Your thumb points in the direction of $\mathbf{v} \times \mathbf{w}$

### Example

Let

$$
\mathbf{v} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \quad \mathbf{w} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
$$

Then:

$$
\mathbf{v} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \quad \mathbf{w} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
\\
\mathbf{v} \times \mathbf{w} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{vmatrix}
\\
\mathbf{v} \times \mathbf{w} = \mathbf{i}(0 \cdot 0 - 0 \cdot 1) - \mathbf{j}(1 \cdot 0 - 0 \cdot 0) + \mathbf{k}(1 \cdot 1 - 0 \cdot 0)
\mathbf{v} \times \mathbf{w} = \mathbf{i}(0) - \mathbf{j}(0) + \mathbf{k}(1)
\\
\mathbf{v} \times \mathbf{w} = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
$$

The result is a vector pointing along the z-axis.

### Working

- Produces a vector perpendicular (normal) to both input vectors.
- Direction follows the right-hand rule.
- Magnitude equals the **area of the parallelogram** formed by the two vectors.
- Zero vector if the vectors are parallel or one is zero.
- Useful for finding normals to planes and calculating torque.