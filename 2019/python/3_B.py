def get_data(d):
    with open("./input/" + str(d) + ".txt", 'r') as i:
        return i.read().splitlines()

def get_path(text):
    ta = text.split(',')
    current = (0,0)
    path = [current]
    for direction in ta:
        if direction[0] == 'U': # UP
            for i in range(int(direction[1:])):
                current = (current[0], current[1] + 1)
                path.append(current)
        
        if direction[0] == 'D': # DOWN
            for i in range(int(direction[1:])):
                current = (current[0], current[1] - 1)
                path.append(current)
        
        if direction[0] == 'L': # LEFT
            for i in range(int(direction[1:])):
                current = (current[0] - 1, current[1])
                path.append(current)
        
        if direction[0] == 'R': # RIGHT
            for i in range(int(direction[1:])):
                current = (current[0] + 1, current[1])
                path.append(current)
        
    return path

def get_total_dist(point, paths):
    return paths[0].index(point) + paths[1].index(point)


def main():
    data = get_data(3)
    path = [list(), list()]
    # Get paths
    for i in range(len(data)):
        path[i] = get_path(data[i])
    # Get all intersections
    all_intersection = list(set(path[0]).intersection(path[1]))
    # Get the closest intersection
    all_intersection.remove((0,0))
    print(get_total_dist(min(all_intersection, key=lambda x: get_total_dist(x, path)), path))
    

if __name__ == "__main__":
    main()