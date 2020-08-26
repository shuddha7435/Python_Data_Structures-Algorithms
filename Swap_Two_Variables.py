
# Method 1 : Using a third variable

a = 10

b = 20

print("value of a before swapping is", a)
print("value of b before swapping is", b)


temp = a
a = b
b = temp

print("value of a after swapping is", a)
print("value of b after swapping is", b)


# Method 2 : Python's built in feature

a = 10

b = 20

print("value of a before swapping is", a)
print("value of b before swapping is", b)

a, b = b, a

print("value of a after swapping is", a)
print("value of b after swapping is", b)

# Method 3 : Using XOR

a = 10

b = 20

print("value of a before swapping is", a)
print("value of b before swapping is", b)

a = a ^ b

b = a ^ b

a = a ^ b

print("value of a after swapping is", a)
print("value of b after swapping is", b)
