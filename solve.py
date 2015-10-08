from blessings import Terminal # $ pip install blessings
import colorama # $ pip install colorama
colorama.init() # replace ANSI escapes with Win32 calls in stdout/stderr

t = Terminal()

import numpy
import math
import time
from itertools import count, izip

try:
	matrixFile = open("200x200.200x200", "r")
	epsilon = float(matrixFile.readline())
	numberOfDimensions = int(matrixFile.readline())
except Exception as e:
	print("Problem is: \n" + str(e))

matrix = [[0] * numberOfDimensions for i in range(numberOfDimensions)]
tay = 1.5
b = []
x = []

numberOfIterations = 0
norma = 0.0

try:
	for i in range(numberOfDimensions):
		b.append(float(matrixFile.readline()))

	for i in range(numberOfDimensions):
		for j in range(numberOfDimensions):
			matrix[i][j] = float(matrixFile.readline())

	for i in range(numberOfDimensions):
		x.append(0.0)

	matrixT = numpy.transpose(matrix)
	matrix = numpy.dot(matrixT, matrix)
	b = numpy.dot(matrixT, b)
except Exception as e:
	print("Problem is: \n" + str(e))

D = [[0] * numberOfDimensions for i in range(numberOfDimensions)]
L = [[0] * numberOfDimensions for i in range(numberOfDimensions)]
U = [[0] * numberOfDimensions for i in range(numberOfDimensions)]

try:
	for i in range(numberOfDimensions):
		for j in range(numberOfDimensions):
			if i < j:
				U[i][j] = matrix[i][j]
			if i > j:
				L[i][j] = matrix[i][j]
			if i == j:
				D[i][j] = matrix[i][j]
except Exception as e:
	print("Problem is: \n" + str(e))


dt1 = time.clock()
Q = numpy.linalg.inv(D+numpy.dot(tay,L))
K = numpy.dot(Q, (numpy.dot((tay-1.0), D) + numpy.dot(tay, U)))
F = numpy.dot(tay, numpy.dot(Q, b))

try:
	while True:
		numberOfIterations += 1
		x = numpy.dot(-1.0, numpy.dot(K, x)) + F
		norma = numpy.linalg.norm(numpy.dot(matrix, x) - b)
		if numberOfIterations % 1000 == 0:
			print(numberOfIterations)
			print("\n")
			print("Itreation number " + str(numberOfIterations))
			print("Norm is " +  str(norma))
			print("\n")
		if norma < epsilon:
			break
except Exception as e:
	print("Problem is: \n" + str(e))

x_ex = numpy.linalg.solve(matrix, b)
err = x - x_ex
dt2 = time.clock()


print("\n")
print('\033[1m' + '\033[4m' + t.blue("In the issue: \n"))
print(t.cyan("Parameter tay is ") + t.red(str(tay)))
print(t.cyan("Nubmer of iterations ") + t.red(str(numberOfIterations)))
#print("Solution is ", x)
print(t.cyan("Error is ") + t.red(str(numpy.linalg.norm(err))))
print(t.cyan("Time of solve ") + t.red(str(dt2-dt1)) + t.cyan(" with tay ") + t.red(str(tay)))
print("\n")
