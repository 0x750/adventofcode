def get_data(d):
    with open("./input/" + str(d) + ".txt", 'r') as i:
        return i.read().split(',')

def init(comp, noun, verb):
    comp = list(map(lambda x: int(x), comp))
    comp[1] = noun
    comp[2] = verb
    return comp

def exec_command(comp, index):
    if comp[index] == 1:
        comp[comp[index + 3]] = comp[comp[index + 1]] + comp[comp[index + 2]]
    if comp[index] == 2:
        comp[comp[index + 3]] = comp[comp[index + 1]] * comp[comp[index + 2]]
    return comp

def main():
    base = get_data(2)
    for i in range(0,99):
        for j in range(0,99):
            data = init(base, i, j)
            index = 0
            while data[index] != 99:
                data = exec_command(data, index)
                index += 4
            if data[0] == 19690720:
                print(i, j, 100 * i + j)

if __name__ == "__main__":
    main()