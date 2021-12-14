def dive():
    horizontal = 0
    depth = 0
    aim = 0

    file = open("input.txt", "r").readlines()

    for item in file:
        command, value = item.split(" ")

        if command == "forward":
            horizontal += int(value)
            depth += aim * int(value)
        elif command == "down":
            aim += int(value)
        elif command == "up":
            aim -= int(value)

    return horizontal * depth


if __name__ == "__main__":
    result = dive()
    print(result)
