# 1
def a():
    return 5


print(a())
# Prints 5
# 2


def a():
    return 5


print(a()+a())
# 5 + 5 = 10
# Prints 10
# 3


def a():
    return 5
    return 10


print(a())
# Returns only 5
# Prints 5
# 4


def a():
    return 5
    print(10)


print(a())
# Returns only 5
# Print 5
# 5


def a():
    print(5)


x = a()
print(x)
# x = null
# Print 5
# Print Null
# 6


def a(b, c):
    print(b+c)


print(a(1, 2) + a(2, 3))
# Print 3
# Print 5
# Error: Cant print because no value is returned within function
# 7


def a(b, c):
    return str(b)+str(c)


print(a(2, 5))
# Converts arguments into strings and concatenates them
# Print 25
# 8


def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7


print(a())
# Print 100
# If b is less than 10, return 5. But 100 is greater than 10, so skip
# Return 10 (7 never executes)
# Print 10
# 9


def a(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3


print(a(2, 3))
print(a(5, 3))
print(a(2, 3) + a(5, 3))
# Pass 2, 3
# 2 is less than 3
# 	Return and print 7
# Pass 5, 3
# 5 is not less than 3
# 	Return and print 14
# Pass 2, 3 along with 5, 3
# 2, 3 returns 7; 5, 3 returns 14
# 7 + 14 = 21
# 	Print 21


def a(b, c):
    return b+c
    return 10


print(a(3, 5))
# Pass 3, 5
# Return 3+5 -> 8 (10 never executes)
# Print 8
# 11
b = 500
print(b)


def a():
    b = 300
    print(b)


print(b)
a()
print(b)
# b = 500
# Print 500
# Print 500 (still global)
# Run a() and print 300 (local)
# Print 500 (global b)


# 12
b = 500
print(b)


def a():
    b = 300
    print(b)
    return b


print(b)
a()
print(b)
#b = 500
# Print 500
# Print 500 (global unchanged)
# run a(); local b = 300
# 	Print 300 (local)
# 	Return 300 (goes nowhere and remains unused)
# Print 500 (still unchanged globally)

# 13
b = 500
print(b)


def a():
    b = 300
    print(b)
    return b


print(b)
b = a()
print(b)
# b = 500
# Print 500 (global)
# Print 500 (unchanged global var)
# b = a() --> sets b (local) to = 300.
# 	print 300 (still local)
# 	return 300
# b (global) = 300
# print 300
# 14


def a():
    print(1)
    b()
    print(2)


def b():
    print(3)


a()
# call a()
# 	print 1
# 	call b() -->
# 		print 3
# 	print 2
# 15


def a():
    print(1)
    x = b()
    print(x)
    return 10


def b():
    print(3)
    return 5


y = a()
print(y)
# y = a() -->
#	print 1
#	x = b() -->
#		print 3
#		return 5
#	x = 5
#	print 5
#	return 10
# y = 10
# print 10
