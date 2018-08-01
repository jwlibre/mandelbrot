# Python code to generate and plot a Mandelbrot set, given specified parameters, using the Escape Time algorithm

# jwlibre 1st August 2018

from matplotlib import pyplot

points_x = [] # these will be the input Real values of c
points_y = [] # these will be the input Imag values of c
points = []

max_iterations = 100
cap = 4 # sets boundaries beyond which the modulus of the complex number z
        # cannot exceed, else it will be considered to be tending to infinity
M = []

for k in range(-250,100):
    points_x.append(k/100)

for q in range(-100,100):
    points_y.append(q/100)

for x in points_x:
    for y in points_y:
        points.append(complex(real=x, imag=y))

print(points)

for point in points:

    z = []
    c = []
    z0 = complex(0,0)
    z.append(z0)

    iteration = 0
    temp2 = 0

    while iteration < max_iterations and abs(temp2) < cap:
        temp = z[iteration]
        temp2 = temp**2 + point
        z.append(temp2)
        iteration = iteration + 1

    if iteration == max_iterations:
        M.append(point)

print (M)
print(len(points))
print(len(M))

x_M = []
y_M = []
for value_M in M:
    x_M.append(value_M.real)
    y_M.append(value_M.imag)

print("x_M =",x_M)
print("y_M =",y_M)

pyplot.scatter(x_M,y_M)
pyplot.show()
