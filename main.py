# This line of code assigns the range of numbers to the variable number
# And for it to print from 1 to 10, you should give the last number as 11 in the range

for number in range(1, 11):
    print(number)

# The range function always steps through the start and end and increases by one
# If you want to increase by another number, the code below illustrates
#  This code will step through start to finish increasing the previous number by two
for number in range(1, 11, 2):
    print(number)
# Let's see how to add numbers between 1 and 100
sum_of_number = 0

for number in range(1, 101):
    sum_of_number  += number
print(sum_of_number)

# Let as print the numbers from 1 to 100
# For number that is divisible by 3 print Fizz,
# divisible by 5 print "Buzz",
# divisible by both print "FizzBuzz"
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
