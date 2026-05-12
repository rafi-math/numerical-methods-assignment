# Numerical Methods in Python

This repository contains clean and simple implementations of fundamental numerical methods used in computational mathematics.

The purpose of this project is not only to make the programs work, but also to understand how classical numerical algorithms operate step by step.

All implementations are written in plain Python without relying on heavy external libraries. The focus is on transparency, mathematical reasoning, and structured implementation.

---

# Topics Covered

## Root Finding Methods

- Bisection Method
- Newton–Raphson Method
- Regula Falsi Method

## Interpolation Methods

- Newton Forward Interpolation
- Newton Backward Interpolation
- Divided Difference Interpolation
- Interpolating Polynomial Construction

## Linear System Solvers

- LU Factorization
- Gauss–Jordan Elimination

## Numerical Integration

- Trapezoidal Rule
- Error Estimation in Trapezoidal Rule

## Ordinary Differential Equations

- Euler’s Method
- Runge–Kutta Method

---

# Purpose of the Project

This project was developed to:

- Build a strong understanding of numerical analysis
- Practice mathematical algorithm implementation from scratch
- Improve structured programming skills
- Create a reusable academic reference
- Connect mathematical theory with computation

The main idea is simple:

No shortcuts.  
No black-box libraries.  
Only mathematics, logic, and implementation.

---

# Repository Structure

```text
Numerical-Methods-Python/
│
├── root_finding/
│   ├── bisection_method.py
│   ├── newton_raphson.py
│   └── regula_falsi.py
│
├── interpolation/
│   ├── newton_forward.py
│   ├── newton_backward.py
│   ├── divided_difference.py
│   └── interpolating_polynomial.py
│
├── linear_systems/
│   ├── lu_factorization.py
│   └── gauss_jordan.py
│
├── numerical_integration/
│   └── trapezoidal_rule.py
│
├── differential_equations/
│   ├── euler_method.py
│   └── runge_kutta.py
│
├── main.py
└── README.md
```

---

# Requirements

- Python 3.x
- No external libraries required

---

# How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/your-repository-name.git
```

Move into the project directory:

```bash
cd your-repository-name
```

Run the main file:

```bash
python main.py
```

Or run any individual method directly:

```bash
python root_finding/bisection_method.py
```

---

# Example Algorithms Included

## Bisection Method

Finds roots of nonlinear equations using interval halving.

## Newton–Raphson Method

Uses tangent approximation for fast root convergence.

## LU Factorization

Decomposes a matrix into lower and upper triangular matrices.

## Runge–Kutta Method

Provides higher accuracy numerical solutions for differential equations.

---

# Academic Applications

These implementations are suitable for:

- Numerical Analysis courses
- Engineering Mathematics
- Scientific Computing practice
- Algorithm learning
- Examination preparation
- Concept revision

---

# Design Philosophy

Clarity over complexity.  
Understanding over optimization.  
Structure over shortcuts.

Every algorithm in this repository is written so the logic can be followed line by line and directly connected to its mathematical formulation.

---

# Future Improvements

Possible future additions:

- Gauss Seidel Method
- Jacobi Iteration
- Simpson’s Rule
- Secant Method
- Numerical Differentiation
- Matrix Inversion
- Eigenvalue Methods

---

# Author

**Md. Ali Arman Rafi**  
3rd Year BSc. (Honours)
Department of Mathematics  
University of Chittagong
