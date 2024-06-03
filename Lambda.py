def square (num): return num ** 2
numbers = [1,3,5,9]
print(list(map(square,numbers)))

for item in map(square,numbers):
    print(item)

#def square (num): return num ** 2
square = lambda num:num**2
numbers = [1,3,5,9]
print(list(map(square,numbers)))
print(square(3))

#for item in map(square,numbers):
#    print(item)

numbers = [1,3,5,9,10,4]
def check_even(num):
    return num%2==0
print(list(filter(check_even,numbers)))
print(list(filter(lambda num:num%2==0,numbers)))

check_even=lambda num:num%2==0
print(list(filter(check_even,numbers)))
print(check_even(numbers[2]))
