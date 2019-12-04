def get_data(d):
    with open("./input/" + str(d) + ".txt", 'r') as i:
        return i.read().split(',')

def init(comp):
    comp = list(map(lambda x: int(x), comp))
    comp[1] = 12
    comp[2] = 2
    return comp

def exec_command(comp, index):
    if comp[index] == 1:
        comp[comp[index + 3]] = comp[comp[index + 1]] + comp[comp[index + 2]]
    if comp[index] == 2:
        comp[comp[index + 3]] = comp[comp[index + 1]] * comp[comp[index + 2]]
    return comp

def main():
    data = init(get_data(2))
    index = 0
    while data[index] != 99:
        data = exec_command(data, index)
        index += 4
    print(data[0])

if __name__ == "__main__":
    main()