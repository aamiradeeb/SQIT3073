import os

try:
    # Attempt to clear the screen for macOS
    os.system('clear')
except:
    try:
        # Attempt to clear the screen for Windows if the first try fails
        os.system('cls')
    except:
        # Output an error message if both attempts fail
        print("Unable to clear the screen.")


import numpy as np

# Create two 2D matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 3], [2, 1]])

# Comparison Operations
print("Comparison Operations")
print("A < B:", A < B)
print("A <= B:", A <= B)
print("A == B:", A == B)
print("A != B:", A != B)
print("A >= B:", A >= B)
print("A > B:", A > B)

# Arithmetic Operations
print("\nArithmetic Operations")
print("A + B:", A + B)
print("A - B:", A - B)
print("A * B:", A * B)
print("A / B:", A / B)
print("Reciprocal of A:", 1 / A)
print("Square of A:", np.square(A))

# Exponential Operations
print("\nExponential Operations")
print("exp(A):", np.exp(A))
print("expm1(A):", np.expm1(A))
print("exp2(A):", np.exp2(A))
print("log(A):", np.log(A))
print("log10(A):", np.log10(A))
print("log1p(A):", np.log1p(A))
print("log2(A):", np.log2(A))
print("power(A, 2):", np.power(A, 2))
print("sqrt(A):", np.sqrt(A))

# Trigonometric Operations
print("\nTrigonometric Operations")
print("sin(A):", np.sin(A))
print("cos(A):", np.cos(A))
print("tan(A):", np.tan(A))
print("arcsin(A/5):", np.arcsin(A / 5))
print("arccos(A/5):", np.arccos(A / 5))

# Hyperbolic Operations
print("\nHyperbolic Operations")
print("sinh(A):", np.sinh(A))
print("cosh(A):", np.cosh(A))
print("tanh(A):", np.tanh(A))
print("arcsinh(A):", np.arcsinh(A))
print("arccosh(A + 1):", np.arccosh(A + 1))

# Bitwise Operations
print("\nBitwise Operations")
print("A & B:", A & B)
print("A | B:", A | B)
print("~A:", ~A)
print("A ^ B:", A ^ B)
print("A << 1:", A << 1)
print("A >> 1:", A >> 1)

# Logical Operations
print("\nLogical Operations")
print("np.logical_and(A, B):", np.logical_and(A, B))
print("np.logical_xor(A, B):", np.logical_xor(A, B))
print("np.logical_not(A):", np.logical_not(A))
print("np.logical_or(A, B):", np.logical_or(A, B))

# Predicates
print("\nPredicates")
print("np.isfinite(A):", np.isfinite(A))
print("np.isinf(A):", np.isinf(A))
print("np.isnan(A):", np.isnan(A))
print("np.signbit(A):", np.signbit(A))

# Other Operations
print("\nOther Operations")
print("np.abs(A):", np.abs(A))
print("np.ceil(A):", np.ceil(A))
print("np.floor(A):", np.floor(A))
print("np.mod(A, 3):", np.mod(A, 3))
print("np.modf(A):", np.modf(A))
print("np.round(A):", np.round(A))
print("np.trunc(A):", np.trunc(A))
print("np.sinc(A):", np.sinc(A))
print("np.sign(A):", np.sign(A))

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my