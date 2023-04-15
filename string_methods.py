string = 'string methods ß'
# Converts the first character to upper case
print(string.capitalize())  # String methods ß

# Converts to upper case
print(string.upper())  # STRING METHODS SS

# Converts to lower case
print(string.lower())  # string methods ß

# Converts to lower case aggressively
print(string.casefold())  # string methods ss

# Returns a centered string
print(string.center(40))  # string methods ß

# Returns the number of times a specified value occurs in a string
print(string.count('t'))  # 2

# Returns an encoded version of the string
print(string.encode())  # b'string methods \xc3\x9f'

# Returns true if the string ends with the specified value
print(string.endswith('ß'))  # True
print(string.endswith('a'))  # false

# Searches the string for a specified value and returns the position of where it was found
print(string.find('meth'))  # 7

# Formats specified values in a string
string1 = 'This is {method} method'
string2 = 'This is {method1} method {method2}'
methods = {'method1': 'format_map', 'method2': 'format_map1'}
print(string1.format(method='format'))  # This is format method
print(string2.format_map(methods))  # This is format_map method format_map1

# Searches the string for a specified value and returns the position of where it was found
print(string.index('th'))  # 9

# Returns True if all characters in the string are alphanumeric
print(string.isalnum())  # False

# Returns True if all characters in the string are alphabet
print(string.isalpha())  # False

# Returns True if all characters in the string are ascii
print(string.isascii())  # False

# Returns True if all characters in the string are decimal
print(string.isdecimal())  # False

# Returns True if all characters in the string are digit
print(string.isdigit())  # False

# Returns True if the string is an identifier
print(string.isidentifier())  # False

# Returns True if all characters in the string are lower case
print(string.islower())  # True

# Returns a left trim version of the string
string3 = "     banana     "
x = string3.lstrip()
# of all fruits banana      is my favorite
print("of all fruits", x, "is my favorite")


# Returns a right trim version of the string
x = string3.rstrip()
# of all fruits      banana is my favorite
print("of all fruits", x, "is my favorite")

# Returns True if all characters in the string are numeric
print(string.isnumeric())  # False


# Returns a translation table to be used in translations
mytable = string.maketrans("s", "P")
print(string.translate(mytable))  # Ptring methodP ß

# Returns a tuple where the string is parted into three parts from 1st occurence
print(string.partition('string'))  # ('', 'string', ' methods ß')

# Returns a string where a specified value is replaced with a specified value
print(string.replace('m', 'b'))  # string bethods ß

# Searches the string for a specified value and returns the last position of where it was found
print(string.rfind('ing'))  # 3

# Searches the string for a specified value and returns the last position of where it was found
print(string.rindex('ng'))  # 4

# Returns a right justified version of the string
print(string.rjust(20))  # string methods ß

# Returns a tuple where the string is parted into three parts from last occurence
print(string.rpartition('string'))  # ('', 'string', ' methods ß')

# Splits the string at the specified separator, and returns a list
print(string.rsplit('ng'))  # ['stri', ' methods ß']

# Returns a right trim version of the string
print(string.rstrip('methods ß'))  # string

# Splits the string at the specified separator, and returns a list
print(string.split(' '))  # ['string', 'methods', 'ß']

# Splits the string at line breaks and returns a list
string4 = "banana\n asd"
print(string4.splitlines())  # ['banana', ' asd']

# Returns true if the string starts with the specified value
print(string.startswith('st'))  # True

# Returns a trimmed version of the string
print(string.strip('dsß'))  # tring methods

# Swaps cases, lower case becomes upper case and vice versa
print(string.capitalize().swapcase())  # sTRING METHODS SS

# Converts the first character of each word to upper case
print(string.title())  # String Methods Ss

# Returns a translated string
mytable = string.maketrans("s", "P")
print(mytable)  # {115: 80}
print(string.translate(mytable))  # Ptring MethodP ß

# Fills the string with a specified number of 0 values at the beginning
print("s".zfill(10))  # 000000000s
