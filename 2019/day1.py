import itertools

# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.

def open_doc(doc):
    with open(doc, "r") as f:
        return [int(i.strip()) for i in f.readlines()]

def module_calc(masses):
    total_fuel = 0
    for mass in masses:
        total_fuel += calc(mass)
    return total_fuel

def module_calc_with_fuel(masses):
    total_fuel = 0
    for mass in masses:
        total_fuel += calc_with_fuel(mass)
    return total_fuel

def calc(mass: int) -> int:
    return mass // 3 - 2

def calc_with_fuel(mass: int) -> int:
    fuel_mass = mass // 3 - 2
    if fuel_mass > 0:
        fuel_mass += calc_with_fuel(fuel_mass)
    else:
        fuel_mass = 0
    return fuel_mass

print(module_calc(open_doc("day1_input")))

assert module_calc([12]) == 2
assert module_calc([14]) == 2
assert module_calc([1969]) == 654
assert module_calc([100756]) == 33583

# At first, a module of mass 1969 requires 654 fuel.
# Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel,
# which requires 5 fuel, which requires no further fuel.
# So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
# The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.

assert calc_with_fuel(1969) == 966
assert calc_with_fuel(100756) == 50346

print(module_calc_with_fuel(open_doc("day1_input")))