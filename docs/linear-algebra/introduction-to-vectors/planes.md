# Planes

## What is a Plane?

A **plane** is a flat, two-dimensional surface that extends infinitely in 3D space. Think of it like an endless sheet of paper floating in space, it has length and width, but no thickness.

## How Do We Define a Plane?

A plane in 3D space can be defined in two main ways:

### 1. Using a Point and a Normal Vector (General)

The general equation of a plane is:

$$
\begin{gathered}
ax+by+cz=d \\
\vec{n}\cdot(\vec{r}-\vec{r_0})
\end{gathered}
$$

Here:

- $\vec{n}=⟨a,b,c⟩$ is the normal vector i.e. a vector that is perpendicular to the plane and `a,b,c` are the components of the vectors.
- $\vec{r} = ⟨x,y,z⟩$ is a variable point on the plane.
- $\vec{r_0} = ⟨x_0,y_0,z_0⟩$ is a known point on the plane.
- `d` is a constant that shifts the plane away from the origin along the direction of the normal vector.

This form tells us: any point `(x, y, z)` that satisfies the equation lies on the plane.

**Example:**

$$
\begin{gathered}
\vec{n}\cdot(\vec{r}-\vec{r_0}) = \langle 4, 5, 6 \rangle \cdot \langle x - 1, y - 2, z - 3 \rangle \\
4(x - 1) + 5(y - 2) + 6(z - 3) = 0 \\
4x + 5y + 6z = 32
\end{gathered}
$$

This describes a plane in 3D space with normal vector `(2,3,5)`.

### 2. Using Two Vectors (Parametric Form)

A plane can also be defined using **two linearly independent vectors** that lie in the plane. Generally used for visualizations, sampling etc. If $v$ and $w$ are such vectors, then all points on the plane can be described by:

To define a plane using vectors, you need:

- A **point** $\mathbf{p} = (x_0, y_0, z_0)$ that lies on the plane
- Two **linearly independent vectors** $v, w$ that lie **in** the plane

Then the parametric equation of the plane is:

$$
r(s,t)=p+sv+tw
$$

Where:

- $s$ and $t$ are real numbers (parameters)
- $r(s,t)$ gives all points on the plane

### Example:

Let:

- Point on the plane: $p=(1,0,0)$
- Direction vectors: $v=(2,2,0),  w=(0,2,1)$

Then the plane is:

$$
r(s,t)=(1,0,0)+s(2,2,0)+t(0,2,1)
$$

Expanding:

$$
r(s,t)=(1+2s,2s+2t,t)
$$

This gives all points on the plane by varying $s$ and $t$.

## Why Are Planes Important?

Planes are fundamental in geometry, linear algebra, computer graphics, and physics. They help:

- Visualize and solve systems of linear equations
- Define surfaces, collisions, or boundaries
- Represent flat objects like walls, screens, or layers in 3D models

## Resources

1. https://www.youtube.com/watch?v=HjJ140TYbXQ