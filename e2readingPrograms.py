#for loopin
stop = int(input())
result = 0
for a in range(4):
    print(a, end=': ')
    for b in range(3):
        result += a + b
        if result > stop:
            print('-', end=' ')
            continue
        print(result, end=' ')
    print()

#simon says code comparison code
user_score = 0
simon_pattern = input()
user_pattern  = input()

for a in range(len(simon_pattern)):
    if simon_pattern[a] == user_pattern[a]:
        user_score+=1
    elif simon_pattern[a] != user_pattern[a]:
        break

print(f'User score: {user_score}')

#loop else
result = 0
n = 1
while n < 4:
    print(n, end=' ')
    result += 4
    n += 1
else:
    print(f'| {result}')
print('done')

result = 0
n = 2
while n > -6:
    print(n, end=' ')
    result -= 2
    if result < -4:
        print('$')
        break
    n -= 1
else:
    print(f'/ {result}')
print('done')


result = 0
for n in range(4):
    print(n, end=' ')
    result += 2
else:
    print(f'\ {result}')
print('done')


stop = -13
total = 0
for number in [5, 2, 4, 6, 2, 4]:
    print(number, end=' ')
    total -= number
    if total <= stop:
        print('$')
        break
else:
    print(f'| {total}')
print('done')

#enumerate
seasons = ['winter', 'spring', 'summer', 'fall']
for (position, season) in enumerate(seasons):
    print(f'{position} {season}')


numbers = [-3, 4, 2, 5]
for position, number in enumerate(numbers):
    if number < 0:
        print(f'{position} {number}')
    else:
        print(f'{position} x')

# find volumne of a pyramid given dimensions
def calc_pyramid_volume(base_length, base_width, pyramid_height):
    base_area = base_length * base_width
    volume = (base_area * pyramid_height) / 3
    return volume

length = float(input())
width = float(input())
height = float(input())
print(f'Volume for {length}{width}{height} is: {calc_pyramid_volume(length, width, height):.2f}')

# print feet inch inches when given num feet and num inches
def print_feet_inch_short(num_feet, num_inches):
    print(num_feet, end="' ")
    print(num_inches, end="\"\n")

user_feet = int(input())
user_inches = int(input())

print_feet_inch_short(user_feet, user_inches) # Will be run with (5, 8), then (4, 11)

# mph_and_minutes_to_miles
def mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):
    hours_traveled = minutes_traveled / 60.0
    miles_traveled = hours_traveled * miles_per_hour
    return miles_traveled

miles_per_hour = float(input())
minutes_traveled = float(input())

print(f'Miles: {mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):f}')

#modular mathematical function calc pyramid volume
def calc_base_area(base_length, base_width):
   return base_length * base_width

def calc_pyramid_volume(base_length, base_width, pyramid_height):
    base_area = calc_base_area(base_length, base_width)
    pyramid_volume = base_area * pyramid_height * (1/3)
    return pyramid_volume

length = float(input())
width = float(input())
height = float(input())
print(f'Volume for {length} {width} {height} is: {calc_pyramid_volume(length, width, height):.2f}')
