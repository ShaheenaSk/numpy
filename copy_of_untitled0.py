# -*- coding: utf-8 -*-
"""Copy of Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10sDPypIHEbTjMMaTtbEYg03iywXO6m1L
"""

import numpy as np
a=np.array([1,3,5])
print(a)
print(a.shape)

import numpy as np
a=np.array([1,3,5,6])
print(a)
print(a.shape)

import numpy as np
a=np.array([[1,3,5],[5,1,9]])
print(a)
print(a.shape)
print (a[0,0],a[1,2],a[1,0])

a=np.zeros((4,4))
print(a)

a=np.array([[1,3,5,6],[2,5,1,9],[1,8,4,2]])
print(a)
print(a.shape)
print(type(a))

a=np.eye(2)
print(a)

a=np.random.random((3,3))
print(a)

a=np.array([[1,3,5,6],[2,5,1,9],[1,8,4,2]])
b=a[:2,:2]
print(b)

b[0,1]=66
print(b[0,1])
print(b)

print(a)
print(b)