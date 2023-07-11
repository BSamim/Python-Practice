import math

# print the square root of 0
print(math.sqrt(0))

# print the square root of 4
print(math.sqrt(4))

# print the square root of 3.5
print(math.sqrt(3.5))

a = math.pi / 6

# returning the value of sine of pi/6
print("The value of sine of pi/6 is : ", end="")
print(math.sin(a))

# returning the value of cosine of pi/6
print("The value of cosine of pi/6 is : ", end="")
print(math.cos(a))

# returning the value of tangent of pi/6
print("The value of tangent of pi/6 is : ", end="")
print(math.tan(a))

# initializing argument
gamma_var = 6

# Printing the gamma value.
print("The gamma value of the given argument is : "
      + str(math.gamma(gamma_var)))

# isinf() function is used to check whether the value is infinity or not.
# with inbuilt numbers
print(math.isinf(math.pi))
print(math.isinf(math.e))

# checking for NaN value
print(math.isinf(float('inf')))

# isnan() function returns true if the number is “NaN” else returns false.
# with inbuilt numbers
print(math.isnan(math.pi))
print(math.isnan(math.e))

# checking for NaN value
print(math.isnan(float('nan')))
