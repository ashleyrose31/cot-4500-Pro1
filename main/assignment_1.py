#Approximation Algorithm - Question 1
def root_two():
    x0 = 1.5
    tol = 0.000001
    iter_count = 0 
    diff = x0
    x = x0
    print(f"{iter_count} : {x}")
    while diff >= tol:
        iter_count += 1
        y = x
        x = (x / 2) + (1 /x)
        print(f"{iter_count} : {x}")
        diff = abs(x-y)

    print(f"Convergence after 4 iterations")

    

root_two()

#Bisection Method -Question 2 --> referenced code from 2.1 on slide 14 to get output on slide 18 
import math
def bisection (f, left, right, tol=1e-3, max_iterations=10):
    if f(left) * f(right) >= 0:
        raise ValueError("Function values at interval endpoints have to have opposite signs.")
    for i in range(max_iterations):
        mid = (left + right) / 2
        print(f"Iteration {i+1}: x = {mid}")

        if abs(right-left) < tol:
            break
        if (f(left) < 0 and f(mid) > 0 or (f(left) > 0 and f(mid) < 0)):
            right = mid
        else: 
            left = mid
    print(f"\nConvergence after {i+1} iterations.")
    return mid 

f = lambda x: x**3 + 4*x**2 - 10
root = bisection(f, 1, 2)

print(f"Approximate root: {root}")

#Fixed-Point Iteration --> output for example in 2.2 on slide 14
def fixed_point_iteration(g, p0, tol=1e-3, max_iteration=100):
    i = 1

    while i <= max_iteration:
        p = g(p0)

        if abs(p-p0) < tol:
            print(f"{p} Success")
            return

        i += 1
        p0 = p

    print("Failure")

g = lambda x: (10 - 4*x**2) ** (1/3)
fixed_point_iteration(g, 1.5)