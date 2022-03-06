iteration = int(input("Enter the total number of iterations: "))
presumm = 0
div = 1
sign = True
for i in range(iteration):
    presumm = presumm + 1 / div if sign else presumm - 1 / div
    div += 2
    sign = not sign
pi = presumm * 4
print(pi)