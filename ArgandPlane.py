#---------------------------------  Multiplication of two Complex Numbers on the Argand Plane ---------------------------------

import matplotlib.pyplot as plt


x = [] # list for real part of the entered complex numbers
y = [] # list for imaginary part of the entered complex numbers

for jill in range(0, 2):   # range is specified for the input of two complex numbers only
    
    # the complex numbers being of the form re + i(ima)
    
    re = float(input("enter the real part: ")) 
    ima = float(input("enter the imaginary part: "))
    
    x.append(re)
    y.append(ima)
    
# product being of the form t + ib

t = x[0] * x[1] - y[0] * y[1] # real part of the product
b = x[0] * y[1] + y[0] * x[1] # imaginary part of the product
    
    
plt.scatter(x, y, label="Numbers to be multiplied", marker="o", color="Blue", s=60)
plt.scatter(t, b, label="Product of the numbers", marker="*", color="Green", s=70)

plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.title('Argand Plane')


plt.legend()
plt.show()
