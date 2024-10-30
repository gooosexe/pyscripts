import matplotlib.pyplot as plt
import math


"""
x and y are reals
a_1 := max(x, y)
g_1 := min(x, y)

a_n+1 = (a_n + g_n)/2
g_n+1 = sqrt(a_n * g_n)
"""

def arithmetic_geometric_mean(x, y, n):
	a = float(max(x, y))
	g = float(min(x, y))

	for i in range(n):
		a_n = (a + g) / 2.0
		print(a_n)
		g_n = math.sqrt(a * g)
		print(g_n)
		a = a_n
		g = g_n
		plt.plot(i, a, 'ro')
		plt.plot(i, g, 'bo')
	
	return a, g

print(arithmetic_geometric_mean(32039093482.9, 29330309340.2, 100))
plt.title("a g")
plt.xlabel("i")
plt.ylabel("value")
plt.show()
