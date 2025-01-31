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