import math

def get_data(d):
    with open("./input/" + str(d) + ".txt", 'r') as i:
        return i.read().splitlines()

def get_fuel(mass):
    return math.floor(int(mass) / 3) - 2

def get_fuel_rec(mass):
    f_total = 0
    while get_fuel(mass) > 0:
        added_fuel = get_fuel(mass)
        if added_fuel > 0:
            f_total += added_fuel
            mass = added_fuel
    return f_total

def main():
    total = 0
    for module in get_data(1):
        total += get_fuel_rec(module)
    print(total)

if __name__ == "__main__":
    main()

