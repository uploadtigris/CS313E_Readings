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

###############
def compute(numbers):
    result = 1
    for num in numbers:
        result *= num + 2
    return result

values = [6, 4, 5]
computed_value = compute(values)
print(computed_value)

#######################
values = [15, 9, 5, 3, 12, 10]

def print_selected_numbers():
    for number in values:
        if number > 5:
            print(number)

print_selected_numbers()

functions w/ branches/loops
def print_popcorn_time(bag_ounces):
    if bag_ounces < 3:
        print("Too small")
    elif bag_ounces > 10:
        print("Too large")
    else: print(6 * bag_ounces, "seconds")

user_ounces = int(input())
print_popcorn_time(user_ounces)


#many many loopies
def print_shampoo_instructions(num_cycles):
    if num_cycles < 1:
        print("Too few.")
    if num_cycles > 4:
        print("Too many.")
    else:
        for i in range(num_cycles):
            print(f'{i+1}: Lather and rinse.')
        if num_cycles >= 1:
            print("Done.")
    
        
user_cycles = int(input())
print_shampoo_instructions(user_cycles)

get user num and computer avg
def get_user_num():
    print('FIXME: Finish get_user_num()')
    return -1
    
def compute_avg(user_num1, user_num2):
    print('FIXME: Finish compute_avg()')
    return -1

user_num1 = 0
user_num2 = 0
avg_result = 0

user_num1 = get_user_num()
user_num2 = get_user_num()
avg_result = compute_avg(user_num1, user_num2)

print(f'Avg: {avg_result}')

# swap the first and last element of a lsit
def swap(a):
    new1 = a[0]
    a[0] = a[-1]
    a[-1] = new1
    return a
    
values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)

dollars to pennies
def number_of_pennies(dollars, pennies=0):
    num_dollars = dollars * 100
    total = num_dollars + pennies
    return total

print(number_of_pennies(int(input()), int(input()))) # Both dollars and pennies
print(number_of_pennies(int(input())))               # Dollars only

############################
# Splitting a check!
# FIXME: Write the split_check function. HINT: Calculate the amount of tip and tax,
# add to the bill total, then divide by the number of diners.

def split_check(bill, people, tax_percentage = 0.15, tip_percentage = 0.09):
    tip_tax = (bill * tax_percentage) + (bill * tip_percentage)
    bill_total = bill + tip_tax
    cost_per_diner = bill_total /people
    return cost_per_diner

bill = float(input())
people = int(input())

# Cost per diner at the default tax and tip percentages
print(f'Cost per diner: ${split_check(bill, people):.2f}')

bill = float(input())
people = int(input())
new_tax_percentage = float(input())
new_tip_percentage = float(input())

# Cost per diner at different tax and tip percentages
print(f'Cost per diner: ${split_check(bill, people, new_tax_percentage, new_tip_percentage):.2f}')

#################
Compute Gas volume
gas_const = 8.3144621

def compute_gas_volume(pressure, temperature, moles):
    gas_equation_volume = (moles * gas_const * temperature) / pressure
    return gas_equation_volume

gas_pressure = float(input())
gas_moles = float(input())
gas_temperature = float(input())
gas_volume = 0.0

gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
print(f'Gas volume: {gas_volume} m^3')

#########################
String Slicing
#######################
