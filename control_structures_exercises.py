
day_of_the_week = input("Enter a day please:")
  
if day_of_the_week == 'Tuesday':
    print(':(')
elif day_of_the_week == 'Wednesday':
    print(':|')
elif day_of_the_week == 'Thursday':
    print(':)')
elif day_of_the_week == 'Friday':
    print(':D')
elif day_of_the_week == 'Saturday':
    print(":'D")
elif day_of_the_week == 'Sunday':
    print(":|")
else:
    print(":'(")

day = input(f'Enter a day please:') 

if day == 'Monday':
    print("weekday")
elif day == 'Tuesday':
    print('weekday')
elif day == 'Wednesday':
    print('weekday')
elif day == 'Thursday':
    print('weekday')
elif day == 'Friday':
    print('weekday')
else:
    print("weekend")












number = 5

while number <= 15:
    print(number)
    number += 1

number = 0

while number <= 100:
  print(number)
  number += 2

number = 2

while number <= 1000000:
  print(number)
  number *= number


number = 100
while number >= 5:
    print(number)
    number -= 5

num = int(input("Enter a number: "))

print("Multiplication Table of", num)
for i in range(1,11):
    print(num,"x",i,"=",num * i)

num = '1','22','333','4444','55555','666666','7777777','88888888','999999999'
for nums in num:
    print(nums)

num = int(input("Enter a positive number please: "))
for i in range(num,0,-1):
    print(i)

num = int(input("Enter a positive number please: "))
for i in range(0,num+1):
    print(i)

num = int(input("Enter a positive odd number please: "))
for i in range(1,50):
    if i % 2 == 0:
        continue
    print(f'Here is an odd number: {i}')
    if i == num:
        print(f'Yikes! Skipping number: {i}')


n = 100      
for n in range(1,n+1):
    print(n)

n = 100      
for n in range(1,n+1):
    if n % 3==0:
        print("Fizz")
    else:
        print(n)

n = 100      
for n in range(1,n+1):
    if n % 3==0:
        print("Fizz")
    if n % 5==0:
        print("Buzz")
    else:
        print(n)

n = 100      
for n in range(1,n+1):
    if n % 3==0:
        print("Fizz")
    if n % 5==0:
        print("Buzz")
    if n % 3==0 and n % 5==0:
        print("FizzBuzz")
    else:
        print(n)

while True:
    user_input = input('Please submit a positive number: ')

    if user_input.isdigit():
        user_input = int(user_input)
        if user_input > 0:
            print('Thank you for submitting a positive number!')
            break

    else:
        print('Thats not a positive number!')

print('number | squared | cubed')
print('-------|---------|------')

for i in range(1, user_input+1):
    print()