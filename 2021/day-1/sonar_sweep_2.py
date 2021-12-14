def sonar_sweep():
    file = open("input.txt", "r").readlines()

    increased = 0

    # First three-measurement sliding window
    current = int(file[0]) + int(file[1]) + int(file[2])

    for i in range(len(file) - 2):
        if int(file[i]) + int(file[i + 1]) + int(file[i + 2]) > current:
            increased += 1
        current = int(file[i]) + int(file[i + 1]) + int(file[i + 2])

    return increased


if __name__ == "__main__":
    result = sonar_sweep()
    print(result)
