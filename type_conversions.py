num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))

# implicit type conversion
int_num = 4
float_num = 4.2

new_num = int_num + float_num

print("Sum:",new_num)
print("Data type of num_sum:",type(new_num))
