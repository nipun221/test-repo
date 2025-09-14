print("Hello world")

import numpy as np
a = np.array([1, 2, 3, 4])

# Element-wise operations
print(a * 2)  

# Multi-dimensional array
res = np.array([[1, 2], [3, 4]])
print(res * 2)

s = "hello geeks"
s1 = "H" + s[1:]                   # update first character
s2 = s.replace("geeks", "GeeksforGeeks")  # replace word
print(s1)
print(s2)