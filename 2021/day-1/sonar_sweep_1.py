def sonar_sweep():
    file = open("input.txt", "r").readlines()

    increased = 0

    # First measurement
    current = int(file[0])

    for elem in file:
        if int(elem) > current:
            increased += 1
        current = int(elem)
    
    return increased

if __name__ == "__main__":
    result = sonar_sweep()
    print(result)