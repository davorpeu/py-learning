num = 5
print(num)
num1 = 5.1
print(num1)
type(num1)
is_true = True
print(is_true)
notype = None
print(notype)
a = 6
b = 2
c = a + b
print(c)
d = a - b
print(d)
e = a * b
print(e)
f = a / b
print(f)
g = a ** b
print(g)

ab = 5
ac = 2

ad = ab > ac
print(ad)
ae = ab < ac
print(ae)
af = ab == ac
print(af)
print(ab > 5)
# day 2
print("day 2")
print(a == 2 and b == 10)  # and
print(a == 10 or b == 10)  # or
print(not (a == 10))  # not
print(not (a == 2))

# conditional statements

number = 13
if number == 9:
    print("Number is 9")
elif number < 9:
    print("Number is less than 9")
else:
    print("Number is more than 9")

is_avialable = True

if is_avialable:
    print("Yes it is available")
else:
    print("Not available")


is_free = True
if not is_free:
    print("Not Free")
else:
    print("It's Free")

data = None
if data:
    print("data is not none")
else:
    print("data is none")

num_a = 10
num_b = 5
if num_a > num_b:
    print("num_a is greater than num_b")

# inline if else
num = 5
print("Number is five") if num == 5 else print("Number is not five")

# nested if-else
num = 25
if num > 10:
    print("Number is greater than 10")
    if num > 20:
        print("Number is greater than 20")
    if num > 30:
        print("number is greather than 30")
else:
        print("number is smaller than 10")


num = 10
if num > 5 and num < 15:
    print (num)
else:
    print("Number may be small than 5 or larger than 15")






