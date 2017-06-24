import numpy as np

print "coconut juice:"
a = np.array([[0, 3, 1, 6, 2, 4, 5],
              [6, 5, 0, 1, 4, 3, 2],
              [2, 1, 3, 4, 0, 5, 6], 
              [3, 2, 6, 0, 5, 1, 4], 
              [1, 6, 4, 5, 3, 2, 0], 
              [5, 4, 2, 3, 6, 0, 1], 
              [4, 0, 5, 2, 1, 6, 3]])
b = np.array([97, 83, 105, 82, 80, 62, 100])
x = np.linalg.solve(a, b)
print x

print "gin:"
b = np.array([115, 104, 109, 74, 96, 106, 89])
x = np.linalg.solve(a, b)
print x

print "limes:"
b = np.array([98, 71, 109, 112, 88, 89, 105])
x = np.linalg.solve(a, b)
print x

print "oranges:"
b = np.array([112, 78, 86, 97, 127, 113, 80])
x = np.linalg.solve(a, b)
print x

print "strawberries:"
b = np.array([96, 90, 96, 128, 122, 108, 116])
x = np.linalg.solve(a, b)
print x

print "tequila:"
b = np.array([148, 120, 136, 113, 111, 110, 123])
x = np.linalg.solve(a, b)
print x