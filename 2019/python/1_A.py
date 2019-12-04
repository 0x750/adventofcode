import math

def get_data(d):
    with open("./input/" + str(d) + ".txt", 'r') as i:
        return i.read().splitlines()

def main():
    total = 0
    for module in get_data(1):
        total += math.floor(int(module) / 3) - 2
    print(total) 

if __name__ == "__main__":
    main()

